
https://arxiv.org/pdf/1604.00289.pdf

## Abstract
machines do things, but not like humans. The use priors.
AI should:
1. Understand causality
2. Be grounded in physics and psychology
3. Rapid generalization

# 1. Introduction

neural networks cannot emulate a brain... which makes sense they are far too small.

statistical, pattern recognition, prediction first
alternative approach, model building.

prediction vs explination

humans are model based, although pattern recognition is also "support" the building of models.

"rich infrecnces from small amounts of training data"

reverse engineering humans is useful when humans are better than machines.

## 1.2 Overview of Key Ideas

### "start up software" aka priors
The earlier something exists, the more likely that it is part of future learning.  
earliest things are priors.

This paper focuses on intuitive physics and intuitive psychology

### learning
causual models

compositionability, when the larger thing (sentence?) is entirely defined by the ordering and meaning of its subparts (grammar, words) (https://plato.stanford.edu/entries/compositionality/)
"learning to learn", curiosity?

### reaction speed

humans can think quickly, react quickly in novel situations

building infrence based models is slow, but traditional pattern recognition techniques can help speed this up.

in humans, infrence based and pattern recognition are used both "colaboratively and cooperatively"??

### 2. "cognitive and neural inspiration in artificial inteligence"

historic behaviorism, mind as a blank notebook, alan turing

later, built on that and assumed that human knowledge and cognition could be thought of as symbols and operations.

neurons => paralell distributed processing (pdp)
    knowledge learned is "distributed across neurons"
    current state of the art deep learning is basically pdp with more compute and data
    **PDP is also compatible with model building**

end pg7

30 Mar 2020

big neural nets don't mimic humans, but they are the best we have in many fields.

macaque IT cortex?

care alot about **small amounts of training data**

when written, convolutional neural nets can achieve near human performance on *specific data sets*  
But humans still learn better -- less data, able to imagine/draw new characters, describe parts

Probabilistic program induction?

planning over time is always hard... seeing the world as goal setting? (wait but why has something on that I think)

deep q learning as a connectionist model?

Even though the same model was used to play all the atari games, it was retrained for each game so the end state, weights, etc were still specialized to that game only.
500x more training time than a human, only 10% performance...  
Later iterations achieved better "ratio" (80-90%) through specialized tuning (better experience replay, parameter sharing?)

Humans learn faster than techniques we have, so maybe the techniques we have are doing something different...

end pg 13

Human flexibility is still crazy -- change colors and DQN breaks

different goals listen on pg14 are interesting,,, shows that humans build intermediete knowledge?

**How do humans retain prior knowledge, and how is it structured?**

"in ways contemporary machine learning has yet to capture"... this is the researcher's outlook on ML.

# 4. Core ingredients of human intelligence

## 4.1 Physics

the concept of an internal "physics engine" developed at an early age

crude/inaccurate/probabilistic but "good enough"

"conectionist models" again?

can models be trained to learn physics based on "infant perception"?

end pg 18
