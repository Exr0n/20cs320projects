# OpenAI Gym Cartpole Exploration

This was my first dive into the OpenAI gym and RL/Q Learning ecosystem. I wanted to get familiar with the ecosystem first, and see what kinds of things are built on the gym, before tackling solving my own environment.

I started by understanding the way OpenAI Gym environments are set up and what kind of API calls I can use, which can be seen in [gym-basics.py](./gym-basics.py). It has a simple episode timestep loop, and also implements a basic Q Learning look up table which I copied from a [tutorial](https://www.oreilly.com/radar/introduction-to-reinforcement-learning-and-openai-gym/).

Then, I moved on to more advanced Q Learning, which used a small dense Keras network to predict the future reward instead of a simple look up table. This way, the model doesn't have to train over every possible state (which would be litterally impossible for something like cartpole where the velocities can in theory be any rational number). I copied the code for this from [OpenAI's ranking page of some kind](https://gym.openai.com/evaluations/eval_EIcM1ZBnQW2LBaFN6FY65g/).

Finally, I rewrote the OpenAI Gym interaction to work with a human player, just so that I could get a better sense of what it would like being the model in the environment. In the future, I might train a model to predict the human player's action given a state, so that I don't have to deal with the Q learning equations that I don't yet fully understand.
