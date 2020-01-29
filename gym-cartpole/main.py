# Gym setup from: https://gym.openai.com/docs/
# Q learning basics from: https://www.oreilly.com/radar/introduction-to-reinforcement-learning-and-openai-gym/

import numpy as np
import gym
config = {
    'episodes': 1000,
    'timesteps': 1000,
    'alpha': 0.618
}


env = gym.make('Taxi-v3')
env.reset()

Q = np.zeros([env.observation_space.n, env.action_space.n])

for i_episode in range(config['episodes']):
    state = env.reset()
    G = 0  # accumulated reward per episode
    for t in range(config['timesteps']):

        # action = env.action_space.sample() # 0 = left, 1 = right
        # do whatever we think will lead to the most reward
        action = np.argmax(Q[state])
        obs, reward, done, info = env.step(action)  # take the action

        # fancy formula that is based on the bellman equation (whatever that is)
        Q[state, action] += config['alpha'] * \
            (reward + np.max(Q[obs]) - Q[state, action])

        G += reward
        state = obs

        if (i_episode % 50 == 0):
            env.render()
            if (done):
                print(f'Episode {i_episode} finished after {t} timesteps with total reward {G}.')
        
        if done: 
            break

env.close()
