import os
import secrets
from cryptography.fernet import Fernet

directory = input('press any button to start: ')
file_name = 'KEY.key'
file_path = os.path.join(directory, file_name)

var = input('Do you have the key y/n: ')
if var == 'y':
    try:
        with open('KEY.key','rb') as key_file:
            key = key_file.read()
        fernet = Fernet(key)
        print('|-----------|')
        print('|key loaded |')
        print('|-----------|')
    except FileNotFoundError:
        print('|-----------------|')
        print('|key not there load|')
        print('|-----------------|')
elif var == 'n':
    if os.path.exists(file_path):
        print('key already exists')
        user = input('do you want to overwrite the previous key y/n | WARNING if there are any passwords that were encrypted with current key they cant be decrypted if the current key is overwritten: ')
        if user == 'y':
            key = Fernet.generate_key()
            fernet = Fernet(key)
            with open('KEY.key','wb') as key_file:
                key_file.write(key)
                print('Key created keep this key file some where safe')
        elif user == 'n':
            print('key wasnt over written')
    if os.path.exists(file_path) == False:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        with open('KEY.key','wb') as key_file:
            key_file.write(key)
            print('Key created keep this key file some where safe')
        
list = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def gen_pswds():
    pswd_list = []
    user_input1 = input('\npress enter to continue :')
    print('-------------------------\n')
    while user_input1 != '3':
        print('|--------------------------------|')
        user_input1 = input('|type 1 to generate new password |\n|type 2 to decrypt               |\n|type 3 to exit                  |\n|--------------------------------|\n type here: ')
        if user_input1 == '1':
            pswd_len = int(input("Enter the length of the password: "))
            print('the below password will be encrypted when saving it')
            for i in range(pswd_len):
                pswd = secrets.choice(list)
                pswd_list.append(pswd)
            clean_pswd = ''.join(pswd_list)
            print('|--------------------------------------------------------|')
            print('|this is the generated password: '+ clean_pswd + '              |')
            print('|--------------------------------------------------------|') 
              
            sv_ip = input("\nSave the above password yes/no:  ")
            if sv_ip == 'yes':
                sv_for = input("This password is for: ").capitalize()
                svd_for_wch = []
                for i in sv_for:
                    svd_for_wch.append(i)
                clean = ''.join(svd_for_wch)
                encrypt_pswd = fernet.encrypt(clean_pswd.encode())
                print('Your saving this password for: ' + clean)
                pswd_file = 'passwords.txt'
                with open(pswd_file,'a') as file:
                    wrt = clean + (' uses this ' + "password:--> " + str(encrypt_pswd) + '\n')
                    file.write(wrt)
                file.close()
                print('|--------------|')
                print("|Password Saved|")
                print('|--------------|\n')
            elif sv_ip == 'no':
                pswd_list.clear()
                
        elif user_input1 == '2':
            file = open('passwords.txt','r')
            print('|-----------------------------------------------------------------------------------------------------------------------------------------------------|')
            print(file.read())
            print('|-----------------------------------------------------------------------------------------------------------------------------------------------------|')
            dcr = input('which password you want to decrypt: ').encode()
            try:
                decrypt_pswd = fernet.decrypt(dcr.decode())
                print(decrypt_pswd)
            except:
                print('|-----------|')
                print('|wrong key  |')
                print('|-----------|\n')

        elif user_input1 == '3':
            print('program closed')
            break

gen_pswds()