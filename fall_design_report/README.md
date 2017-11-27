# MORL Fall 2017 Design Report
**Team:** Frazier Baker and Jeremiah Greer<br/>
**Advisor:** Dr. Fred Annexstein

1. [Abstract](#Abstract)
2. [Project Description](#Description)
3. [User Stories](#UserStories)
4. [Design Diagrams](#DesignDiagrams)
5. [Task List](#Tasks)
6. [Timeline](#Timeline)
7. [Effort Matrix](#Effort)
8. [ABET Constraints Essay](#ABET)
9. [Slideshow](#Slideshow)
10. [Self-Assessment Essays](#SelfAssessments)
11. [Professional Biographies](#Biographies)
12. [Budget](#Budget)
13. [Bibliography](#Bibliography)
14. [Appendix](#Appendix)

## Abstract <a name="Abstract"></a>

Reinforcement Learning involves learning a task through feedback based on its performance and can be expanded to include multiple measures of performance, requiring Multi-Objective Optimization. We seek to find a novel multi-objective optimization method for use in reinforcement learning. Current methods involve linear combinations of reward terms, but balancing their weights has been difficult. Instead, we plan to use Filter Methods as an alternative method of multi-objective optimization. We will test our filter method on OpenAI's MuJoCo Gym and compare our results to those using linear combination for multi-objective optimization. We will also examine alternative methods of feature selection, such as genetic algorithms. Finally, we hope to show generality and demonstrate real-world benefits by applying our work to other datasets.

## Description <a name="Description"></a>

#### Problem Statement

We seek to find a novel multi-objective optimization method for use in reinforcement learning.

#### Current Solutions

Current methods for multi-objective optimization involve linear combinations of the reward terms; however, balancing each of the rewards has proven difficult.
OpenAI.com has suggested that Filter Methods may be useful for multi-objective optimization and have been studied very little in relation to Reinforcement Learning.
In addition, there are many other search or optimization methods which could be derived from other subfields of Artificial Intelligence that have yet to be explored.

#### Our Approach

Our plan is to explore the use of filter methods for multi-objective optimization and reinforcement learning.
In addition, we will explore other areas of AI, particularly Genetic Programming, to find new methods of feature selection.
Next, we hope to test both of these using the publicly available <a href="https://gym.openai.com/envs#mujoco">OpenAI Gym MuJoCo environments</a>.
Finally, we hope to explore applications to other datasets that would demonstrate real-world benefits, as time permits.


## User Stories <a name="UserStories"></a>

As a **Data Scientist**,<br>
I want to **enhance feature selection**<br>
So that I can **increase the accuracy of my machine learning models.**

As a **Robotics Engineer**,<br>
I want a **better method of multi-objective Reinforcement Learning**<br>
So that **my simulated robot's performance improves.**

As a **Researcher**<br>
I want to **utilize an improved multi-objective reinforcement learning model**<br>
So that I can **extract more information from my data.**

## Design Diagrams <a name="DesignDiagrams"></a>

![Design Diagram 1](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-UseCase-D0.png)

![Design Diagram 2](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-D1.png)

![Design Diagram 3](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-D2.png)

## Task List <a name="Tasks"></a>

| Task Description                                                          | Estimated Time (days for one person) | Dependencies | Frazier's Effort | Jeremy's Effort | Optional? | 
|---------------------------------------------------------------------------|--------------------------------------|--------------|------------------|-----------------|-----------| 
| Research potential Filter Methods for use in reinforcement learning       | 7                                    |              | 40%              | 60%             | No        | 
| Find appropriate Python libraries for use with filter methods             | 1                                    | 1            | 50%              | 50%             | No        | 
| Research best practices for reinforcement learning in Tensor Flow         | 7                                    |              | 60%              | 40%             | No        | 
| Experiment with tensorflow, RL, and OpenAI Gym in Python                  | 14                                   | 3            | 50%              | 50%             | No        | 
| Research best practices for using Genetic Algorithms in feature selection | 1                                    |              | 50%              | 50%             | No        | 
| Locate fast GA Python libraries for use in feature selection              | 1                                    | 5            | 50%              | 50%             | No        | 
| Develop feature selection algorithm using filter methods                  | 14                                   | 1, 2         | 50%              | 50%             | No        | 
| Design efficient RL system in Tensorflow using current best-practices     | 14                                   | 1, 2, 3, 4   | 50%              | 50%             | No        | 
| Combine filter methods and GA in feature selection                        | 14                                   | 7, 6         | 50%              | 50%             | Yes       | 
| Integrate feature selection workflow into RL Tensorflow system            | 4                                    | 7, 9         | 50%              | 50%             | No        | 
| Develop CLI Tool for Feature Selection                                    | 4                                    | 10           | 50%              | 50%             | No        | 
| Develop UI Tool for Feature Selection                                     | 14                                   | 10           | 50%              | 50%             | Yes       | 
| Test feature selection and RL implementation on OpenAI MuJoCo Gym         | 7                                    | 11           | 50%              | 50%             | No        | 
| Test feature selection and RL implementation on Bioinformatics Data       | 7                                    | 13           | 100%             | 0%              | Yes       | 
| Test feature selection and RL implementation on Crime Rate Data           | 7                                    | 14           | 0%               | 100%            | Yes       | 
| Design Visual Aids for Presentation                                       | 14                                   | 13, 14?, 15? | 50%              | 50%             | No        | 
| Write Paper                                                               | 14                                   | 16           | 50%              | 50%             | Yes       | 


## Timeline <a name="Timeline"></a>

## Effort Matrix <a name="Effort"></a>

## ABET Constraints Essays <a name="ABET"></a>

## Slideshow <a name="Slideshow"></a>

## Self-Assessment Essays <a name="SelfAssessments"></a>

## Professional Biographies <a name="Biographies"></a>

## Budget <a name="Budget"></a>

## Bibliography <a name="Bibliography"></a>

## Appendix <a name="Appendix"></a>
