import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_script()

    def restart_script(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} changed, restarting...")
            self.restart_script()

if __name__ == "__main__":
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../", "main.py"))
    script_to_watch = script_path
    event_handler = ReloadHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
