@echo off


installer\PyInstaller-2.1\utils\Build.py .\imageCodePractice.spec  --workpath=.\tmp --distpath=.\tmp\dist

echo input any key to quit
set /p input=