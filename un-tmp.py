#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
# Light modification by @gimbi. Code credit to:
#
# http://www.likexian.com/
# https://gist.github.com/likexian/f9da722585036d372dca
#
# Copyright 2014, Kexian Li
# Released under the Apache License, Version 2.0
##
import struct, sys

XTMP_STRUCT = 'hi32s4s32s256shhiii4i20x'
XTMP_STRUCT_SIZE = struct.calcsize(XTMP_STRUCT)

def read_xtmp(fname):
    result = []

    fp = open(fname, 'rb')
    while True:
        bytes = fp.read(XTMP_STRUCT_SIZE)
        if not bytes:
            break

        data = struct.unpack(XTMP_STRUCT, bytes)
        data = [(lambda s: str(s).split("\0", 1)[0])(i) for i in data]
        if data[0] != '0':
            result.append(data)

    fp.close()
    result.reverse()

    return result


print 'Type,Login process PID,TTY Device,TermName or inittab(5),Username ,Hostname or kernel version,Exit status ,?ut_session?,Session ID (getsid(2)),UnixTime,IPv4 address,Future use'
data = read_xtmp(sys.argv[1])
for i in data:
    
		print ','.join(map(str,i))

print