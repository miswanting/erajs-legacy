@echo off
cd /d %~dp0
cd ..
mklink /d erajs\erajs\front ..\..\erajs-web\dist
pause