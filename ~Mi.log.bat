:: ������־������
:: �����ļ�������Mihomo Party��Ŀ¼�У�������ݷ�ʽ���ڱ��������ĵط������к��Զ���\data\logs�ļ����µ�����log�ļ���
:: ʹ��Notepad4�򿪣�Ctrl+End����ĩ�У���־����д��ʱ�������ת��
@echo off
set "folder_path=%~dp0data\logs"

for /f "delims=" %%i in ('dir /b /a-d /o-d "%folder_path%\*.log"') do (
    set "latest_log=%%i"
    goto :found
)

:found

powershell -Command "Start-Process notepad.exe '%folder_path%\%latest_log%'"

:end
