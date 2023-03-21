@echo off

set PYTHON=".\venv\Scripts\Python.exe"

if exist .\venv\ goto :run

python -m venv .\venv\

%PYTHON% -m pip install -r requirements.txt
%PYTHON% -m pip install git+https://github.com/modelscope/modelscope.git

:run
%PYTHON% modelscope_gradio.py
