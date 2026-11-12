@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
  set "HOPON_PYTHON=py -3"
) else (
  where python >nul 2>&1
  if errorlevel 1 (
    echo Python 3 is required. Install Python 3 and run this file again.
    pause
    exit /b 1
  )
  set "HOPON_PYTHON=python"
)
start "" powershell -NoProfile -Command "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:8787'"
%HOPON_PYTHON% hopon_app.py
endlocal
