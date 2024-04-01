@echo off

SET venv.activate=%~dp0..\.venv\Scripts\activate.bat
SET venv.deactivate=%~dp0..\.venv\Scripts\deactivate.bat

@REM Setup Venv
pip install virtualenv
python -m venv %~dp0..\.venv

@REM Enter & Install Venv
call %venv.activate%
py -m pip install -r %~dp0requirements.txt
call %venv.deactivate%