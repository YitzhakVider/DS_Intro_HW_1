# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:59:21 2022

@author: yitzhak vider
"""
def shortestWord (list):
    shortestLen=len(list[0])
    ret = 0
    for i in range(1,len(list)):
        if(len(list[i])<shortestLen):
           shortestLen = len(list[i])
           ret = i
    return ret

def longest_words (file):
    try:
        fhand=open(file)
    except: 
        return(print("file not found"))
    x=['a', 'a', 'a', 'a', 'a']
    words = list()
    for line in fhand:
        line=line.replace(',', ' ')
        line=line.replace('-', ' ')
        line=line.replace('.', ' ')
        line=line.replace('(', ' ')
        line=line.replace(')', ' ')
        splitedLine=line.split()
        for word in splitedLine:
            words.extend(word)
            
            if "(" not in word and ")" not in word and "." not in word and "-" not in word :
                words.append(word)

    for word in words:
        minWordIndex = shortestWord(x)
        if (len(x[minWordIndex]))<len(word):
            x[minWordIndex] = word
        
    
                
    x = sorted(x, key = len, reverse = True)               
    return(print(x))
        

           
        
    
   
file=input("Enter the name of the file: ") 
# file="C:/Users/yitzhak vider/DS Introduction Course/files/ex3_text.txt"
longest_words(file) 
