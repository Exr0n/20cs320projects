# Goal: create a "human" agent where a human can interact with the client

import gym

import numpy as np
import gym
from tkinter import Tk
import time

config = {
    'framerate': 5
}


class Episode():
    def __init__(self):
        self.env = gym.make('CartPole-v0')
        self.state = self.env.reset()
        self.done = False
        self.next_action = 1

    def step(self, action=None):
        if (self.done):
            print("Episode finished!")
            self.env.close()
            return None

        if action is None:
            action = self.next_action

        # action = self.env.action_space.sample() # 0 = left, 1 = right
        print(f'taking action {action}')
        out = self.env.step(action)  # take the action
        self.state = out[0]
        self.done = out[-1]

        self.env.render()

        return out

    def on_key(self, event=None):
        if event is None:
            return

        key = event.keysym
        if key == 'Left':
            print("Stepping left")
            # self.next_action = 0
            self.step(0)
        elif key == 'Right':
            print("Stepping right")
            # self.next_action = 1
            self.step(1)


if __name__ == "__main__":
    ep = Episode()
    root = Tk()
    root.bind('<Any-KeyPress>', ep.on_key)

    def draw():
        root.after(int(1000/config['framerate']), draw)

    print('''
######## Playable Gym Cartpole #########
This is a human interactive version of OpenAI Gym's Cartpole.
To play, click on the tkinter window and press an arrow key...
Then click on the tkinter window again and press a left or right 
  arrow key to send an action to the environment.
Good luck!''')

    root.after(1000, draw)
    root.mainloop()
