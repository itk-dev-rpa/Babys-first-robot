import subprocess
import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

subprocess.run("python -m venv .venv", check=True)
subprocess.run(r".venv\Scripts\pip install OpenOrchestrator", check=True)

command_args = [r".venv\Scripts\python", "process.py"] + sys.argv[1:]

subprocess.run(command_args, check=True)
