#!/usr/bin/python
import time
from hashlib import sha256
from urllib.request import urlopen

print("your word set:「" + "".join([chr(i) for i in range(0x21,0x7e+1)]) + "」")


def task1(seedStr):
    wordSet = [chr(i) for i in range(0x21,0x7e+1)]
    prefix = [0,0,0,0,0]
    while True:
        mod = len(wordSet)
        string = wordSet[prefix[0]] + wordSet[prefix[1]] + wordSet[prefix[2]] + wordSet[prefix[3]] + wordSet[prefix[4]] + seedStr
        h = sha256(string.encode("ascii")).hexdigest()
        if h.startswith('00000'):
            print(string)
        prefix[0] += 1
        if prefix[0] >= mod:
            prefix[0] %= mod
            prefix[1] += 1
        if prefix[1] >= mod:
            prefix[1] %= mod
            prefix[2] += 1
        if prefix[2] >= mod:
            prefix[2] %= mod
            prefix[3] += 1
        if prefix[3] >= mod:
            prefix[3] %= mod
            prefix[4] += 1
        if prefix[4] >= mod:
            break

def task2(url):
    html = urlopen(url).read()
    title = html.decode("utf8").split('<title>')[1].split('</title>')[0]
    print(title)

def multithreading(taskFunc, taskNum, cases):
    start = time.time()
    from threading import Thread, Semaphore
    def worker(taskFunc, case):
        taskFunc(case)
        sem.release()
    sem = Semaphore(taskNum)
    threads = []
    for i in range(len(cases)):
        threads.append(Thread(target = worker, args = (taskFunc, cases[i],)))
        sem.acquire()
        threads[i].start()
    for i in threads:
        i.join()
    print("time spent: " + str(time.time()-start))
    return

def multiprocessing(taskFunc, taskNum, cases):
    start = time.time()
    from multiprocessing import Process, Pool
    pool = Pool(taskNum)
    pool.map(taskFunc, cases)
    print("time spent: " + str(time.time()-start))
    return

def coroutine(taskFunc, taskNum, cases):
    start = time.time()
    import asyncio
    async def worker(taskFunc, case):
        taskFunc(case)
    async def asyncmain(taskFunc, taskNum, cases):
        taskList = []
        pending = []
        casesNum = len(cases)
        i = 0
        while i<casesNum:
            if len(pending) < taskNum:
                taskList.append(asyncio.create_task(worker(taskFunc, cases[i])))
                await asyncio.wait([taskList[len(taskList)-1]])
                i+=1
            _, pending = await asyncio.wait(taskList, timeout=None)
    asyncio.run(asyncmain(taskFunc, taskNum, cases))
    print("time spent: " + str(time.time()-start))

def main():
    multitaskMethod = [multithreading, multiprocessing, coroutine]
    taskMethod = [task1, task2]
    taskOrd = int(input(),10)
    multiMethodOrd, taskNum = input().split(" ")
    multiMethodOrd, taskNum = int(multiMethodOrd,10), int(taskNum,10)
    caseNum = int(input(),10)
    cases = []
    for _ in range(caseNum):
        cases.append(input())
    multitaskMethod[multiMethodOrd](taskMethod[taskOrd], taskNum, cases)

def test():
    print("multithreading sha256")
    multithreading(task1, 2,["abcde", "efghj", "12311"])
    print("multiprocessing sha256")
    multiprocessing(task1, 2,["abcde", "efghj", "12311"])
    print("coroutine sha256")
    coroutine(task1, 2,["abcde", "efghj", "12311"])
    print("multithreading urlopen")
    multithreading(task2, 2,["https://www.google.com/", "https://tw.yahoo.com", "https://www.nctu.edu.tw"])
    print("multiprocessing urlopen")
    multiprocessing(task2, 2,["https://www.google.com/", "https://tw.yahoo.com", "https://www.nctu.edu.tw"])
    print("coroutine urlopen")
    coroutine(task2, 2,["https://www.google.com/", "https://tw.yahoo.com", "https://www.nctu.edu.tw"])

if __name__ == "__main__":
    test()
