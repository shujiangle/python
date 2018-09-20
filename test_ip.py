#!/usr/bin/python3
# author:shujiangle

ip = open("/root/sh/ip.txt","r")
book = ip.readlines()
ip.close()
NUM=0
for i in book:
    i=i.strip("\n")
    i = i.split()
    NUM+=1
    print("第%s个ip是%s,第%s个port是%s"%(NUM,i[0],NUM,i[1]))   
