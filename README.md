# Banana-collector

## The Project
Banana Collector is the first project of Deep Reinforcement Learning Nanodegree from Udacity.
The main objective here is to solve an environment (Unity Banana Environment) using deep reinforcement learning techniques.

## The Environment
The environment banana.app was develop and provided by Udacity team. The environment is composed by and agent that has to collect yellow bananas avoiding blue bananas. The yellow bananas give the agent +1 as reward whereas the blue ones give it -1. The problem is considered solved when the trained agent reaches an average of 13 points on afetr 100 episodes.

## The solution
To solve the problem an agent is trained using reinforcement learning techniques. The implementation is written in PyTorch and Python 3.6 that implements a Deep Q-Network in order to help training the agent.

## Getting Started
In order to run this code, install the following dependencies:

pip install unityagents

pip install torch

pip install matplotlib
