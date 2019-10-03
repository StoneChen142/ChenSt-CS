# Encryption
f=open("text.txt","rt")
data=f.read()
length=len(data)
f.close()


#Encrypt

encrypted_text=""
i=0
while i<length:
    word=data[i]
    if word.islower():
        encrypted_text = encrypted_text + chr(ord(word.upper())+3)
    elif word.isupper():
        encrypted_text = encrypted_text + chr(ord(word.lower())+3)
    else:
        encrypted_text = encrypted_text + chr(ord(word)+3)
    i+=1
    #endif
#endwhile

print("Encrypted text: ",encrypted_text)
print("")

#Decrypt
decrypted_text=""
i=0
while i<length:
    word=encrypted_text[i]
    if word.islower():
        decrypted_text = decrypted_text + chr(ord(word.upper())-3)
    elif word.isupper():
        decrypted_text = decrypted_text + chr(ord(word.lower())-3)
    else:
        decrypted_text = decrypted_text + chr(ord(word)-3)
    i+=1
    #endif
#endwhile

print("Decrypted text: ",decrypted_text)
#ord()
#chr()
