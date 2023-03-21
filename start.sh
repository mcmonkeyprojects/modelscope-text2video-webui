#!/bin/bash

if [[ ! -d ./venv/ ]]
then
    source install.sh
fi

source ./venv/bin/activate

python3 modelscope_gradio.py
