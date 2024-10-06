
FIRST_CHAR_CODE=ord('A')
LAST_CHAR_CODE=ord('Z')
CHAR_RANGE=LAST_CHAR_CODE-FIRST_CHAR_CODE+1


def encode(text,shift):
    res=""
    for ch in text.upper():
        if ch.isalpha():

            ch_code=ord(ch)
            new_ch_code=ch_code+shift

            if new_ch_code >LAST_CHAR_CODE: 
                new_ch_code-=CHAR_RANGE

            if new_ch_code < FIRST_CHAR_CODE:
                new_ch_code+=CHAR_RANGE


            new_ch=chr(new_ch_code)
            res+=new_ch
        else:
            res+=ch 

    return res        

print()
print()
print('    CAESAR CIPHER')
print()

text=input("Enter the message to be sent : ")
shift=int(input("Enter the encryption key : "))
encrypted_msg=encode(text,shift)
print()
print("Message is Encrypted : ",encrypted_msg)

#decoding
ans=input("Do You want to decrypt the message? (y/n)  ")
if ans.lower()=='y':
    pass_key=int(input('Enter the pass key : '))
    if pass_key == shift:
        decrypted_msg=encode(encrypted_msg,-shift)
        print("Decrypted message is : ",decrypted_msg)
        print()
    else:
        print('Wrong Pass Code')    
elif ans.lower()=='n':
    pass
else:
    print()
    print("Wrong Input!")

