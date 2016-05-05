import subprocess

subprocess.call("python gpsStamp.py", shell=True)
subprocess.call("python makeSignup.py", shell=True)
subprocess.call("python makeSheets.py", shell=True)
