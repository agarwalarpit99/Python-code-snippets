#!/bin/python3

import math
import os
import random
import re
import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT

class Student:
    def __init__(self,roll,name,marks_list):
        self.roll=roll
        self.name=name
        self.marks_list=marks_list
    def calculate_percentage(self):
        self.percent=sum(self.marks_list)
        self.ans=self.percent/len(self.marks_list)
        self.ans=int(self.ans)
        return self.ans
    def find_grade(self):
        if self.ans>=80:
            return 'A'
        elif self.ans>=60 or self.ans<80:
            return 'B'
        elif self.ans>=40 or self.ans<60:
            return 'C'
        elif self.ans<40:
            return 'F'


if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())