config = {
  'episodes': 1,
  'timesteps': 1000
}

import gym

env = gym.make('CartPole-v0')
env.reset()

for i_episode in range(config['episodes']):
  obs = env.reset()
  for t in range(config['timesteps']):
    env.render()
    print(obs)
    
    action = env.action_space.sample() # 0 = left, 1 = right
    obs, reward, done, info = env.step(action)
    
    if (done):
      print(f'Episode {i_episode} finished after {t} timesteps.')
      break
  
env.close()