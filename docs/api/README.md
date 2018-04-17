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
   - [morl.run.MORLEnviornment](#RunMORLEnviornment)
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
| gamma             | `float`    | Decay weight for connected utilities                   |
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

##### <a name="LearningSequentialDDPG">`morl.learning.sequential.dqn`</a>
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



##### <a name="LearningSequentialQlearn">`morl.learning.sequential.qlearn`</a>


#### <a name="LearningParallel">`morl.learning.parallel`</a> | Parallel


### <a name="Run">`morl.run`</a> | Configuration Class

### <a name="Examples">`morl.examples`</a> | Examples

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
   - [morl.run.MORLEnviornment](#RunMORLEnviornment)
