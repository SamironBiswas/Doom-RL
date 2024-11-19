# Playing Doom using Deep Reinforcement Learning

This project displays the use of deep learning to teach an agent to play the classic first person shooter game Doom.

# Overview

Doom is one of the most iconic first-person shooter games, offering a dynamic and challenging environment for artificial intelligence experimentation. In this project, we use deep reinforcement learning to teach an AI agent to play the basic map of Doom. The agent learns to navigate and react to the environment, with the primary objective being to shoot the monster as fast as possible.

# The Environment

State Space: The model receives a snapshot of the current game state as input, represented by the raw pixel data visible to the player. These inputs are typically RGB frames, capturing the visual information needed for decision-making.

Action Space: There are only 3 basic actions - Move left, move right, shoot. To keep things simple, only one action will be taken at a time.

Rewards: The agent is deducted points for taking actions without results, such as unnecessary strafing and reckless shooting. It is rewarded heavily for shooting the target.

# Requirements
- Python 3.x (or Greater)
- [OpenAi Gym]([https://gymnasium.farama.org/])
- [ViZDoom](https://github.com/Farama-Foundation/ViZDoom/tree/master)

# Installation 
- Install OpenAi Gym
   ``` bash
   git clone https://github.com/openai/gym 
-  Clone the Repository:
   ``` bash  
   git clone https://github.com/AJ-SM/IV_Tasks/tree/main/Mini_Grid)](https://github.com/AJ-SM/IV_Tasks/tree/main/Mini_Grid

# Working

The training process for this project involves initializing a custom environment using OpenAI Gym's framework, which is specifically designed for reinforcement learning tasks. The custom environment is based on the classic game Doom and integrates seamlessly with the reinforcement learning algorithms provided by the Stable-Baselines3 library.

Environment Initialization
The Doom environment is initialized through a custom implementation (CustomEnv) that defines the game's state space, action space, and reward structure. The state space consists of raw pixel data (RGB frames), which captures the visual game state as seen by the player. The agent interacts with the environment by taking actions (e.g., shooting), and it receives rewards based on its performance, such as successfully hitting a target.

Training Procedure
The training process employs the Proximal Policy Optimization (PPO) algorithm from Stable-Baselines3. The key steps are as follows:

Environment Setup:
The environment is instantiated, and necessary directories for saving models and logging data are created (MODELS/PPO for saving trained models and logs for TensorBoard monitoring).

Model Initialization:
A PPO model with the MlpPolicy policy is initialized. The MlpPolicy uses a multi-layer perceptron to process the input state and make decisions.

Training Loop:
The training is conducted in a loop, where the model learns from the environment in increments of TIMESTEPS (e.g., 10,000 timesteps per iteration). After every iteration:

The model is updated based on the collected experience.
The model is saved periodically for backup and future use.
Progress Monitoring:
Training metrics such as mean episodic length and mean episodic rewards are logged using TensorBoard. This provides a visual representation of the model's performance and allows for easy monitoring of its progress over time.

# Results

Below is a demonstration of our trained model in action.

https://github.com/user-attachments/assets/3f0943eb-a79a-4a28-95a9-fabc5494f044



The results of training are as shown.

Increase in rewards as the agent learns:
![image](https://github.com/user-attachments/assets/51c77a2d-f094-43be-8c36-d53e5854bb8d)

Decrease in length of each episode as the agent learns:
![image](https://github.com/user-attachments/assets/36a6916d-47c2-48c7-a679-af54dbc03e9f)


