import gym
from gym import spaces
from vizdoom import *
import numpy as np

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def init(self):
        super().init()
        self.game = vizdoom.DoomGame()
        self.game.load_config("/home/hell-cat/Storage/Codec/IV_Stuff/StableBaseline/Doom/ViZDoom/scenarios/basic.cfg")
         #rendering window is off
        self.game.set_window_visible(False)
        # Initialize the game
        self.game.init()

        # Action and observation space
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(3, 240, 320), dtype=np.uint8)

    def step(self, action):
        actions = [[1, 0, 0],  # 0
                   [0, 1, 0],  #  1
                   [0, 0, 1]]  #  2

        # Execute the action and get the reward
        reward = self.game.make_action(actions[action], 4)  # Frame skip parameter

        # Check if the episode is done
        done = self.game.is_episode_finished()

        # Get the new state
        if not done:
            state = self.game.get_state().screen_buffer
        else:
            state = np.zeros(self.observation_space.shape)

        return state, reward, done, {}

    def reset(self):
        self.game.new_episode()  # Start a new episode
        state = self.game.get_state().screen_buffer
        return state

    def render(self, mode='human'):
        pass

    def close(self):
        self.game.close()  # Close the game
