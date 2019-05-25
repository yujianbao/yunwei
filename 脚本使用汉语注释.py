#!/usr/bin/python
# -*- coding:utf-8 -*-
# 输入这一条就可以在Python脚本里面使用汉语注释！此脚本可以直接复制使用；

while True:  # 进入死循环
    input = raw_input('Please input your username:')

    # 交互式输入用户信息，输入input信息；
    if input == "wenlong":
        # 如果input等于wenlong则进入此循环（如果用户输入wenlong）
        password = raw_input('Please input your pass:')
        # 交互式信息输入，输入password信息；
        p = '123'
        # 设置变量P赋值为123
        while password != p:
            # 如果输入的password 不等于p（123）， 则进此入循环
            password = raw_input('Please input your pass again:')
        # 交互式信息输入，输入password信息；
        if password == p:
            # 如果password等于p（123），则进入此循环
            print
            'welcome to select system!'  # 输出提示信息；
            while True:
                # 进入循环；
                match = 0
                # 设置变量match等于0；
                input = raw_input("Please input the name whom you want to search :")
                # 交互式信息输入，输入input信息；
                while not input.strip():
                    # 判断input值是否为空，如果input输出为空，则进入循环；
                    input = raw_input("Please input the name whom you want to search :")
                # 交互式信息输入，输入input信息；
                name_file = file('search_name.txt')
                # 设置变量name_file，file('search_name.txt')是调用名为search_name.txt的文档
                while True:
                    # 进入循环；
                    line = name_file.readline()  # 以行的形式，读取search_name.txt文档信息；
                    if len(
                            line) == 0:  # 当len(name_file.readline() )为0时，表示读完了文件，len(name_file.readline() )为每一行的字符长度，空行的内容为\n也是有两个字符。len为0时进入循环；
                        break  # 执行到这里跳出循环；
                    if input in line:  # 如果输入的input信息可以匹配到文件的某一行，进入循环；
                        print
                        'Match item: %s' % line  # 输出匹配到的行信息；
                        match = 1  # 给变量match赋值为1
                if match == 0:  # 如果match等于0，则进入   ；
                    print
                    'No match item found!'  # 输出提示信息；
    else:
        print("Sorry ,user  %s not found " % input)  # 如果输入的用户不是wenlong，则输出信息没有这个用户；

# !/usr/bin/python
while True:
    input = raw_input('Please input your username:')
    if input == "wenlong":
        password = raw_input('Please input your pass:')
        p = '123'
        while password != p:
            password = raw_input('Please input your pass again:')
        if password == p:
            print
            'welcome to select system!'
            while True:
                match = 0
                input = raw_input("Please input the name whom you want to search :")
                while not input.strip():
                    print
                    'No match item found!'
                    input = raw_input("Please input the name whom you want to search :")
                name_file = file('search_name.txt')
                while True:
                    line = name_file.readline()
                    if len(line) == 0:
                        break
                    if input in line:
                        print
                        'Match item: ', line
                        match = 1
                if match == 0:
                    print
                    'No match item found!'
    else:
        print("Sorry ,user  %s not found " % input)