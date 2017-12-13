#!/bin/bash
# Provisions environment for MORL

$PROJ_DIR="../../bin"

rm -rf $PROJ_DIR 2>/dev/null
mkdir $PROJ_DIR
cd $PROJ_DIR

pip install tensorflow

git clone https://github.com/openai/gym
cd gym
pip install -e .
