#!/usr/bin/env python3

import subprocess as sp
file= input("Enter the file name : ")
sp.getoutput(f"openssl enc -aes-256-cbc -pbkdf2 -in {file} -out encrypt.txt")
print("file was encrepted ")
sp.getoutput(f"openssl enc -d -aes-256-cbc -pbkdf2 -in encrypt.txt -out decrypt.txt")
print("file decrypt")
