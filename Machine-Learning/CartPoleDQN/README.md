This project is my first experience with Reinforcement Learning , specifically Deep Q Learning Network (DQN).

The enviroment used here is the CartPole-v1 from openAI gym: https://gym.openai.com/envs/CartPole-v1/

<i>Explaning the Program:</i>
The CartPole enviroment works as such: theres a pole on a black box that needs to be balanced on it without falling.
The rules for failing: Once the pole falls down to 15° (degrees) the run ends, Or as the box gets to the bounds of the screen.
Overall, the enviroment will procceed to run for <b>500 timesteps</b> without interruptions.

<i>The goal:</i> Train the model to last for an average time of 195 timesteps/ticks. or get to 500 ticks. (It will get both,yet the program
will stop only after achieving mean score of 195 ticks.)
