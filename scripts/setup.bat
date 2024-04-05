@echo off

SET venv.activate=%~dp0..\.venv\Scripts\activate.bat
SET venv.deactivate=%~dp0..\.venv\Scripts\deactivate.bat
SET inst.base=%~dp0..\requirements\base.txt
SET inst.dev=%~dp0..\requirements\dev.txt

pip install toml
@REM Setup Venv
pip install virtualenv
python -m venv %~dp0..\.venv

@REM Enter & Install Venv
call %venv.activate%
cd %~dp0..

@REM pip install -e .
@REM https://setuptools.pypa.io/en/latest/userguide/development_mode.html#strict-editable-installs
@REM Install as Package in edit mode
pip install -e . --config-settings editable_mode=strict

@REM Dependencies
py -m pip install -r %inst.base%
py -m pip install -r %inst.dev%

call %venv.deactivate%


echo.
echo Finished Setup
echo.