import numpy
from math import sqrt
from time import sleep

def hello_world():
    print('hello world')

def recursion(loop=5):
    if loop == 0:
        return
    recursion(loop-1)

def limited_time(sec):
    sleep(sec)