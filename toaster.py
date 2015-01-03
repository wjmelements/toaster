#!/usr/bin/python3

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
if __name__ == "__main__":
    t = Toaster()
    import fileinput
    for line in fileinput.input():
        if line.startswith("heat"):
            print("heating...")
            t.heat()
        elif line.startswith("put"):
            slot = t.put(untoasted)
            if slot is -1:
                print("no room in toaster")
            else:
                print("put untoasted bread in slot", slot)
        elif line.startswith("get"):
            for slot in range(2):
                got = t.get(slot)
                if got is untoasted:
                    print("untoasted slice got from slot", slot)
                elif got is toasted:
                    print("toasted slice got from slot", slot)
                elif got is burned:
                    print("burned slice got from slot", slot)
        else:
            print("valid commands are put, get, and heat")
