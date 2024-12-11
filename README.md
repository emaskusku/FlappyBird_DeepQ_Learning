# FlappyBird_DeepQ_Learning
# Overview
This work is an exam project of the Deep Learning course in Physics at University of Milan.
I taught a neural network to play Flappy Bird using a deep reinforcement learning algorithm, following the paper [https://arxiv.org/abs/1312.5602](https://arxiv.org/abs/1312.5602).
A PowerPoint presentation was also created about the algorithm, along with a performance study focusing on key quantities of the algorithm.

## Dependencies 
* Python 3
* TensorFlow 2
* pygame
* OpenCV-Python

## Usage
In order to train, modify these parameters in deep_q_network.py
OBSERVE = 10000
EXPLORE = 3000000
FINAL_EPSILON = 0.0001
INITIAL_EPSILON = 0.1

and comment lines between 119 and 123

then run:
python deep_q_learning

## Video
To make a video, enable the saving screen function in line 153 "save_jpg_screen(count, x_t1_col)", it will save a screen of the game frame by frame. Then run the code "makevideo.py" in "screen_saved" folder.

## References
This work is based on the following repos:

1. https://github.com/sourabhv/FlapPyBird
2. https://github.com/yenchenlin/DeepLearningFlappyBird

