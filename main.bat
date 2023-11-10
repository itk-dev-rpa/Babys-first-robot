cd %~dp0

python -m venv .venv
call .venv\Scripts\activate
pip install "C:\Repos\OpenOrchestrator"

python process.py %1 %2 %3 %4