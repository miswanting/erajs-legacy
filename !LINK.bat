@echo off
cd /d %~dp0
cd ..
mklink /d erajs\erajs\front era-js-frontend\dist
pause