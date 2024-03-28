@echo off
pyinstaller ebula.spec
copy .\dist\ebula.exe .