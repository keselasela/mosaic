import subprocess
proc = subprocess.run(["ls"],stdout = subprocess.PIPE,stderr = subprocess.PIPE, cwd="/home")

print(proc.stdout.decode("utf8"))

print(proc.stdout)