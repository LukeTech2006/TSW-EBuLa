@echo off
pyinstaller ebula.py -w -i icon.ico
copy .\dist\ebula.exe .