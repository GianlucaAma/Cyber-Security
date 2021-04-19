'''Script per decodificare stringhe prese da un file 'string64.txt' in base64 in formato ascii'''
#!/usr/bin/python

import base64
import sys
b64_lines = []
count = 0
with open("string64.txt",'r') as f:
    for line in f:
        line = line.strip("\n")
        line_byte = line.encode("ascii")
        message_bytes = base64.b64decode(line_byte)
        message = message_bytes.decode('ascii')
        count += 1
        b64_lines.append(message)
        print ("{}{}{}{}".format("[+] -----String Decoded n ", count," ", message))
