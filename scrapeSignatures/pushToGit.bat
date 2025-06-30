@echo off
cd /d "%~dp0"

for /f "tokens=1-3 delims=/ " %%a in ("%date%") do (
    set mm=%%a
    set dd=%%b
    set yyyy=%%c
)

for /f "tokens=1-2 delims=: " %%a in ("%time%") do (
    set hh=%%a
    set min=%%b
)

if %hh% LSS 10 set hh=0%hh%

set timestamp=%yyyy%-%mm%-%dd%_%hh%-%min%

:: Stage, commit, and push
git add .
git commit -m "Auto update: %timestamp%"
git push origin main
