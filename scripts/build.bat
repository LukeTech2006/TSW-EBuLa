@echo off
rem BUILD
pyinstaller %~dp0\..\src\ebula.py -w -i %~dp0\..\src\icon.ico --noconfirm --onefile
copy %~dp0\..\dist\ebula.exe %~dp0\..\ebula.exe