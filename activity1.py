with open('Codingal.txt','w') as file:
  file.write("Hi!I am Penguin and I'm 1 yr old.")
file.close()
with open('Codingal.txt','r') as file:
  data = file.readlines()
  print("Words in the file are...")
  for line in data:
    word = line.split()
    print(word)
file.close()
