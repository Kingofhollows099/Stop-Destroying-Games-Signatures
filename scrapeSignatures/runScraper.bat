@echo off
echo "Phase 1 starting"
python3 scrapeSignatures.py
echo Last Run: %date% %time% > lastRun.txt
echo "Phase 2 starting"
call pushToGit.bat
echo "Phase 3 starting"
powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -NonInteractive -File "%~dp0Refresh signatures.ps1"
echo "Done"