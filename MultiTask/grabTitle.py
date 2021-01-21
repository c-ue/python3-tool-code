#!/usr/bin/python
import time
from hashlib import sha256
from urllib.request import urlopen
import requests
import asyncio

wordSet = list("0123456789abcdef")
wordSetMod = len(wordSet)

def genUrl(protoSchema, BaseDomain):
    prefix = [0] * 12
    loop = asyncio.get_event_loop()
    tasks = []
    counter = 0
    while True:
        url = protoSchema
        for i in prefix:
            url += wordSet[i]
        url += BaseDomain
        tasks.append(loop.create_task(genTitle(url, loop)))
        counter += 1
        prefix[0] += 1
        Carry = False
        for i in range(len(prefix)):
            if Carry is True:
                prefix[i] += 1
                Carry = False
            if prefix[i] == wordSetMod:
                Carry = True
                prefix[i] -= wordSetMod
        if Carry is True:
            break
        if counter == 25:
            counter = 0
            print("wait for asyncio")
            loop.run_until_complete(asyncio.wait(tasks))
            time.sleep(5)
            tasks = []

async def genTitle(url, loop):
    for _ in range(3):
        res = await loop.run_in_executor(None,requests.get,url)
        if res.status_code == 200:
            title = res.text.decode("utf8").split('<title>')[1].split('</title>')[0]
            print(url, ",", title)
            return
        else:
            # print("connect Error ASCE@VFVDF.")
            pass


def main():
    pass

def test():
    genUrl("http://" , ".ngrok.io")

if __name__ == "__main__":
    test()
