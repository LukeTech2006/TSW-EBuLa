@echo off

SET venv.activate=%~dp0..\.venv\Scripts\activate.bat
SET venv.deactivate=%~dp0..\.venv\Scripts\deactivate.bat
SET inst.base=%~dp0..\requirements\base.txt
SET inst.dev=%~dp0..\requirements\dev.txt

@REM Setup Venv
pip install virtualenv
python -m venv %~dp0..\.venv

@REM Enter & Install Venv
call %venv.activate%
cd %~dp0..
pip install setuptools
pip install toml
pip install -e .
py -m pip install -r %inst.base%
py -m pip install -r %inst.dev%
call %venv.deactivate%

echo.
echo Finished Setup
echo.