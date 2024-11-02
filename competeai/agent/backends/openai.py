# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
# Source Attribution:
# The majority of this code is derived from the following sources:
# - Chatarena GitHub Repository: https://github.com/Farama-Foundation/chatarena

import os
import re
import time
from typing import List
from tenacity import retry, stop_after_attempt, wait_random_exponential
from openai import OpenAI

from .base import IntelligenceBackend
from ...message import Message, SYSTEM_NAME, MODERATOR_NAME


try:
    openai_api_key = os.environ.get("OPENAI_KEY")
    
    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set. Please set the environment variable OPENAI_API_KEY")
    
    is_openai_available = True

except ImportError:
    is_openai_available = False

total_tokens = 0

# Default config follows the OpenAI playground
DEFAULT_TEMPERATURE = 0.9
DEFAULT_MAX_TOKENS = 1024
DEFAULT_MODEL = "gpt-4o-mini"

END_OF_MESSAGE = "<EOS>"  # End of message token specified by us not OpenAI
STOP = ("<|endoftext|>", END_OF_MESSAGE)  # End of sentence token
BASE_PROMPT = f"The messages always end with the token {END_OF_MESSAGE}."


class OpenAIChat(IntelligenceBackend):
    """
    Interface to the ChatGPT style model with system, user, assistant roles separation.
    """
    stateful = False
    type_name = "openai-chat"

    def __init__(self, temperature: float = DEFAULT_TEMPERATURE, max_tokens: int = DEFAULT_MAX_TOKENS,
                 model: str = DEFAULT_MODEL, merge_other_agents_as_one_user: bool = False, **kwargs):
        """
        Instantiate the OpenAIChat backend.
        Args:
            temperature: the temperature of the sampling
            max_tokens: the maximum number of tokens to sample
            model: the model to use
            merge_other_agents_as_one_user: whether to merge messages from other agents as one user message
        """
        assert is_openai_available, "openai package is not installed or the API key is not set"
        super().__init__(temperature=temperature, max_tokens=max_tokens, model=model,
                         merge_other_agents_as_one_user=merge_other_agents_as_one_user, **kwargs)

        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model = model
        self.merge_other_agent_as_user = merge_other_agents_as_one_user

    @retry(stop=stop_after_attempt(6), wait=wait_random_exponential(min=4, max=60))
    def _get_response(self, messages):
        global total_tokens
        
        """ OpenAI 1.00 API """
        
        client = OpenAI(api_key=openai_api_key)
        
        completion = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop=STOP
        )

        response = completion.choices[0].message.content
        response = response.strip()
        return response


    def query(self, agent_name: str, agent_type: str, role_desc: str, history_messages: List[Message], 
              relationship: str = None, global_prompt: str = None, request_msg: Message = None, *args, **kwargs) -> str:
        """
        Format the input and call the ChatGPT/GPT-4 API.
        Args:
            agent_name: the name of the agent
            role_desc: the description of the role of the agent
            env_desc: the description of the environment
            history_messages: the history of the conversation, or the observation for the agent
            request_msg: the request from the system to guide the agent's next response
        """
        messages = []
        
        # System-level instructions
        system_prompt = f"Your name is {agent_name}.\n\nYour role:{role_desc}"
        if global_prompt:  # Prepend the global prompt if it exists
            system_prompt = f"{global_prompt.strip()}\n\n" + system_prompt
        if relationship:
            system_prompt += f"\n\nYour relationship: {relationship.strip()}"
        system_prompt += f"\n\n{BASE_PROMPT}"
        
        system_message = {"role": "system", "content": system_prompt}
        messages.append(system_message)
        
        # Conversation history
        if len(history_messages) > 0:
            user_messages = []
            if len(history_messages) > 12:  # Limit context length
                history_messages = history_messages[-12:]
            for msg in history_messages:
                user_messages.append((msg.agent_name, f"{msg.content}{END_OF_MESSAGE}"))

            user_prompt = ""
            for _, msg in enumerate(user_messages):
                user_prompt += f"[{msg[0]}]: {msg[1]}\n"
            user_prompt += f"You are a {agent_type} in a virtual world. Now it's your turn!"
            
            user_message = {"role": "user", "content": user_prompt}
            messages.append(user_message)

        # Generate response
        response = self._get_response(messages, *args, **kwargs)
        
        # Remove the agent name if the response starts with it
        response = re.sub(rf"^\s*\[.*]:", "", response).strip()
        response = re.sub(rf"^\s*{re.escape(agent_name)}\s*:", "", response).strip()

        # Remove the trailing end of message token
        response = re.sub(rf"{END_OF_MESSAGE}$", "", response).strip()
        
        return response
