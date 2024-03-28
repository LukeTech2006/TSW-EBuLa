@echo off
pyinstaller ebula.py -w -i icon.ico --noconfirm --onefile
copy .\dist\ebula.exe .