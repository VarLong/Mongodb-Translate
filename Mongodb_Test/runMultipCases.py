"""
"""
import subprocess
import os
import threading
import time

###############Begin Configuration section #########################

testCases=["artifacts\\build\\tests\\BrowseBar\\BrowseBarEventActionButtons10ft.js", "artifacts\\build\\tests\\BrowseBar\\BrowseBarShowHideTimeout10ft.js", "artifacts\\build\\tests\\LiveTV\\LiveTVGuideExpandedRow10ft.js", "artifacts\\build\\tests\\Settings\\Verify10ftKeyBoardMultiplePin.js", "artifacts\\build\\tests\\Settings\\Verify10ftKeyBoardOnePin.js"]

mylock = threading._allocate_lock()
failTimes=0
failCases=[]
def runTest(cmd):
    global failTimes
    global failCases
    global mylock
    print("start new test running ")
    print(cmd)
    child = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    message=child.communicate()
    if child.returncode != 0:
        mylock.acquire()
        failTimes=failTimes+1
        failCases.append(cmd)
        mylock.release()
    print("one test process ended")


testThreads=[]
for caseName in testCases:
    testCmdLine="node node_modules/nightwatch/bin/nightwatch --env ofunk-chrome-10ft-1080  -t " + caseName + ""
    th = threading.Thread(target=runTest, args=(testCmdLine,))
    testThreads.append(th)
print("Start running ")
for th in testThreads:
    th.start()
    time.sleep(10)

for t in testThreads:
    t.join()
print("Test Result Status :")
print("Failed: {0} FailedCases: {1}".format(failTimes, failCases))
print("Done, please see StableCheckerFailLogs.log file for detailed failed info if have  ")
