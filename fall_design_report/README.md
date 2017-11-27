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

| Task Id | Task Description                                                          | Start Date | End Date | 
|---------|---------------------------------------------------------------------------|------------|----------| 
| 1       | Research potential Filter Methods for use in reinforcement learning       | 12/1/17    | 12/5/17  | 
| 2       | Find appropriate Python libraries for use with filter methods             | 12/5/17    | 12/6/17  | 
| 3       | Research best practices for reinforcement learning in Tensor Flow         | 12/6/17    | 12/10/17 | 
| 4       | Experiment with tensorflow, RL, and OpenAI Gym in Python                  | 12/10/17   | 12/17/17 | 
| 5       | Research best practices for using Genetic Algorithms in feature selection | 12/17/17   | 12/18/17 | 
| 6       | Locate fast GA Python libraries for use in feature selection              | 12/18/17   | 12/19/17 | 
| 7       | Develop feature selection algorithm using filter methods                  | 1/2/18     | 1/9/18   | 
| 8       | Design efficient RL system in Tensorflow using current best-practices     | 1/9/18     | 1/16/18  | 
| 9       | Combine filter methods and GA in feature selection                        | 1/16/18    | 1/23/18  | 
| 10      | Integrate feature selection workflow into RL Tensorflow system            | 1/23/18    | 1/25/18  | 
| 11      | Develop CLI Tool for Feature Selection                                    | 1/25/18    | 1/27/18  | 
| 12      | Develop UI Tool for Feature Selection                                     | 1/27/18    | 2/3/18   | 
| 13      | Test feature selection and RL implementation on OpenAI MuJoCo Gym         | 2/3/18     | 2/7/18   | 
| 14      | Test feature selection and RL implementation on Bioinformatics Data       | 2/7/18     | 2/11/18  | 
| 15      | Test feature selection and RL implementation on Crime Rate Data           | 2/11/18    | 2/15/18  | 
| 16      | Design Visual Aids for Presentation                                       | 2/15/18    | 2/22/18  | 
| 17      | Write Paper                                                               | 2/22/18    | 3/1/18   | 

## Effort Matrix <a name="Effort"></a>

