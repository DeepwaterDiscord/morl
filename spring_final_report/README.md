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
[Link To Test Plan](<https://github.com/DeepwaterDiscord/morl/blob/master/essays/Test%20Plan%20and%20Results.pdf>)

## Task List <a name="Tasks"></a>

| Task Description                                                          | Estimated Time (days for one person) | Dependencies | Frazier's Effort | Jeremy's Effort | Optional? | 
|---------------------------------------------------------------------------|--------------------------------------|--------------|------------------|-----------------|-----------| 
| Research potential Filter Methods for use in reinforcement learning       | 7                                    |              | 40%              | 60%             | No        | 
| Find appropriate Python libraries for use with filter methods             | 1                                    | 1            | 50%              | 50%             | No        | 
| Research best practices for reinforcement learning in Tensor Flow         | 7                                    |              | 60%              | 40%             | No        | 
| Experiment with tensorflow, RL, and OpenAI Gym in Python                  | 14                                   | 3            | 50%              | 50%             | No        | 
| Research best practices for using RL on different problems | 1                                    |              | 50%              | 50%             | No        | 
| Locate Python libraries for use in RL              | 1                                    | 5            | 50%              | 50%             | No        | 
| Develop policy generation algorithm using filter methods                  | 14                                   | 1, 2         | 50%              | 50%             | No        | 
| Design efficient RL system in Tensorflow using current best-practices     | 14                                   | 1, 2, 3, 4   | 50%              | 50%             | No        | 
| Combine filter methods with RL in policy generation                        | 14                                   | 7, 6         | 50%              | 50%             | Yes       | 
| Integrate policy generation workflow into RL Tensorflow system            | 4                                    | 7, 9         | 50%              | 50%             | No        | 
| Develop CLI Tool                                    | 4                                    | 10           | 50%              | 50%             | No        | 
| Develop UI Tool                                     | 14                                   | 10           | 50%              | 50%             | Yes       | 
| Test implementation on OpenAI MuJoCo Gym         | 7                                    | 11           | 50%              | 50%             | No        | 
| Test implementation Bioinformatics Data       | 7                                    | 13           | 100%             | 0%              | Yes       | 
| Test implementation on Crime Rate Data           | 7                                    | 14           | 0%               | 100%            | Yes       | 
| Design Visual Aids for Presentation                                       | 14                                   | 13, 14?, 15? | 50%              | 50%             | No        | 
| Write Paper                                                               | 14                                   | 16           | 50%              | 50%             | Yes       | 


## Timeline <a name="Timeline"></a>

| Task Id | Task Description                                                          | Start Date | End Date | 
|---------|---------------------------------------------------------------------------|------------|----------| 
| 1       | Research potential Filter Methods for use in reinforcement learning       | 12/1/17    | 12/5/17  | 
| 2       | Find appropriate Python libraries for use with filter methods             | 12/5/17    | 12/6/17  | 
| 3       | Research best practices for reinforcement learning in Tensor Flow         | 12/6/17    | 12/10/17 | 
| 4       | Experiment with tensorflow, RL, and OpenAI Gym in Python                  | 12/10/17   | 12/17/17 | 
| 5       | Research best practices for using RL on different problems | 12/17/17   | 12/18/17 | 
| 6       | Locate Python libraries for use in RL              | 12/18/17   | 12/19/17 | 
| 7       | Develop policy generation algorithm using filter methods                   | 1/2/18     | 1/9/18   | 
| 8       | Design efficient RL system in Tensorflow using current best-practices     | 1/9/18     | 1/16/18  | 
| 9       | Combine filter methods with RL in policy generation                        | 1/16/18    | 1/23/18  | 
| 10      | Integrate policy generation workflow into RL Tensorflow system            | 1/23/18    | 1/25/18  | 
| 11      | Develop CLI Tool                                    | 1/25/18    | 1/27/18  | 
| 12      | Develop UI Tool                                     | 1/27/18    | 2/3/18   | 
| 13      | Test implementation on OpenAI MuJoCo Gym         | 2/3/18     | 2/7/18   | 
| 14      | Test implementation on Bioinformatics Data       | 2/7/18     | 2/11/18  | 
| 15      | Test implementation on Crime Rate Data           | 2/11/18    | 2/15/18  | 
| 16      | Design Visual Aids for Presentation                                       | 2/15/18    | 2/22/18  | 
| 17      | Write Paper                                                               | 2/22/18    | 3/1/18   | 

## Effort Matrix <a name="Effort"></a>

![Effort Graph](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/morl_effort_graph.png)

## Final Presentation <a name="Slideshow"></a>

[MORL Presentation](https://github.com/DeepwaterDiscord/morl/blob/master/essays/MORL%20Final%20Presentation.pdf)

## Final Poster <a name="Poster"></a>

[Final Poster](https://github.com/DeepwaterDiscord/morl/blob/master/essays/MORL%20Poster.pdf)

## Initial Self-Assessment Essays <a name="InitialSelfAssessments"></a>

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Initial%20Assessment%20-%20Greer.pdf)

## Final Self-Assessment Essays <a name="FinalSelfAssessments"></a>

[Greer](https://github.com/DeepwaterDiscord/morl/blob/master/essays/Final%20Assessment%20-%20Greer.pdf)

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
