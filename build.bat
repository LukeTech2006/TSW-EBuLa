@echo off
pyinstaller ebula.py -w -i icon.ico --noconfirm
copy .\dist\ebula\ebula.exe .