#!/usr/bin/env python3

import hashlib

def check_pass(pas):
    length =len(pas) >=8
    upper = any(c.isupper() for c in pas)
    low= any(c.islower() for c in pas)
    dig = any(c.isdigit() for c in pas)
    spe = any(c.isalnum() for c in pas)

    s = sum([length,upper,low,dig,spe])

    if s == 5:
        return "stromg"
    else:
        return "Week "



def hash_p(pas):
    return hashlib.sha256(pas.encode()).hexdigest()


Pass=input("Enter the Password: ")
print(check_pass(Pass))

store_hash = hash_p(Pass)
print("SHA-256 PAss : ",store_hash)


