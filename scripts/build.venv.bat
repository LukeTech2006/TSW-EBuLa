@echo off

@REM echo %cd%
@REM echo %~dp0

SET venv.activate=%~dp0..\virtual-environment\Scripts\activate.bat
SET venv.deactivate=%~dp0..\virtual-environment\Scripts\deactivate.bat
SET build=%~dp0build.bat

@REM echo %venv.activate%
@REM echo %build%
@REM echo %venv.deactivate%

rem ENTER VENV
call %venv.activate%

call %build%

rem EXIT VENV
call %venv.deactivate%