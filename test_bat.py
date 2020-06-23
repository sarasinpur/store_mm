import os

myBat = open(r'D:\Users\sarasinpur\Desktop\Work\MM_Store\Result\test.bat','w+')
myText = open("D:\\Users\\sarasinpur\\Desktop\\Work\\MM_Store\\Test_woy.txt", "r")
Content = myText.read()
i = 1
lines = Content.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]

Content_Use = ""
for line in non_empty_lines:
    Content_Use += line + "\n"
# Content_Use = Content_Use.split("\n")
Content_Use = [elements.split("__") for elements in Content_Use.strip().split("\n")] 

for each_list in Content_Use:
    while '' in each_list:
        each_list.remove('')
    if i == 1:
        myBat.write("@echo off\n")
    else :
        if each_list[0][0] == '0':            
            IP = "117.1" + each_list[0][1:3] + ".1" + each_list[0][3:5] + ".110"
            myBat.write("call ping D:\Temp\sarasinpur\files\pingcheck.bat " + IP + "\n")
        elif each_list[0][0] != '0':   
            IP = "11" +  each_list[0][0] + ".1" +  each_list[0][1:3] + ".1" + each_list[0][3:5] + ".110"
            myBat.write("call ping D:\Temp\sarasinpur\files\pingcheck.bat " + IP + "\n")
    i = i+1

myBat.close()
