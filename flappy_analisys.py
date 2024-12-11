#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

reward_data = np.loadtxt('AverageReward.txt')
epochs = reward_data[:,0]
rewards = reward_data[:,1]

qmax_data = np.loadtxt('AverageQmax.txt')
qmax = qmax_data[:,1]

plt.figure(figsize=(8,6))

#plt.scatter(X, Y, color='red')
plt.subplot(2,1,1)
plt.grid()
plt.title('Average reward on flappy bird')
plt.xlabel("Training Epochs / 10000")
plt.ylabel("Average reward per Episode")
plt.plot(epochs, rewards)

plt.subplot(2,1,2)
plt.grid()
plt.title('Average Qmax on flappy bird')
plt.xlabel("Training Epochs / 10000")
plt.ylabel("Average Qmax per Episode")
plt.plot(epochs, qmax)
plt.subplots_adjust(hspace = 0.5, wspace=0.3)
plt.savefig('flappy_results.png')
plt.show()
