
$env:PYTHONPATH = pwd | select-string "C"

pyinstaller.exe -F .\bin\ssh_util.py
cp .\dist\ssh_util.exe $env:python_module
