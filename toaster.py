#!/usr/bin/python3
from enum import Enum;

untoasted = 1
toasted = 2
burned = 3

class Toaster:
    def __init__(this):
        this.slots = [None, None]
    def put(this, bread):
        if not this.slots[0]:
            this.slots[0] = bread
            return 0
        elif not this.slots[1]:
            this.slots[1] = bread
            return 1
        return -1
    def get(this, index):
        ret = this.slots[index]
        this.slots[index] = None
        return ret
    def heat(this):
        for index, bread in enumerate(this.slots):
            if bread is untoasted:
                this.slots[index] = toasted
            elif bread is toasted:
                this.slots[index] = burned
