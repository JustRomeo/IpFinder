import os
import re
import sys
import time

content: str = ""
cleaned: list = []
happened: list = []
logfile: str = "ip_logs_" + str(int(time.time() * 1000))

# Usage
if (len(sys.argv) == 1):
    print("NAME")
    print("       ", sys.argv[0])
    print("")
    print("SYNOPSIS")
    print("       ", sys.argv[0], "[FILE]")
    print("")
    print("DESCRIPTION")
    print("    List all ip in the file given.")
    sys.exit()

# Reading File
try:
    print("[DEBUG] Reading file: ...", end="\r")
    if os.path.isdir(sys.argv[1]):
        raise Exception(sys.argv[1] + ": The path is a folder.")
    f = open(sys.argv[1])
    content = f.read()
    f.close()
    print("[DEBUG] Reading file: OK ")
except Exception as e:
    print("[ERROR] Reading file: KO \n", e)
    sys.exit()

# Parsing Ip(s)
print("[DEBUG] Parsing Ip(s) in file: ...", end="\r")
happened = re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', content)
for ip in happened:
    if ip not in cleaned:
        cleaned.append(ip)
print("[DEBUG] Parsing Ip(s) in file: OK ")

# Writing Log(s) file
try:
    print("[DEBUG] Writing in file: ...", end="\r")
    f = open(logfile, "w+")
    content = f.write("\n".join(cleaned) + "\n")
    f.close()
    print("[DEBUG] Writing in file: OK ")
except Exception as e:
    print("[ERROR] Writing in file: KO \n" + str(e))
    sys.exit()
