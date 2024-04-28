@echo off

:: Set the installation path
set INSTALL_PATH=C:\Python311

:: Set the Python installer filename
set INSTALLER_FILENAME=python-3.11.7-amd64.exe

:: Install Python
start /wait %INSTALLER_FILENAME% /quiet InstallAllUsers=1 PrependPath=1 TargetDir=%INSTALL_PATH%

:: Display installed Python version
python --version

:: Add Python to system environment variables
setx PATH "%PATH%;%INSTALL_PATH%"
