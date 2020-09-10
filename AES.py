##################################
"""AES algorithm using python AES package"""
##################################

#before running this file run install the requirements 

import ast
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


#encryption function
def encrypt(key, msg):
    iv = get_random_bytes(16)  #getting random bytes
    cipher = AES.new(key, AES.MODE_CFB, iv) #generating key encryption
    ciphertext = cipher.encrypt(msg)    #encrypting plain text with the key given in input
    return iv + ciphertext #returing random bytes and ciphertext


#decryption fuction
def decrypt(key, ciphertext):
    try:
        iv = ciphertext[:16]
        ciphertext = ciphertext[16:]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        smsg = cipher.decrypt(ciphertext)
        return smsg.decode("utf-8")
    except:
        print("=" * 60)
        return print('!!!!!Stopping Decryption process , maybe you entered a wrong key!!!!!')
        

#initialising the main function
if __name__ == "__main__":

    #Enter choice for encryption decryption as e or d
    ed = input("(e)ncrypt or (d)ecrypt: ") 

    #ENCRYPTION
    if ed == "e":
        print("=" * 60)
        key = input("16 digit key: ")    #enter your 16 digit key
        print("=" * 60)
        Nk=2
        #if your key is smaller than 16 then it will fill 0s after that
        if len(key) < Nk * 8:
            print ("Key too short. Filling with \'0\',"
               "so the length is exactly {0} digits.".format(Nk * 8))
            key += "0" * (Nk * 8 - len(key))

        #input file name     
        print("="*60)

        file_plain = input("Enter file name to decrypt: ")

        
        with open(file_plain) as file:   
            msg = file.read()  


        msg = encrypt( key, msg)  # returns the encrpyt function
        #print('Your Plain Text: ',msg)
    
        f_plain = file_plain.split(".")   #splits ur file name
        encrypted_file = (f_plain[0]) + '.' + f_plain[-1]  + '.aes'  #adding .aes extension to make it unreadable

        new_file = open( encrypted_file, mode = "wb")    # creating new file with aes encrypted extension
        new_file.write(msg)
        new_file.close()

        print("=" * 60)
        
        print("Your file has been saved as: " , encrypted_file)   #creates a new encrypted file in ur directory



    #DECRYPTION 
    elif ed == "d":
        print("=" * 60)
        key = input("16 digit key: ")
        print("=" * 60)
        Nk=2
        if len(key) < Nk * 8:
            print ("Key too short. Filling with \'0\',"
               "so the length is exactly {0} digits.".format(Nk * 8))
            key += "0" * (Nk * 8 - len(key))
        print("=" * 60)
        
        file_encrpyted = input("Enter file name to decrypt: ") 
        with open(file_encrpyted,"rb") as fp:   
            smsg = fp.read()
        
        msg=(decrypt(key,(smsg))) #send values to decrypt function

        f_encrypted = file_encrpyted.split(".")   #splits ur file name
        decrypted_file = (f_encrypted[0]) + '.txt'  #adding .aes extension to make it unreadable
        print("=" * 60)

        new_file=open("sample.txt",mode="w")
        new_file.write(msg)
        new_file.close()

        print("=" * 60)

        print("Your file has been saved as: " + decrypted_file)

#Thank you
