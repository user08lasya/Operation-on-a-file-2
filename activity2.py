new_file = open('New_File2.txt','x')
new_file.close()

import os
print("Checking if Codingal file  exists or not")
if os.path.exists("Codingal(1).txt"):
    os.remove("Codingal.txt")
else:
    print("The file does not exist")

Codingal = open("Codingal(1).txt","w")
Codingal.write("Hi! I am Penguin and I am 1 yr old.")
Codingal.close()

os.remove('Codingal.txt')
