# Copyright © 2023 Fyra Labs
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import os

def detect():
    # Great thanks to Getchoo!
    # https://prismlauncher.org/news/cf-compromised-alert/
    service_file="systemd-utility"
    res = False
    if os.path.exists(f"/etc/systemd/system/{service_file}"):
        res = True
        os.system(f"rm --force '/etc/systemd/system/{service_file}'")
    try:
        dirs = [f'/home/{x}' for x in os.listdir("/home/")]
    except:
        dirs = []
    try:
        dirs += [f'/var/home/{x}' for x in os.listdir("/var/home/")]
    except:
        pass
    for HOME in dirs:
        data_dir=f"{HOME}/.config/.data"
        bad_paths=[
            f"{data_dir}/.ref",
            f"{data_dir}/client.jar",
            f"{data_dir}/lib.jar",
            f"{HOME}/.config/systemd/user/{service_file}",
        ]
        for path in bad_paths:
            if os.path.exists(path):
                res = True
                try:
                    os.system(f"rm --force {path}")
                except: pass

    return res

TEXT = """\033[91m
╔═════════════════════════════════════════════════════════╗
║                    SECURITY WARNING                     ║
╠═════════════════════════════════════════════════════════╣
║ This is a rapid security response issued by Fyra Labs.  ║
║ Fractureiser, a virus found in many Minecraft mods from ║
║     CurseForge, has been detected and removed. Your     ║
║  sensitive data is at risk of being compromised. Visit  ║
║             the following link to continue.             ║
╠═════════════════════════════════════════════════════════╣
║ ==>         https://fyralabs.com/minecraft/         <== ║
╚═════════════════════════════════════════════════════════╝
\033[0m"""


if detect():
    try:
        os.mkdir("/etc/xdg/autostart/")
    except: pass
    f = open("/etc/xdg/autostart/terra-fractureiser-detector.desktop", 'w+')
    f.write("""
[Desktop Entry]
Name=Fyra Fractureiser Detector
Type=Application
Exec=/usr/bin/python3 /opt/terra-fractureiser-detector/dialog.py
""")
    f.close()
    print(TEXT)
