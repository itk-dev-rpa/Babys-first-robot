cd %~dp0

@REM python -m venv .venv
@REM call .venv\Scripts\activate
@REM pip install "C:\Repos\OpenOrchestrator"

echo %1
echo %2
echo %3
echo %4

python process.py %1 %2 %3 %4