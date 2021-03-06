import os
import sys
import subprocess

rootDir = ("/Users/zacks/Desktop/Code/Python/Exercise")

os.chdir(rootDir)
for i in range(5):
    print("times: " + str(i))
    proc = subprocess.Popen(["/Users/zacks/opt/anaconda3/bin/python", "testOs.py"])
    proc.wait()

'''
proc = subprocess.Popen(["/Users/zacks/opt/anaconda3/bin/python", "testOs.py"])


subprocess.run(["/Users/zacks/opt/anaconda3/bin/python", "testOs.py"], stdout=True)
'''
'''
%reset -f

import os
import sys
import subprocess

for i in range(5):
    print("times: " + str(i))
    proc = subprocess.Popen(["/Users/zacks/opt/anaconda3/bin/python", "testOs.py"])
    try:
        proc.wait()
        proc
    except:
        sys.exit()
'''