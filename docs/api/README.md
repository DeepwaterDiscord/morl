# MORL API Reference

## Table of Contents
 - [morl.learning](#Learning)
   - [morl.learning.sequential](#LearningSequential)
     - [morl.learning.sequential.ddpg](#LearningSequentialDDPG)
     - [morl.learning.sequential.dqn](#LearningSequentialDQN)
     - [morl.learning.sequential.multiddpg](#LearningSequentialMultiDDPG)
     - [morl.learning.sequential.multilearn](#LearningSequentialMultilearn)
     - [morl.learning.sequential.qlearn](#LearningSequentialQlearn)
   - [morl.learning.parallel](#LearningParallel)
     - [morl.learning.parallel.multilearn](#LearningParallelMultilearn)
 - [morl.run](#Run)
   - [morl.run.MORLEnviornment](#RunMORLEnvironment)
 - [morl.examples](#Examples)
   - [morl.examples.ddpg_mujoco](#ExamplesDDPGMujoco)
   - [morl.examples.ddpg_pendulum](#ExamplesDDPGPendulum)
   - [morl.examples.dqn_mountaincar](#ExamplesDQNMountaincar)
   - [morl.examples.frozenlake_config](#ExamplesFrozenlakeConfig)
   - [morl.examples.frozenlake](#ExamplesFrozenlake)
   - [morl.examples.mountaincar](#ExamplesMountaincar)

## Reference

### <a name="Learning">`morl.learning`</a> | Learning

#### <a name="LearningSequential">`morl.learning.sequential`</a> | Sequential

##### <a name="LearningSequentialDDPG">`morl.learning.sequential.ddpg`</a>
This file provides all of the classes and functions needed to implement a Deep Deterministic Policy Gradient learner based on our Learner class setup and Patrick Emami's implementation of the algorithm described in [Lillicrap et al.](https://arxiv.org/pdf/1509.02971v2.pdf).  Deep Deterministic Policy Gradients are useful for reinforcement learning problems when the action space and the state space are continuous (as opposed to discrete).  The most notable class in this file is `DDPG_Learner`.
```DDPG_Learner(actions, gamma, reward_function, action_dim, action_bound, state_dim, default_file_name, save_dir="./", minibatch_size=64, graph=tf.get_default_graph(), save=True, load=True, save_frequency=100)```

| Parameter         | Type       | Description                                            |
|-------------------|------------|--------------------------------------------------------|
| actions           | `gym.Box`  | Action space from OpenAI Gym                           |
| gamma             | `float`    | Discount weight for connected utilities                |
| reward_function   | `function` | Dynamically pulls reward from environment step results |
| action_dim        | `np.shape` | Dimensions of the action space                         |
| action_bound      | `np.array` | Boundaries of each vector of the action space          |
| state_dim         | `np.shape` | Dimensions of the state space                          |
| default_file_name | `string`   | Prefix for progress filenames.                         |
| save_dir          | `string`   | Directory to which to save progress.                   |
| minibatch_size    | `int`      | Size for mini batch optimization                       |
| graph             | `tf.Graph` | The underlying tensorfow dataflow computation graph    |
| save              | `bool`     | Whether or not to save progress to disk                |
| load              | `bool`     | Whether or not to attempt to load from disk            |
| save_frequency    | `int`      | Number of epochs to wait between saves                 |

You can use a `DDPG_Learner` in the same way you would use a typical `QLearner`, except the `DDPG_Learner` can handle continuous state and action spaces.

##### <a name="LearningSequentialDQN">`morl.learning.sequential.dqn`</a>
This file provides all of the classes and functions needed to implement a Deep Q Network learner based on our Learner class setup and Victor Mayoral Vilches' implementation of the algorithm described in [Mnih et al.](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf).  Deep Q Networks are useful for reinforcement learning problems when the state space are continuous but the action space is discrete.  The most notable class in this file is `DQN_Learner`.

```DQN_Learner(actions, epsilon, alpha, gamma, reward_function, deepQNetwork)```

| Parameter         | Type       | Description                                            |
|-------------------|------------|--------------------------------------------------------|
| actions           | `list`     | Discrete actions represented as unique objects         |
| epsilon           | `float`    | Exploration Rate. (Percentage of iterations in which the action will be selected off-policy) |
| reward_function   | `function` | Dynamically pulls reward from environment step results |
| learn_start       | `int`      | Learning Delay.  Number of samples for which to wait before learning. |
| memory_size       | `int`      | Maximum number of samples to keep                      |
| network_structure | `list`     | Dimensions of the layers for the underlying deep neural network. |

You can use a `DQN_Learner` in the same way you would use a typical `QLearner`, except the `DQN_Learner` can handle continuous state  spaces.

##### <a name="LearningSequentialMultiDDPG">`morl.learning.sequential.multiddpg`</a>
The `MultiDDPG` class is an adaptation of the `MultiLearn` class for continuous action and state spaces.  It uses `DDPG_Learner` by default as its single learner function instead of `QLearner`.

```MultiDDPG(actions, gamma, reward_functions, action_dim, action_bound, state_dim, minibatch_size=64, include_sum=False)```

| Parameter         | Type       | Description                                            |
|-------------------|------------|--------------------------------------------------------|
| actions           | `gym.Box`     | Continuous action space         |
| reward_functions   | `list(function)` | List of functions to dynamically pull rewards from environment step results |
| action_dim        | `np.shape` | Dimensions of the action space                         |
| action_bound      | `np.array` | Boundaries of each vector of the action space          |
| state_dim         | `np.shape` | Dimensions of the state space                          |
| minibatch_size    | `int`      | Size of mini-batch for mini-batch optimization         |
| include_sum       | `bool`     | Whether or not to include the sum of the rewards as a separate reward function |

`MultiDDPG` behaves like `MultiLearn` except that it can take continuous input and the multipolicy generation chooses the best from each reward function as a simple approximation of the best possible actions.  We use this approximation due to the complexity of exploring a continuous state-action space.

##### <a name="LearningSequentialMultilearn">`morl.learning.sequential.multilearn`</a>
The `MultiLearn` class is the heart of this project.  This class uses multiple learner classes to compute separate utilities for each of the supplied reward functions.  It then uses a Pareto filter to construct a multipolicy, that is, it constructs a policy containing one or more actions for each state that are not dominated by any other action on all reward functions' utilities.  From this multipolicy, actions can be chosen from a variety of manners, with the default being random choice.

```MultiLearn(actions, epsilon, alpha, gamma, reward_functions, default_actions=[], klass=QLearn)```

| Parameter         | Type       | Description                                            |
|-------------------|------------|--------------------------------------------------------|
| actions           | `dict(state: action)`  | Discrete action space         |
| epsilon           | `float`                | Exploration Rate. (Percentage of iterations in which the action will be selected off-policy) |
| reward_functions  | `list(function)`       | List of functions to dynamically pull rewards from environment step results |
| alpha             | `float`                | Learning rate                         |
| gamma             | `float`                | Discount weight for connected utilities                |
| default_actions   | `list(actions)`        | List of actions available from any state.  Useful if all states share the same action space. |
| klass             | `type`                 | Single learner class |


##### <a name="LearningSequentialQlearn">`morl.learning.sequential.qlearn`</a>

`QLearn` is a traditional reinforcement learning algorithm implementation that serves as the default single learner for `MultiLearn`.  

```MultiLearn(actions, epsilon, alpha, gamma, reward_function, default_actions=[])```

| Parameter         | Type       | Description                                            |
|-------------------|------------|--------------------------------------------------------|
| actions           | `dict(state: action)`  | Discrete action space         |
| epsilon           | `float`                | Exploration Rate. (Percentage of iterations in which the action will be selected off-policy) |
| reward_function   | `function`             | Functions to dynamically pull rewards from environment step results |
| alpha             | `float`                | Learning rate                         |
| gamma             | `float`                | Discount weight for connected utilities                |
| default_actions   | `list(actions)`        | List of actions available from any state.  Useful if all states share the same action space. |
| klass             | `type`                 | Single learner class |

#### <a name="LearningParallel">`morl.learning.parallel`</a> | Parallel

**Coming Soon**

### <a name="Run">`morl.run`</a> | Configuration Class

MORL was built to be extensible; we want you to be able to use our software and our API.  To simplify that process, we have provided a simple format for you to configure your own reinforcement learning environment and run it using the MORL CLI or MORL Web Server.

#### <a name="RunMORLEnvironment">`morl.run.MORLEnvironment`</a> | Config
`MORLEnvironment` is the configuration class which is capable of acting as a wrapper to OpenAI Gym Environments, while also being able to abstract away the complex instantiation of the learners. It also enables access to various learning hyperparameters and contains the universal run() method which abstracts the learning and printing process of the model to allow one to compare different models. It also contains plotting functionality to provide visual clarity to the learning process over the number of iterations.

```MORLEnvironment(learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9, doprint=True)```

| Parameter         | Type         | Description                                                                 |
|-------------------|--------------|-----------------------------------------------------------------------------|
| learner_klass     | `class type` | Type of learner-class you wish to use, such as `MultiLearn`, `QLearn`, etc. |
| n_learners        | `int`        | Number of learners (used in Multilearners, others default to 1)             |
| epsilon_start     | `float`      | Initial value of exploration rate                                           |
| alpha_start       | `float`      | Initial value of Learning rate                                              |
| gamma_start       | `float`      | Initial value of discount weight for connected utilities                    |
| doprint           | `bool`       | Print reward progress to stdout                                             |

### <a name="Examples">`morl.examples`</a> | Examples

MORL comes with numerous examples which we used in testing.  It also comes with some sample configurations for you to use as you model your own MORL configurations.

#### <a name="ExamplesDDPGMujoco">`morl.examples.ddpg_mujoco`</a> | DDPG Mujoco
This example shows how to use our DDPG version of Multilearn in a sample environment, and also showcases the ability of our system to work in more complex environments, such as the OpenAI Mujoco Humanoid environment.

#### <a name="ExamplesDDPGPendulum">`morl.examples.ddpg_pendulum`</a> | DDPG Pendulum
This example shows how to use a single-learner version of a DDPG (i.e. a normal DDPG) in a sample environment OpenAI Pendulum environment.

#### <a name="ExamplesDQNMountaincar">`morl.examples.dqn_mountaincar`</a> | DQN Mountaincar
This example shows how to use a Deep Q-Network in the OpenAI Mountaincar sample environment.

#### <a name="ExamplesFrozenlakeConfig">`morl.examples.frozenlake_config`</a> | FrozenLake Config
This example shows how to create your own configuration by wrapping the OpenAI Environment within. Configs help to abstract away the training and iteration code for reinforcement learning, letting you focus on the model and the environment.

#### <a name="ExamplesFrozenlake">`morl.examples.frozenlake`</a> | FrozenLake
This example shows how to our use default tabular Q-Learning with a basic environment from OpenAI, the FrozenLake environment. This was used to generate reward-over-time graphs to compare Multilearning with Q-Learning.

#### <a name="ExamplesMountaincar">`morl.examples.mountaincar`</a> | Mountaincar
This example shows how to our use default tabular Q-Learning with an environment with a continuous state-space from OpenAI, the Mountaincar environment. For tabular Q-Learning, this involves discretizing the state-space, but for larger spaces this becomes inpractical, which is why DQN's and DDPG Networks are used instead.

## Index
 - [morl.examples](#Examples)
   - [morl.examples.ddpg_mujoco](#ExamplesDDPGMujoco)
   - [morl.examples.ddpg_pendulum](#ExamplesDDPGPendulum)
   - [morl.examples.dqn_mountaincar](#ExamplesDQNMountaincar)
   - [morl.examples.frozenlake_config](#ExamplesFrozenlakeConfig)
   - [morl.examples.frozenlake](#ExamplesFrozenlake)
   - [morl.examples.mountaincar](#ExamplesMountaincar)
 - [morl.learning](#Learning)
   - [morl.learning.sequential](#LearningSequential)
     - [morl.learning.sequential.ddpg](#LearningSequentialDDPG)
     - [morl.learning.sequential.dqn](#LearningSequentialDQN)
     - [morl.learning.sequential.multiddpg](#LearningSequentialMultiDDPG)
     - [morl.learning.sequential.multilearn](#LearningSequentialMultilearn)
     - [morl.learning.sequential.qlearn](#LearningSequentialQlearn)
   - [morl.learning.parallel](#LearningParallel)
     - [morl.learning.parallel.multilearn](#LearningParallelMultilearn)
 - [morl.run](#Run)
   - [morl.run.MORLEnviornment](#RunMORLEnvironment)
