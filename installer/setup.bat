@echo off
cd PyInstaller-2.1
pyinstaller.py -F ..\..\imageCodePractice.py --workpath="..\..\tmp" --distpath="..\..\dist" --specpath="..\..\tmp"


echo input any key to quit
set /p input=