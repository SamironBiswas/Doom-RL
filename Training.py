
from stable_baselines3 import PPO
import numpy as np
import gym
import random
import CustomEnv 

import time 
import os 
models_dir = "MODELS/PPO"
logdir = "logs"

env = CustomEnv()
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env.reset()

model = PPO("MlpPolicy",env,verbose=1,tensorboard_log=logdir)

TIMESTEPS = 10000
steps = 300
for step in range(steps):
    model.learn(total_timesteps=TIMESTEPS,reset_num_timesteps=False,tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*step}")
