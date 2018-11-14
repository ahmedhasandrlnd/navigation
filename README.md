# Navigation
Deep Reinforcement Learning Nanodegree Project 1

## Project description
For this project, the task is to train an agent to navigate (and collect bananas) in a large, square world. 

* Goal: A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal is to collect as many yellow bananas as possible while avoiding blue bananas.

* State space is 37 dimensional and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction.

* Action space is 4 dimentional. Four discrete actions correspond to:

	* 0 - move forward
	* 1 - move backward
	* 2 - move left
	* 3 - move right
* Solution criteria: the environment is considered as solved when the agent gets an average score of +13 over 100 consecutive episodes.