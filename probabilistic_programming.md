
We need to think about the inputs. we know how to represent input, but we don't know how they relate.

CNNs kind of do this, as do RNNs, but it's hard to say any certain inputs are grouped in some way

treat every input as if they are generated from a certain function, such as a normal curve.

mixture model: some number of clumps, maybe saying there's three means and std devs

"here are the relations I expect to see, what are the parameters that generate this data?"

advantages
	the model is more "general", once trained it can classify, fill in information, generate
	less likely to overfit, since it kind of knows what it's looking for

drawbacks:
	you never know if you've trained for long enough, just like neural networks
	very slow to train

training
	markov chain monte carlo (MCMC)
		probability of transitions between states
		start with random parameters for the distributions
		takes samples, tweak the parameters until it looks like the distributions
	example
		https://pystan.readthedocs.io/en/latest/optimizing.html

