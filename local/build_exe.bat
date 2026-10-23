@echo off
rem Builds "SHODAN Stat Editor Offline.exe" and shodan_hash.dll from offline\launcher, with the MSVC
rem Build Tools that are installed here, and LuaJIT at local\third_party\LuaJIT (same commit as the CI).
rem The outputs land in offline\launcher and offline\runtime as upstream's CI puts them, so upstream's
rem offline\package.py can pack them unchanged.
setlocal
set "VSROOT=C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools"
call "%VSROOT%\VC\Auxiliary\Build\vcvars64.bat" >nul
if errorlevel 1 (echo [exe] vcvars failed & exit /b 1)
where cl >nul || (echo [exe] cl not on PATH & exit /b 1)

set "LJ=%~dp0third_party\LuaJIT\src"
if not exist "%LJ%\lua51.lib" (echo [exe] no lua51.lib in %LJ% & exit /b 1)
if not exist "%LJ%\lua51.dll" (echo [exe] no lua51.dll in %LJ% & exit /b 1)
copy /y "%LJ%\lua51.dll" "%~dp0..\offline\runtime\" >nul || exit /b 1

cd /d "%~dp0..\offline\launcher" || exit /b 1
rc /nologo /fo launcher.res launcher.rc || (echo [exe] rc failed & exit /b 1)
cl /nologo /O2 /W3 /MD /I"%LJ%" launcher.c /Fo:launcher.obj /link /SUBSYSTEM:WINDOWS "%LJ%\lua51.lib" user32.lib launcher.res /OUT:"SHODAN Stat Editor Offline.exe"
if errorlevel 1 (echo [exe] launcher failed & exit /b 1)
cl /nologo /O2 /W3 /MT /LD hashsolve.c fetch.c update.c /link winhttp.lib user32.lib /OUT:shodan_hash.dll
if errorlevel 1 (echo [exe] shodan_hash.dll failed & exit /b 1)
echo [exe] done
