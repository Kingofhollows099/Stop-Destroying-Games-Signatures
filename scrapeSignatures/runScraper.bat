@echo off
python3 scrapeSignatures.py
echo Last Run: %date% %time% > lastRun.txt
call pushToGit.bat