### python3 >= 3.5
import subprocess

argvs = ['./input'] + ['a']*99
argvs[ord('A')] = '\x00'
argvs[ord('B')] = "\x20"
argvs[ord('B')+1] = "\x0a"
argvs[ord('B')+2] = "\x0d"

print(argvs)
process = subprocess.Popen(argvs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout, stderr
