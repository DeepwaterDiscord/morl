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
This file provides all of the classes and functions needed to implement a Deep Deterministic Policy Gradient learner based on our Learner class setup and Patrick Emami's implementation of the algorithm described in [Lillicrap et al.](https://arxiv.org/pdf/1509.02971v2.pdf).  Deep Deterministic Policy Gradients are useful for reinforcement learning problems when the action space and the state space are continuous (as opposed to discrete).  The most notable class in this file is `DDPGLearner`.
```DDPGLearner(actions, gamma, reward_function, action_dim, action_bound, state_dim, default_file_name, save_dir="./", minibatch_size=64, graph=tf.get_default_graph(), save=True, load=True, save_frequency=100)```
Parameters:
| Parameter         | Type       | Description                                            |
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

##### <a name="LearningSequentialDDPG">`morl.learning.sequential.dqn`</a>

##### <a name="LearningSequentialDDPG">`morl.learning.sequential.multilearn`</a>

##### <a name="LearningSequentialDDPG">`morl.learning.sequential.qlearn`</a>

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
