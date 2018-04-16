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

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Initial%20Assessment%20-%20Greer.pdf)

## Final Self-Assessment Essays <a name="FinalSelfAssessments"></a>

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Final%20Assessment%20-%20Greer.pdf)

## Hours Summmary <a name="HoursSummary></a>
  
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

### Timetables
#### Jeremiah Greer

| Description                                                                 | Date     | Hours |
|-----------------------------------------------------------------------------|----------|-------|
| Wrote Professional Biography (Assignment 1)                                 | 8/29/17  | 3     |
| Discussed project ideas with group members                                  | 9/01/17  | 3     |
| Created project description (Assignment 2)                                  | 9/10/17  | 3     |
| Discussed details of project with group members                             | 9/17/17  | 3     |
| Found relevant libraries and papers for project                             | 9/20/17  | 3     |
| Wrote self-assessment essay (Assignment 3)                                  | 9/24/17  | 3     |
| Created user stories and design diagrams  with group members (Assignment 4) | 10/01/17 | 3     |
| Started discussing project outline and tasks                                | 10/09/17 | 3     |
| Finalized task list with group (Assignment 5)                               | 10/15/17 | 3     |
| Finished milestones, timeline, and effort matrix  with group(Assignment 6)  | 10/22/17 | 3     |
| Wrote ABET Constraint Essay with  group (Assignment 7)                      | 10/29/17 | 3     |
| Designed and recorded slideshow  presentation with group (Assignment 8)     | 11/5/17  | 3     |
| Investigated current reinforcement learning techniques                      | 11/12/17 | 3     |
| Began experimenting with tensorflow                                         | 11/19/17 | 3     |
| Finished writing fall design report with  group (Assignment 9)              | 11/27/17 | 3     |

#### Frazier Baker

| Description                                                                 | Date     | Hours |
|-----------------------------------------------------------------------------|----------|-------|
| Wrote Professional Biography (Assignment 1)                                 | 8/29/17  | 3     |
| Discussed project ideas with group members                                  | 9/01/17  | 3     |
| Created project description (Assignment 2)                                  | 9/10/17  | 3     |
| Discussed details of project with group members                             | 9/17/17  | 3     |
| Found relevant libraries and papers for project                             | 9/20/17  | 3     |
| Wrote self-assessment essay (Assignment 3)                                  | 9/24/17  | 3     |
| Created user stories and design diagrams  with group members (Assignment 4) | 10/01/17 | 3     |
| Started discussing project outline and tasks                                | 10/09/17 | 3     |
| Finalized task list with group (Assignment 5)                               | 10/15/17 | 3     |
| Finished milestones, timeline, and effort matrix  with group(Assignment 6)  | 10/22/17 | 3     |
| Wrote ABET Constraint Essay with  group (Assignment 7)                      | 10/29/17 | 3     |
| Designed and recorded slideshow  presentation with group (Assignment 8)     | 11/5/17  | 3     |
| Investigated current reinforcement learning techniques                      | 11/12/17 | 3     |
| Set up parallel-capable computational environment                           | 11/19/17 | 3     |
| Finished writing fall design report with  group (Assignment 9)              | 11/27/17 | 3     |
