## Introduction

The ultimate aim of this framework is unifying sociological simulation experiments into a single framework from both theoretical and code design perspectives. Currently, competeai is the only instance under this framework. The construction of this framework is based on the following fundamental ideas:

- Most sociological experiments can be decomposed into several scenes, where various agents interact in a certain order within each scene.
  - For example, in the competeai experiment, it can be broken down into scenes such as restaurant management, customer group discussions, customer dining, and feedback. In the first scene of restaurant management, the agent playing the role of the boss needs to modify each restaurant module in sequence. In the second scene of customer group discussions, the customers need to speak in a certain order, and so on.
- Currently, many multi-agent frameworks do not allow agents to complete tasks within a scene based solely on the initial prompt settings. Therefore, it is necessary to add prompts at several nodes in the simulation to guide the agents in completing this part of the simulation.
  - For instance, in restaurant management, if only a few management tasks (e.g., chef management, menu management) are mentioned at the beginning, agents cannot successfully complete these tasks without prompts guiding their actions before each management task.


## Installation Requieremnts

basic 
```
sudo apt update && sudo apt upgrade
```
enviroment
```install conda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

**Note: the framework has only been tested on linux.**

First, clone the repo:

```bash
git clone https://github.com/juanguerralatam/marketCompete
```

Then

```bash
cd competeai
```

To install the required packages, you can create a conda environment:

```enviroment
source ~/miniconda3/bin/activate
conda create --name competeai python=3.10
conda activate competeai
pip install -r requirements.txt

```

## How to run

First, add a environment variable into your environment config file:

```bash
export OPENAI_KEY='sk-xxx'
```

Next, launch Django database server

```bash
./database.sh restart
```

Then, open a new terminal, run the following command: 

```bash
python run.py <exp_name>
```

The result will save into `logs/<exp_name>`

## The structure of framework

```bash
.
├── database                       <- Database management system for restaurant simulation
├── database.sh                    <- Script file for operating the database
├── logs                           <- Where all experiment results are recorded, part of the pipeline
├── README.md                      <- You are here
├── run.py                         <- Entry point for the program
├── competeai                       <- Core folder
│   ├── agent                     <- Core component of the framework: agent. Allows for setting up more complex agent structures
│   │   ├── agent.py               <- Completes agent observation, reaction, and execution model (essentially the process of inputting a prompt and outputting a response)
│   │   ├── backends               <- Different large models can simulate an agent, but gpt4 is generally used
│   │   │   ├── openai.py
|   |   |   └── ...
│   │   └── __init__.py
│   ├── config.py
│   ├── examples                   <- Each simulation experiment needs such a configuration file, specifying the participating agents, their roles, and the supporting LLMs
│   │   ├── group.yaml
│   │   └── restaurant.yaml
│   ├── globals.py
│   ├── image.py
│   ├── __init__.py
│   ├── message.py                 <- Core component of the framework: message. Every response made by an agent counts as a message, which includes the content of the response, the owner (agent) of the message, who can see the message, etc.
│   ├── prompt_template            <- Core component of the framework: prompt template. Prompts needed in the interaction process are given to agents at appropriate times to guide their actions
│   │   ├── dine
│   │   │   ├── comment.txt
│   │   │   ├── feeling.txt
│   │   │   └── order.txt
│   │   ├── group_dine
│   │   │   └── ...
│   │   └── restaurant_design
│   │       └── ...
│   ├── relationship.yaml
│   ├── scene                     <- Core component of the framework: scene. Each scene implements a sequence of agent interactions, such as a discussion phase among multiple customers.
│   │   ├── base.py
│   │   ├── dine.py
│   │   ├── group_dine.py
│   │   ├── __init__.py
│   │   └── restaurant_design.py
│   ├── simul.py                  <- Core file: responsible for coordinating multiple scenes to run, allowing scenes to run in any order
│   └── utils                     <- Some tools
│       ├── analysis.py
│       ├── database.py
│       ├── draw.py
│       ├── image.py
│       ├── __init__.py
│       ├── log.py
│       ├── prompt_template.py
└── test                          <- Unit test files
    ├── get_base64.py
    └── ...
```


