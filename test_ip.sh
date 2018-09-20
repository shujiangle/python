#!/bin/bash

NUM=1
while read ip port
do  
    echo -e "第$NUM个是$ip"
    echo -e "第$NUM个$port"
    NUM=$(( $NUM + 1 ))
done </root/sh/ip.txt
