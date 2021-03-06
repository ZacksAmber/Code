#!/usr/bin/env python3
import os
import subprocess
import time

rootDir = ("/Users/zacks/Desktop/Code/Python/Exercise")
testDir = rootDir+"/test/"
'''
os.chdir(testDir)
for i in os.listdir(testDir):
    proc = subprocess.Popen(["cat", i])
    try:
        print(i + " content: ")
        outs, errs = proc.communicate(timeout=15)
        print("Process Running Succeed: " + i)
        time.sleep(15)
    except:
        proc.kill()
        outs, errs = proc.communicate()
        print("Process Running Failed: " + i)
        print("")
'''
os.chdir(testDir)
for i in os.listdir(testDir):
    proc = subprocess.Popen(["cat", i])
    try:
        print(i + " content: ")
        proc.wait()
        print("Process Running Succeed: " + i)
        print("")
        time.sleep(2)
    except:
        proc.kill()
        print("Process Running Failed: " + i)
        print("")


