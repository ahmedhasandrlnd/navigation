# Project report
### Learning algorithm
The learning algorithm used is vanilla Deep Q Learning as described in the [original paper](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf). As batch of vector of state is used as input instead of an image, so convolutional neural nework is replaced with deep neural network. 
![DQN Algorithm](images/dqn_algorithm.png)

The deep neural network has following layers:

Fully connected layer - input: 37 (state size) output: 128
Fully connected layer - input: 128 output 64
Fully connected layer - input: 64 output: (action size)
Parameters used in DQN algorithm:

Maximum steps per episode: 1000
Starting epsilion: 1.0
Ending epsilion: 0.01
Epsilion decay rate: 0.999