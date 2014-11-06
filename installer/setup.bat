@echo off
cd PyInstaller-2.1
pyinstaller.py --clean -F ..\..\imageCodePractice.py --workpath="..\..\tmp" --distpath="..\..\dist" --specpath="..\..\tmp" -r "..\..\*.bmp"


echo input any key to quit
set /p input=