print("\033[1m" + "WARNING THIS SCRIPT WILL OPEN NOTEPAD 1000000 TIMES(!!! NO MALICIOUS PURPOSE !!!)" + "\033[0m")
print("THINK TWICE BEFOURE RUNNING THIS SCRIPT")

input("Press Enter to continue...")
input("I'm not responsible for any damage caused by this script run at your own risk! (Enter to continue...)")
input("This is the last warning do you really want to run this script?! (Enter to continue...)")

if input("ARE YOU SURE? (y/n)") == "n":
    exit()



import subprocess
import tempfile
from pathlib import Path

message_file = Path(tempfile.gettempdir()) / "bye bye ram.txt"
message_file.write_text("bye bye ram", encoding="utf-8")

for _ in range(1000000):
    subprocess.Popen(["notepad.exe", str(message_file)])
print("bye bye ram")