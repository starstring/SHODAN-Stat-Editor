@echo off
setlocal
set "VSROOT=C:\Program Files (x86)\Microsoft Visual Studio\18\BuildTools"
echo [luajit] using %VSROOT%
call "%VSROOT%\VC\Auxiliary\Build\vcvars64.bat" >nul
if errorlevel 1 echo [luajit] vcvars failed & exit /b 1
where cl >nul || (echo [luajit] cl not on PATH & exit /b 1)
cd /d "%~dp0third_party\LuaJIT\src"
if errorlevel 1 (echo [luajit] no LuaJIT source & exit /b 1)
set NoDefaultCurrentDirectoryInExePath=
set "PATH=.;%PATH%"
call msvcbuild.bat
if errorlevel 1 (echo [luajit] msvcbuild failed & exit /b 1)
echo [luajit] done
