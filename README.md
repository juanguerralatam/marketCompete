## Introduction

The ultimate aim of this repository is to unify the study of competitive dynamics in the global marketplace into a cohesive framework, integrating both theoretical insights and practical code design. Currently, the focus is on the competitive dynamics of Born Global companies, particularly their interactions with established Multinational Corporations (MNCs). The construction of this framework is based on the following fundamental ideas:

The global marketplace can be dissected into various scenarios, where Born Global companies and MNCs interact in specific contexts.
For example, in the scenario of market entry, Born Global companies must navigate regulatory hurdles, establish brand presence, and secure supply chains. In the scenario of product development, these firms must balance innovation with cost efficiency, while in the scenario of cost leadership, they must optimize operations and pricing strategies. Each of these scenarios requires a sequence of strategic decisions and interactions.
Many existing models fail to capture the full complexity of these interactions based solely on initial conditions. Therefore, it is necessary to introduce dynamic factors at various stages of the simulation to guide the strategic decisions of Born Global companies and MNCs.
For instance, in the market entry scenario, if only basic regulatory requirements are outlined at the outset, companies cannot successfully navigate the complexities without additional guidance on local market nuances, cultural considerations, and competitive strategies. Similarly, in product development, companies need prompts to guide their decisions on technology adoption, design iterations, and customer feedback integration.

This repository aims to provide a comprehensive simulation framework powered by Large Language Models (LLMs) to explore these dynamics. By simulating interactions across diverse economic contexts, we identify critical success factors that enable Born Global companies to thrive despite resource constraints and the dominance of larger players. Our findings offer valuable insights into how these firms can leverage their agility, technological adoption, and innovative cultures to achieve competitive advantages and rapid internationalization. This research contributes to both academic theory and managerial practice, providing a nuanced understanding of how Born Global firms can strategically position themselves for long-term growth in an increasingly interconnected global economy.


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
git clone https://github.com/juanguerralatam/marketcompete
```

Then

```bash
cd marketcompete
```

To install the required packages, you can create a conda environment:

```enviroment
source ~/miniconda3/bin/activate
conda create --name marketcompete python=3.10
conda activate marketcompete
pip install -r requirements.txt

```

## Test requiments
1. Open Source models using Ollama refert to ollama instalation.
    Download Deepseek-R1, LLama 3.2 and Qwen
    In folder test run ollama.py 

2. Propierary models can be run using the current API
    First, add a environment variable into your environment config file:
```bash
export OPENAI_API_KEY="sk-xxx"
```
    In folder test run openAI.py

3. launch Django database server for normal SQL query
```bash
./database.sh restart
```
4. (Optional) You can also use mode AI datavector base like MondoBD Atlas

## Run the framwork

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

## Citation

If you find ChatArena useful for your research, please cite our repository (our arxiv paper is coming soon):

```bibtex
@software{ChatArena,
  author = {Yuxiang Wu, Zhengyao Jiang, Akbir Khan, Yao Fu, Laura Ruis, Edward Grefenstette, and Tim Rocktäschel},
  title = {ChatArena: Multi-Agent Language Game Environments for Large Language Models},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  version = {0.1},
  howpublished = {\url{https://github.com/chatarena/chatarena}},
}
```

## Contact

If you have any questions or suggestions, feel free to open an issue or submit a pull request.

Happy chatting!

## Sponsors

We would like to thank our sponsors for supporting this project:

- [HITsz](https://www.hitsz.edu.cn/)
