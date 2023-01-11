import subprocess
import os
import json

class HTML_CONVERTER:
    def convert_text_to_html(self, filepath):
        try:
            tika_path = get_relative_path() + "/packages/tika-app-1.20.jar"
            cmd = 'java -jar ' + tika_path  + ' -h ' + filepath
            html_text = subprocess.check_output(cmd, shell=True).decode('windows-1252')
            print("[CONVERT TEXT TO HTML] Done.")
            return html_text
        except Exception:
            return None


def get_relative_path():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir.replace('\\', '/')