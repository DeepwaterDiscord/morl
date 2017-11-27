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

[![MORL Presentation](https://img.youtube.com/vi/0MXuCKj4gsQ/0.jpg?)](https://youtu.be/0MXuCKj4gsQ)

## Self-Assessment Essays <a name="SelfAssessments"></a>

**MORL**

Frazier Baker

Computer Science Senior Design

Self-Assessment

**Project Description**

Multi-objective reinforcement learning is a subfield of deep learning, which is currently a
booming field within Computer Science. Multi-objective reinforcement learning is the process
of conditioning a computer program to make decisions based on more than one goal. The
applications of multi-objective reinforcement learning vary widely and include intelligent
robotics, bioinformatics, and data analysis. Our project focuses on improving feature
selection for multi-objective reinforcement learning. For any machine learning algorithm,
data cleaning and feature selection is essential to achieving good results. We plan to use
filter methods and genetic algorithms to improve feature selection for multi-objective
reinforcement learning.

**Classroom Experience**

My experience in the classroom throughout my undergraduate career has played a role in
preparing me for this project. In Intelligent Data Analysis my sophomore year, I learned the
basics of data analysis with focus on clustering, decision trees, support vector machines, and
association rules. In addition, I learned about the importance of feature selection and
knowing my data. I learned that techniques like PCA exist to analyze features give visual
representations of multivariate data. I also participated in a Deep Learning Seminar last year
as part of an independent study. There I was formally and thoroughly introduced to neural
networks and the concept of deep neural networks.

**Work Experience**

My experience in the workplace has done a lot to prepare me for this project. In my work at
Cincinnati Children’s Hospital Medical Center, I have applied various machine learning and
data analysis techniques to real research problems in proteomics and bioinformatics. I also
have experience with big data visualization and have been able to articulate my work at
conferences and in peer-reviewed journal articles. I also have some experience as a Web
Developer at Kinetic Vision. At Kinetic Vision, I learned a lot about best practices in software
engineering and how to design and organize a project.

**Motivation**

I’ve been doing research-oriented projects since I was a senior in high school, so I was
interested in a research-oriented senior design. For a long time I have been interested in
artificial intelligence and machine learning. As I grew and developed in my career as a
Computer Scientist, I saw pertinent applications in a variety of fields, such as bioinformatics
and data analytics. I am especially driven towards machine learning applications in
bioinformatics because of my childhood dream of tackling problems related to autism, a
disorder with which my brother was diagnosed at a young age. When I was discussing project
ideas with my partner and advisor, I was excited to pick up a manageable piece of the puzzle
in furthering deep learning as a field. I see this project as broadening horizons not only for my
own interests, but for all those who have interests like mine. I want to help the deep learning
community make computers learn better so that we can solve bigger problems across many
fields.

**Preliminary Project Design**

As I’ve been discussing with my partner, I think our preliminary goals will include a literature
search for thorough understanding of the topics we will be exploring, namely multiobjective
reinforcement learning, genetic algorithms, and filter methods. Progress towards these goals
has already been made and we expect to start the next phase soon. In the implementation
phase, we will need to compare our changes to some baseline, so implementing a current
method of feature selection and reinforcement learning would be a good first step of
implementation. Our next step would be to attempt to use filter methods for feature
selection, as suggested in the OpenAI request for research
(https://openai.com/requests-for-research/#multiobjective-rl). Simultaneously, we can be
developing genetic algorithms for the same purpose of feature selection, and explore to what
extent these can be used to improve multiobjective reinforcement learning. Towards the end
of this project, we need to exhaustively evaluate these across multiple datasets and show
their practical applications. Finally, I think we should aim to have some user-friendly
graphical tool to perform feature selection using our algorithm or a selection of algorithms
given a user-provided dataset.

<br>

**MORL: Initial Assessment**

Jeremiah Greer

**Introduction**

Reinforcement Learning is one of the primary areas currently being explored in
research related to Machine Learning, Neural Networks, and Deep Learning. Often this
type of learning involves "learning" multiple tasks in order to reach the desired
functionality, and these multiple tasks are generally defined as trying to optimize
multiple objective functions at once. Modern methods for optimizing these
multi-objective functions usually involve taking a linear combination of the reward terms,
basically combining the functions into one via a linear combination. One area that so far
has not been tested in these methods are Filter Methods, which are a method of
optimizing multi-objective functions. We seek to design and test a filter method which
can adequately train a network in Reinforcement Learning. By drawing upon our
previous experience with Data Analytics and Machine Learning, we hope to extend our
own understanding of these areas and contribute to them.

**Experiences**

The experiences I've gained in my curriculum will help to contribute to this project
in many ways. CS 5152, Intelligent Data Analysis, has given me a wide breadth of
knowledge and tools with which I may be able to analyze data, as well as an
introduction into neural networks and machine learning as a whole. This knowledge will
directly benefit me in my dive into Reinforcement Learning and Multi-Objective
Optimization. In addition, CS 7001, an independent study which turned into a Deep
Learning seminar, helped to work as a deep-dive into the areas of neural networks,
allowing me to analyze modern open-source literature on these areas using the Deep
Learning Book. This spurred off my own personal study on Coursera of Machine
Learning and Neural Networks with Andrew Ng and Geoffrey Hinton, respectively. The
knowledge I've gained from these experiences will prove to be invaluable in
understanding future material and work.

My co-op experiences will also help to contribute to this learning. In particular, my
time at the University of Cincinnati as a Student Researcher under Dr. Rozier
contributes immensely to my current ability as a researcher and as a Data Scientist. In
this co-op, I worked extensively in Python, gaining an intuitive grasp on what it's like to
perform data analytics in the language. In addition, it improved my ability to self-educate
and perform research, two areas which will prove to be critical in this project, as a large
part of it is education and research to understand exactly what we need to do. I had
another co-op at Kinetic Vision as a Software Developer, and in this co-op I primarily
developed VR applications using Unity and C#, while also gaining some design skills to
help improve the visual fidelity of my work. This co-op, while not specifically related to
Machine Learning, did give me the skills necessary to bring my work up to an
acceptable level to present to others as well as manage various projects. These two
skills will assist me in my effort to get our project to a presentable state, as well as
improving how we work on the project going forward, both as individuals and as a
group. I don't seek to maintain leadership in the project, but I will be happy to help work
to keep everything organized.

**Motivation and Methodology**

I look forward to this project primarily because I'm excited to get a chance at
becoming familiar with modern Deep Learning concepts, tools, and datasets. I have a
strong interest in machine learning and I believe that it will continue to be a fruitful area
of the future. I'm also excited because this project particularly entails multi-objective
learning, something which encompasses a lot of areas, including teaching robots to
walk like humans. Replicating organic life behavior through simulations and robotics is
immensely interesting to me, and I feel that this will help me to develop a reasonable
understanding of this area as a result. In order to develop this understanding, I must first
become fairly acquainted with these areas for the project. Doing so will help to prepare
me for the actual project and enable me to structure it in such a way that is
understandable to others and hopefully successful.

In researching the aforementioned areas, we hope to better understand the
current state of research in these topics. We plan to accomplish this by discovering
baseline tutorials for these concepts to gain a familiarity with the vocabulary and
concepts, then read the current literature on these areas to get an idea of what the most
current practices are. After getting ourselves up to speed, we will start working with the
tools we'll need to use to gain familiarity with them, then begin discussing and testing
some possible designs for Filter Methods to use and how to best implement them. This
will finally result in the visualization of the training of the dataset and a formalization of
our process and results presented in a poster and potentially a publication. The project
will be completed once we've achieved a consistent, stable result with which we can use
as a solid test result. We will evaluate our results by comparing them with current
modern methods utilizing different means of multi-objective optimization on the same
dataset.

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
