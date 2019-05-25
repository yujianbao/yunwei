#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys

ssh = pexpect.spawn('ssh root@192.168.20.103 ')
fout = open('sshlog.txt', 'w')
ssh.logfile = fout


ssh.expect("root@192.168.20.103's password:")

ssh.sendline("yzg1314520")

ssh.expect('#')
ssh.sendline('ls /home')
ssh.expect('#')