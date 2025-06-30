@echo off
python3 scrapeSignatures.py
echo Last Run: %date% %time% > lastRun.txt
call pushToGit.bat
powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -NonInteractive -File "%~dp0Refresh signatures.ps1"
