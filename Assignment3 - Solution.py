# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:06:24 2022

@author: yitzhak vider
"""

def read_line (n, file):
    try:
        n=int(n)
    except:
        return(print("invalid input detected"))
    try:
        fhand=open(file)
    except: 
        return(print("file not found"))
    
    count=1
    for line in fhand:
        if count==n:
            return(print("Line "+str(count)+": "+ line))
        count=count+1
    if count<n:
        return(print("Line "+str(n)+" doesn't exist "))
        

           
        
    
n=input("Enter a number: ")   
file=input("Enter the name of the file: ") 
#file="C:/Users/yitzhak vider/DS Introduction Course/files/ex3_text.txt"
read_line(n, file)    
