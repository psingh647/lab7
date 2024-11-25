#!/usr/bin/env python3
# Student ID: psingh647

def function1():
    global schoolName  # Declare schoolName as global to modify the global object
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # This already declares schoolName as global, allowing modification of the global object
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)  # Now reflects the change made in function1
function2()
print('print() in main on schoolName:', schoolName)  # Reflects the change made in function2
