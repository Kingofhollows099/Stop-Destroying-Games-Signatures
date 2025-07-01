@echo off
echo "Phase 1 starting"
python3 scrapeSignatures.py
echo Last Run: %date% %time% > lastRun.txt

echo "Phase 2 starting"
call pushToGit.bat