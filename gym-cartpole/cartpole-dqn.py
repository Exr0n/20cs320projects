"""
Source: https://gym.openai.com/evaluations/eval_EIcM1ZBnQW2LBaFN6FY65g/

What I did is I downloaded this person's code and commented it, so that I understand how it works.
"""

import random
import gym
import math
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class DQNCartPoleSolver():
    '''
    * = not fully understood
    n_episodes: number of episodes to train for
    n_win_ticks: number of ticks to survive in an episode to consider the environment solved
    max_env_steps: stop an episode after this many steps (fallback incase the episode doesn't end)
    *gamma: scalar value for the Q Learning equation
        (I don't understand this fully, I think it scales what the penalty for predicting future rewards is?)
    epsilon: chance that we choose a random action
    epsilon_min: minimum epsilon after decay
    *epsilon_log_decay: speed of the epsilon decay (log scale or something)
    *alpha: some paramater for the prediction network optimizer
    *alpha_decay: also goes into the dense network optimizer
    batch_size: number of randomly sampled experiences to train the predictor network on
    '''
    def __init__(self, n_episodes=1000, n_win_ticks=195, max_env_steps=None, gamma=1.0, epsilon=1.0, epsilon_min=0.01, epsilon_log_decay=0.995, alpha=0.01, alpha_decay=0.01, batch_size=64, monitor=False, quiet=False):
        self.memory = deque(maxlen=100000)
        self.env = gym.make('CartPole-v0')
        if monitor: self.env = gym.wrappers.Monitor(self.env, './data/cartpole-1', force=True)
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_log_decay
        self.alpha = alpha
        self.alpha_decay = alpha_decay
        self.n_episodes = n_episodes
        self.n_win_ticks = n_win_ticks
        self.batch_size = batch_size
        self.quiet = quiet
        if max_env_steps is not None: self.env._max_episode_steps = max_env_steps

        # Init model
        self.model = Sequential()
        self.model.add(Dense(24, input_dim=4, activation='tanh'))
        self.model.add(Dense(48, activation='tanh'))
        self.model.add(Dense(2, activation='linear'))
        self.model.compile(loss='mse', optimizer=Adam(lr=self.alpha, decay=self.alpha_decay)) # TODO: I don't understand how optimizers work

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def choose_action(self, state, epsilon):
        return self.env.action_space.sample() if (np.random.random() <= epsilon) else np.argmax(self.model.predict(state))

    def get_epsilon(self, t):
        return max(self.epsilon_min, min(self.epsilon, 1.0 - math.log10((t + 1) * self.epsilon_decay)))

    def preprocess_state(self, state):
        return np.reshape(state, [1, 4]) # TODO: I don't understand why this needs to be reshaped

    def replay(self, batch_size):
        x_batch, y_batch = [], []
        minibatch = random.sample( # pick batch_size experiences (ticks)
            self.memory, min(len(self.memory), batch_size))
        for state, action, reward, next_state, done in minibatch:
            y_target = self.model.predict(state) # see what the model would have guessed for this state
            y_target[0][action] = reward if done else reward + self.gamma * np.max(self.model.predict(next_state)[0]) # fix the predicted reward to also take the final reward of the episode into account
            x_batch.append(state[0]) # training input
            y_batch.append(y_target[0]) # training solution
        
        # train the model on the previous experiences enhanced with the reward from the future
        self.model.fit(np.array(x_batch), np.array(y_batch), batch_size=len(x_batch), verbose=0)
        if self.epsilon > self.epsilon_min: # decay the chance that we pick a random action each time the model gets better
            self.epsilon *= self.epsilon_decay

    def run(self):
        scores = deque(maxlen=100)

        for e in range(self.n_episodes):
            state = self.preprocess_state(self.env.reset())
            done = False
            i = 0
            while not done: # run the episode
                action = self.choose_action(state, self.get_epsilon(e))
                next_state, reward, done, _ = self.env.step(action)
                next_state = self.preprocess_state(next_state) # preprocess for storage and Q learning purposes
                self.remember(state, action, reward, next_state, done)
                state = next_state
                i += 1

            scores.append(i)
            mean_score = np.mean(scores)
            if mean_score >= self.n_win_ticks and e >= 100: # if we consider that we won and it wasn't an accident
                if not self.quiet: print('Ran {} episodes. Solved after {} trials ✔'.format(e, e - 100))
                return e - 100
            if e % 100 == 0 and not self.quiet:
                print('[Episode {}] - Mean survival time over last 100 episodes was {} ticks.'.format(e, mean_score))

            self.replay(self.batch_size) # retrain the prediction network with this new experience
        
        if not self.quiet: print('Did not solve after {} episodes 😞'.format(e))
        return e

if __name__ == '__main__':
    agent = DQNCartPoleSolver(n_episodes=5000, monitor=True, batch_size=256)
    agent.run()
