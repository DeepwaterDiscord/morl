# MORL Fall 2017 Design Report
**Team:** Frazier Baker and Jeremiah Greer<br/>
**Advisor:** Dr. Fred Annexstein

1. [Abstract](#Abstract)
1. [Project Description](#Description)
1. [Test Plan and Results](#TestPlan)
1. [User Manual](#UserManual)
1. [FAQ](#FAQ)
1. [Final Presentation](#Slideshow)
1. [Poster](#Poster)
1. [Initial Self-Assessment Essays](#InitialSelfAssessments)
1. [Final Self-Assessment Essays](#FinalSelfAssessments)
1. [Hours Summary](#Hours)
1. [Appendix](#Appendix)

## Abstract <a name="Abstract"></a>

Reinforcement Learning involves learning a task through feedback based on its performance and can be expanded to include multiple measures of performance, requiring Multi-Objective Optimization. We seek to find a novel multi-objective optimization method for use in reinforcement learning. Current methods involve linear combinations of reward terms, but balancing their weights has been difficult. Instead, we plan to use Filter Methods as an alternative method of multi-objective optimization. We will test our filter method on OpenAI's MuJoCo Gym and compare our results to those using linear combination for multi-objective optimization. Finally, we hope to show generality and demonstrate real-world benefits by applying our work to other datasets.

## Description <a name="Description"></a>

#### Problem Statement

We seek to find a novel multi-objective optimization method for use in reinforcement learning.

#### Current Solutions

Current methods for multi-objective optimization involve linear combinations of the reward terms; however, balancing each of the rewards has proven difficult.
OpenAI.com has suggested that Filter Methods may be useful for multi-objective optimization and have been studied very little in relation to Reinforcement Learning.
In addition, there are many other search or optimization methods which could be derived from other subfields of Artificial Intelligence that have yet to be explored.

#### Our Approach

Our plan is to explore the use of filter methods for multi-objective optimization and reinforcement learning.
We plan to use Pareto filters to enhance the construction of multi-objective policies.
Next, we hope to test our approach using the publicly available <a href="https://gym.openai.com/envs#mujoco">OpenAI Gym environments</a>.
Finally, we hope to explore applications to other datasets that would demonstrate real-world benefits, as time permits.

## Test Plan and Results <a name="TestPlan"></a>
[Link to Test Plan](<https://github.com/DeepwaterDiscord/morl/blob/master/essays/Test%20Plan%20and%20Results.pdf>)

## User Manual <a name="UserManual"></a>

## FAQ <a name="FAQ"></a>

## Final Presentation <a name="Slideshow"></a>

[Link to MORL Presentation](https://github.com/DeepwaterDiscord/morl/blob/master/essays/MORL%20Final%20Presentation.pdf)

## Final Poster <a name="Poster"></a>

[Link to Final Poster](https://github.com/DeepwaterDiscord/morl/blob/master/essays/MORL%20Poster.pdf)

## Initial Self-Assessment Essays <a name="InitialSelfAssessments"></a>

[Baker](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Initial%20Assessment%20-%20Baker.pdf)

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Initial%20Assessment%20-%20Greer.pdf)

## Final Self-Assessment Essays <a name="FinalSelfAssessments"></a>

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Final%20Assessment%20-%20Greer.pdf)

## Hours Summary <a name="Hours"></a>
### Fall Semester
| Person     | Hours     | Description                                                           |
|------------|-----------|-----------------------------------------------------------------------|
| F. Baker   | 45        | Worked with team members on project structuring and planning, including abstract, task list, timeline, etc. In addition, looked into understanding Reinforcement Learning and Filter Methods to be able to successfully implement our plans regarding these concepts into a functional library using modern tools. Researched state-of-the-art reinforcement learning techniques and began experimenting with tensorflow. |
| J. Greer   | 45        | Worked with team members on project structuring and planning, including abstract, task list, timeline, etc. In addition, looked into understanding Reinforcement Learning and Filter Methods to be able to successfully implement our plans regarding these concepts into a functional library using modern tools. Researched state-of-the-art reinforcement learning techniques and began experimenting with tensorflow. |

### Winter Break
| Person     | Hours     | Description                                                           |
|------------|-----------|-----------------------------------------------------------------------|
| F. Baker   | 80        | Began laying groundwork for class-based system for individual learners as well as MultiLearn, creating the base learner-class system which allows users to implement any type of learner and test them in environments/configurations. Also laid the groundwork for the configuration class, which acts as a wrapper over OpenAI Gym Environments with the ability to customize them or create your own configuration outside the system entirely. Finally, a CLI tool was created to allow for easy testing of systems. |
| J. Greer   | 80        | Began experimenting with OpenAI Gym and finding modern implementations of advanced Reinforcement Learning models including Deep Q-Networks and Deep Deterministic Policy Gradients Networks. Tested the groundwork class code and connected it to OpenAI Gyms to examine the performance of each method, helping to provide feedback towards the alteration of the base class code to accomodate more complex environments. Also worked to create example configurations using OpenAI Gym to showcase the simplicity of creating a config which abstracts the training process. |

### Spring Semester
| Person     | Hours     | Description                                                           |
|------------|-----------|-----------------------------------------------------------------------|
| F. Baker   | 45        | Continued updating class system for learners and configurations for use with more advanced learners and environments. Worked with teammates to develop test suites, documentation, and set up a laptop to be used as a bulk learner for our more complex training tasks, primarily the humanoid mujoco environment using a DDPG. Finally, worked to develop a poster, presentation, and final report covering our work over the past year. |
| J. Greer   | 45        | Continued integration testing and tieing in more complex learners and environments to be used with our system. Worked with teammates to develop test suites, documentation, and set up a laptop to be used as a bulk learner for our more complex training tasks, primarily the humanoid mujoco environment using a DDPG. Finally, worked to develop a poster, presentation, and final report covering our work over the past year. |

### Total Hours and Results
| Person     | Hours     | Description                                                           |
|------------|-----------|-----------------------------------------------------------------------|
| F. Baker   | 170       | Developed a system for creating custom learners and configurations to be used for testing and analysis. In addition, we analyzed the effectiveness of using filter methods as a method of multi-objective optimization for reinforcement learning and found that, by using filter methods, we were able to achieve an increased learning rate for base tabular Q-Learning utilizing the OpenAI FrozenLake environment of approximately 1/2 the number of training iterations, and with this we can begin testing other environments to see if these findings hold for other learners and other environments. |
| J. Greer   | 170       | Developed a system for creating custom learners and configurations to be used for testing and analysis. In addition, we analyzed the effectiveness of using filter methods as a method of multi-objective optimization for reinforcement learning and found that, by using filter methods, we were able to achieve an increased learning rate for base tabular Q-Learning utilizing the OpenAI FrozenLake environment of approximately 1/2 the number of training iterations, and with this we can begin testing other environments to see if these findings hold for other learners and other environments. |

## Budget <a name="Budget"></a>

There have been no expenses to date and we do not expect any.

## Appendix <a name="Appendix"></a>

### References
* [OpenAI Requests for Research](https://openai.com/requests-for-research/)
* [MuJoCo Gym](https://gym.openai.com/envs/#mujoco)
* [Your Mapper CrimeScore](https://www.programmableweb.com/api/your-mapper-crimescore)
* [TensorFlow](https://www.tensorflow.org)
* [Pyvolution](https://pypi.python.org/pypi/Pyvolution/1.1)
* [Deap](https://github.com/DEAP/deap)
* [SciKitLearn](http://scikit-learn.org/stable/)
* [Numpy](http://www.numpy.org)
* [Python](https://www.python.org)

### Design Diagrams <a name="DesignDiagrams"></a>

![Design Diagram 1](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-UseCase-D0-Final.png)

Above shows a high-level use case model where the user (in this case a Researcher/Engineer) requests learning for some Data object, and this Data is fed through the MORL system, which uses reinforcement learning in combination with filter methods to get a result.

![Design Diagram 2](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-D1-Final.png)

Above shows a detailed view of the MORL system which goes into the Reinforcement Learning cycle and how our MultiLearn object interacts with it. 

![Design Diagram 3](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/MORL-D2-Final.png)

Above shows an in-depth detailed view of the MORL system which highlights some specific implementation-based details for our system
