# Faour Hand

This repository contains the result of our work in the scope of the 151-0615-00L Real-World Robotics - A Hands-On Project Class at ETH Zürich.
The goal was to imagine, design, build, train, operate, test and challenge a dexterous robotic hand. Here is the content of the resulting work.

## Content

The content of this repo is composed of 3 parts :

### RL

The content of this part is directly a fork of the ressource provided by the Soft Robotic Lab of ETH Zürich, as this course is a direct extension of their research. They gave a working RL environnement already set up and tested for the IsaacGym framework. For conveinience, we forked the [related repository](https://github.com/srl-ethz/faive_gym_oss) and republished it with our own hand in the files. Please refer to the original repository for the setup and give them all the credit for their amazing work.

The minor improvement are the addition of different tasks and their related PPO, as well as a scheduler do batch launch every combination of parameters in a user defined intervals. We also provide the results of our training in the recording and runs folder.

### Control

The control submodule includes both teleoperation and autonomous modes for full control of the hand. The teleoperation mode uses an Oakd Depth camera for direct hand mimicry. The autonomous mode replays a learned RL policy for the purpose of rolling a ball. All the code is written on a backbone provided by the RWR team.

### CAD

Access https://a360.co/43FZL2z for the final CAD prototype of the hand.

## Other comments
Don't forget to read the paper for the SRL about the main project this work is derived from. This project is for a class backed on their academic work, so all the credit is their, not our.
```
@misc{toshimitsu2023getting,
	title={Getting the Ball Rolling: Learning a Dexterous Policy for a Biomimetic Tendon-Driven Hand with Rolling Contact Joints}, 
	author={Yasunori Toshimitsu and Benedek Forrai and Barnabas Gavin Cangan and Ulrich Steger and Manuel Knecht and Stefan Weirich and Robert K. Katzschmann},
	year={2023},
	eprint={2308.02453},
	archivePrefix={arXiv},
	primaryClass={cs.RO}
}
```
