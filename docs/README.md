# MORL Documentation
## Installation
To install the project on your system, download and extract the repository onto your computer, and then change directory to the base project directory (containing setup.py) and run the following command:

```
sudo pip install -e .
```

This should install all necessary dependencies

## Command Line Examples
To use the command line tool, make sure you're in the base directory of the project. The following is the basic command for the repository:
```
python -m morl
```

This will require both a running mode to use, such as the openai gym environments (frozenlake, mountaincar, etc.), as well as a type of learner (qlearn, multilearn).

The following command runs the OpenAI Gym FrozenLake Environment using multilearn:
```
python -m morl frozenlake multilearn
```

This will run the default configuration. To modify configurations or to create your own, refer to the Developer Docs.

## API Documentation
If you want to use MORL on your own environments/datasets, you will probably want to take a look at our [api documentation](./api).

## Graphical User Interface

MORL has a django webserver User Interface that tracks the progress of your MORL Configuration Jobs for you.  More documentation on this will be made available in the future.