![Effort Graph](https://github.com/DeepwaterDiscord/morl/blob/master/design_diagrams/morl_effort_graph.png)

## ABET Constraints Essays <a name="ABET"></a>

#### Economic Constraints

MORL has financial limitations that are often inherent to any openly publishable research. Given
our lack of funding and our desire to produce results which are replicable by anyone, we are
reliant on freely available tools such as Tensorflow, OpenAI Gym, and Python. While using free
tools limits some of our performance capabilities, the vast support and availability of these tools
improves its accessibility to others, and we feel this benefit outweighs the loss of limiting
ourselves to freely available tools. This also enables us to be unrestricted by any potential bias
of funding from other sources, as we will be receiving no monetary contributions. In addition,
this frees us from any restrictions in regards to use of physical resources such as computers at
UC. So long as a computer can install tensorflow and use Python and OpenAI Gym, our work
should be entirely usable from this computer, thus improving universal accessibility and
replicability. Thinking beyond constraints and more towards contributions, this tool could be
used to support economic development, particularly in any economic area which involves
multi-objective problems, and given the complexity of many economic issues, many of these
issues could be modeled as multi-objective problems and therefore be used as input into the
MORL system to find their solutions.


#### Professional Constraints

Multi-Objective Reinforcement Learning is a growing subset of Deep Learning which seeks to
use Reinforcement Learning to solve complex problems in which one wishes to solve for
multiple objectives. Because of this, our contribution to this area will provide us with an
improved understanding into this area and providing us with hands-on experience in the areas
of Deep Learning and Machine Learning. The members of this group have all worked on
Machine Learning topics to some degree, from Clustering, SVMs, and Decision Trees, to Neural
Networks, a Deep Learning Seminar, Genetic Algorithms, etc. By working with Reinforcement
Learning, we seek to extend our knowledge to include a greater domain of Machine Learning
topics and how we can use the tools within it to solve problems. This project will require us to
apply all of our previous Machine Learning knowledge, improve it, and widen it. As such, this
also means that the project will be inherently constrained by our own understanding of this area,
so it is crucial that we ensure it is as clear as possible. This in turn will improve our knowledge
and expertise as Computer Scientists and Data Analysts, supporting us in our future work and
careers. In our effort to publish our work to the Machine Learning community, we will also
improve our standing as researches in the field.


#### Social Constraints

Our project can be used by nonprofit and for profit organizations alike to analyze data and train
computers to solve problems and make decisions. This can be especially useful to society by
propelling forward fields that are rich in data, but have high-complexity, multi-objective
problems. For instance, the upcoming field of personalized medicine often wants to provide
good information to patients without incurring excessive medical expenses. Medical
professionals and researchers could use our tool to advance the current state of personalized
medicine. It could also be used by bioinformaticians outside of the scope of personalized
medicine, and we hope to present an example of such use in our testing. Additionally, there has
been huge interest in deep learning from the automotive and robotics industries. Our
optimizations of feature selection for multi-objective reinforcement learning could aid in the
development of self-driving cars, autonomous robotic assistants, and other innovative
technologies. While our tool will primarily improve the quality of research, the research that
uses our tool could have a major impact on quality of life for everyone.


#### Diversity and Cultural Constraints
With the wide-reaching impact that our tool could have, it is important to consider that people
from diverse cultures and lifestyles may want to use our tool and incorporate that into its design.
However, as two white males from Appalachia, it can certainly be a challenge to incorporate
diversity into our tool. Initially, we will only have one locale, American English for our UI and CLI
tool; however, with our collective knowledge of Spanish and Mandarin Chinese, we may later
seek to expand this and incorporate other locales. With the amount of artificial intelligence
research currently being done in China by Baidu and other companies (Daugherty, Paul, 2017,
https://www.weforum.org/agenda/2017/06/how-china-became-ai-leader/), there could be a huge
benefit to the global research community to translating our tool into a Mandarin Chinese
distribution. Designing our tool to be intuitive and easy to translate into other locales will be an
important step in our initial design.

## Slideshow <a name="Slideshow"></a>

## Self-Assessment Essays <a name="SelfAssessments"></a>

## Professional Biographies <a name="Biographies"></a>

### Professional Biography for Frazier Baker

Uploaded November 27, 2017. For a more up-to-date biography, click here: https://github.com/DeepwaterDiscord/about-us/blob/master/frazierbaker.md

#### Work

Frazier Baker has had the opportunity to work at a few companies through the cooperative education program at the University of Cincinnati.  Here's a basic rundown of his work history.

##### Center for Autoimmune Genomics and Etiology (CAGE), Cincinnati Children's Hospital Medical Center

Frazier worked as a student researcher under Dr. Alexey Porollo, PhD. on bioinformatics projects related to proteomics, protein coevolution, fungi, and autoimmune disorders.  Notable accomplishments include <a href="http://polyview.cchmc.org/coeviz_doc.html">CoeViz</a> and these publications:

- <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4782369/pdf/12859_2016_Article_975.pdf">Baker FN, Porollo A. A.
CoeViz: a web-based tool for coevolution analysis of protein residues. BMC Bioinformatics. 2016; 17:119.</a>
- <a href="">Baker FN, Cushion MT, Porollo A. A Quantitative Model to Estimate Drug Resistance in Pathogens. Journal of Fungi. 2016; 2(4):30.</a>

##### Kinetic Vision

Frazier worked as a Software Development Co-op at Kinetic Vision in Evendale, Ohio for two semesters.  He used Ruby on Rails, ES 2015, SCSS, and a variety of JavaScript libraries to develop web applications for a variety of clients and purposes.  In addition, he helped design databases, cloud-based solutions using AWS, and web APIs using the JSONAPI format.

##### Ohio University Zanesville

Frazier worked on computational physics research with Dr. Gabriela Popa.  He developed a pipeline of Python scripts to do web-scraping and mathematical analysis using matplotlib.

#### Education

##### University of Cincinnati, *2014 - 2019*
B.S. in Computer Science, M.S. Computer Science
ACCEND Student, Honors Student
Will Graduate in May 2019

##### Ohio University Zanesville, *2012 - 2014*
Post Secondary Enrollment Options Program Student, Non-matriculated

#### Personal

Frazier has a number of hobbies which include, but are not limited to:

- Playing Piano
- Playing Euphonium
- Writing Poetry
- Teaching Sunday School
- Hiking

#### Project Interests

Frazier Baker is interested in working on projects that involve web design and development, database design and development, cloud or distributed computing, machine learning, augmented reality, and bioinformatics.

#### How To Contact

I welcome side-projects, feedback on existing projects, and opportunities for collaboration.  If you would like to contact me, send an email to me@frazierbaker.com or bakerfn@mail.uc.edu.


### Professional Biography for *Jeremiah Greer*

Uploaded November 27, 2017. For a more up-to-date biography, click here: https://github.com/DeepwaterDiscord/about-us/blob/master/jeremiahgreer.md

#### Contact Info
 - School Email: greerji@mail.uc.edu
 - Professional Email: JeremiahGreer013@gmail.com
 - References available upon request
#### Work Experience
###### Kinetic Vision: Aug-Dec 2016, May-Aug 2017
  - Developed VR applications for clients using Unity and C#
  - Worked with advanced VR and AR hardware such as the Vive and Hololens
  - Gained experience working in an AGILE-like workflow
  - Collaborated with the Visualization department on applications, getting an in-depth perspective on various design decisions and processes
  - Used Blender and Photoshop to assist in asset creation
  - Manager: Kyle Hartshorn
###### University of Cincinnati, Research: Jan-Jul 2015-16
  - Developed platform for World Bank to assist in detecting fraud using Python and Neo4j
  - Created a RESTful API for the system for extensible programatic use
  - Built a small web application using basic javascript and Django
  - Gained a base understanding of various clustering and data-processing techniques
  - Generated a VM for use by the client and created a Docker instance
  - Manager/PI: Dr. Eric Rozier

#### Skills
  - Experienced with: Unity, C#, Python, HTC Vive, Oculus Rift, Hololens, Linux, Neo4j
  - Worked with: Matlab, Octave, Django, Docker, Javascript, PSQL, C, C++, PHP
#### Project
  - Looking for something related to areas of machine learning, computer vision, and/or data analytics.
  - Would also be interested in developing an AR or VR application


## Budget <a name="Budget"></a>

There have been no expenses to date and we do not expect any.

## Bibliography <a name="Bibliography"></a>

## Appendix <a name="Appendix"></a>
