@echo off
rem BUILD
cd %~dp0\..
pyinstaller %~dp0\..\src\ebula.py -w -i %~dp0\..\src\icon.ico --noconfirm --onefile
copy %~dp0\..\dist\ebula.exe %~dp0\..\ebula.exe
cd %~dp0