sentence = input("write a sentence:")
freq=[0 for i in range(0,26)]

for i in sentence:
    if(i!=' '):
        character = i.lower()
        index = ord(character) - 97
        freq[index]+=1

flag = True
for i in range(0,26):
    if(freq[i]==0):
        flag = False

if(flag == True):
    print("It is a pangram")
else:
    print("It is not a pangram") 
        
        
