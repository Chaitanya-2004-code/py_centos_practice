import subprocess as sp
ipout = sp.getoutput("ip a")
lines = ipout.split('\n')
for line in lines:
    if 'inet ' in line:
        ip=line.split()[1]
        print("IP add is : ",ip)
    if 'link/ether ' in line:
        mac= line.split()[1]
        print(f'MAC add is : {mac} ')
    if 'state UP ' in line:
        print("The Status is UP")
