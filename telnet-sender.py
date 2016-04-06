import getpass
import sys
import telnetlib
import json

with open('config.js') as json_data_file:
    data = json.load(json_data_file)
print(data)

HOST = data['lw12']['fhemip']
PORT = data['lw12']['fhemport']
print "python running, printing args passed to script:"
print sys.argv[1]
tn = telnetlib.Telnet(HOST,PORT)

tn.write(sys.argv[1])
tn.write("\n")
tn.write("exit\n")

print tn.read_all()
