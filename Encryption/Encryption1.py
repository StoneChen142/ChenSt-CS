# Encryption
f=open("text.txt","rt")
data=f.read()
length=len(data)
f.close()


#Encrypt

encrypted_text=""
i=1
while i<length:
    word=data[i]
    if word.islower():
        encrypted_text = encrypted_text + str(word.upper)
    elif word.islower():
        encrypted_text = encrypted_text + str(word.lower)
    i+=1
    #endif
#endwhile

print("Encrypted text: ",encrypted_text)
#Decrypt
#ord()
#chr()
