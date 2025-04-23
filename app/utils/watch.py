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
        print(f"🔁 Restarting: {self.script}")
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        observer.schedule(event_handler, path="app", recursive=True)

        if event.is_directory:
            return

        if event.src_path.endswith(".py") or event.src_path.endswith(".qss"):
            print(f"📁 File changed: {event.src_path}")
            self.restart_script()

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    script_path = os.path.join(base_dir, "main.py")

    event_handler = ReloadHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, path=base_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
