:: 最新日志启动器
:: 将此文件放置于Mihomo Party主目录中，创建快捷方式放在便于启动的地方，运行后自动打开\data\logs文件夹下的最新log文件。
:: 使用Notepad4打开，Ctrl+End跳至末行，日志有新写入时会继续跳转。
@echo off
set "folder_path=%~dp0data\logs"

for /f "delims=" %%i in ('dir /b /a-d /o-d "%folder_path%\*.log"') do (
    set "latest_log=%%i"
    goto :found
)

:found

powershell -Command "Start-Process notepad.exe '%folder_path%\%latest_log%'"

:end
