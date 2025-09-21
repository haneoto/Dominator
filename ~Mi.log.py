import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(current_dir, "data", "logs")

log_files = [f for f in os.listdir(folder_path) if f.startswith("core") and f.endswith(".log")]
log_files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)
latest_log = log_files[0] if log_files else None

if latest_log:
    log_file_path = os.path.join(folder_path, latest_log)
    subprocess.run(["notepad.exe", log_file_path])
else:
    print("没有找到日志文件。")
