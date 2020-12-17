#!/usr/bin/env python3


import os
import sys
import time
import datetime


def PrintHelper():
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')


def Add(filename, item, doneFile):
    if (item == ""):
        print("Error: Missing todo string. Nothing added!")
        return
    _file = open(filename, "a+")
    if (doneFile):
        _file.write("x " + str(datetime.datetime.today()).split()
                    [0] + item + "\n")
    else:
        _file.write(item + "\n")
    _file.close()


def Show(filename):
    todo_file = open(filename, "r")
    items = todo_file.readlines()
    len_items = len(items)

    if (len_items == 0):
        print("There are no pending todos!")
        return

    for i in range(len_items):
        print("[" + str(len_items-i) + "]", items[len_items - 1 - i][:-1])
    todo_file.close()


def ErrorCheck(lines, index, fromDeleteItem):
    numLines = len(lines)
    if (numLines == 0 or index > numLines or index <= 0):
        if(fromDeleteItem):
            print("Error: todo #" + str(index) +
                  " does not exist. Nothing deleted.")
        else:
            print("Error: todo #"+str(index)+" does not exist.")
        return False
    return True


def DeleteItem(filename, index):
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()

    isOkay = ErrorCheck(lines, index, True)
    if (not isOkay):
        return False

    delString = lines[index - 1]

    with open(filename, "w") as f:
        for line in lines:
            if line != delString:
                f.write(line)
    return True


def DoneItem(index):  # Redundancy -> Try invoking delete and add
    lines = []
    with open("todo.txt", "r") as f:
        lines = f.readlines()

    isOkay = ErrorCheck(lines, index, False)
    if(isOkay):
        Add("done.txt", lines[index - 1][:-1], True)
        DeleteItem("todo.txt", index)
        return True

    return False


def ShowStats():
    pending = len(open("todo.txt", "r").readlines())
    done = len(open("done.txt", "r").readlines())

    print (str(datetime.datetime.today()).split()
           [0], "Pending : " +
           str(pending)+" Completed : "+str(done))

# Extra feature - Verbose Report


def ShowEverything():
    print("\n")
    ShowStats()
    print("\n[+]Pending Tasks:")
    Show("todo.txt")
    print("\n[-]Completed Tasks:")
    Show("done.txt")
    print("\n")


def start():
    n = len(sys.argv)
    # Create empty files (to fix: No such file or dir bug)
    f1 = open("todo.txt", "a+")
    f2 = open("done.txt", "a+")
    f1.close()
    f2.close()
    # No arguement passed -> Usage
    if n == 1:
        PrintHelper()
    # Called help or -h flag
    elif (n == 2 and (sys.argv[1] == 'help' or sys.argv[1] == '-h')):
        PrintHelper()

    for i in range(len(sys.argv)):
        if sys.argv[i] == 'add':
            if (i + 1 >= n):
                print("Error: Missing todo string. Nothing added!")
                continue
            Add("todo.txt", sys.argv[i + 1], False)
            print("Added todo: \""+sys.argv[i + 1]+"\"")

        elif sys.argv[i] == 'ls':
            Show("todo.txt")

        elif sys.argv[i] == 'del':
            if (i + 1 >= n):
                print("Error: Missing NUMBER for deleting todo.")
                continue

            if (DeleteItem("todo.txt", int(sys.argv[i + 1]))):
                print("Deleted todo #"+sys.argv[i + 1])

        elif sys.argv[i] == 'done':
            if (i + 1 >= n):
                print("Error: Missing NUMBER for marking todo as done.")
                continue
            if(DoneItem(int(sys.argv[i + 1]))):
                print("Marked todo #" + sys.argv[i + 1] + " as done.")

        elif sys.argv[i] == 'report':
            ShowStats()
        # Extra feature - Verbose Report
        elif sys.argv[i] == 'reportVerbose':
            ShowEverything()


# Entry point
if __name__ == "__main__":
    start()
