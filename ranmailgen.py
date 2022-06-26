print('''

 ____   _____  _   _  ____    ___   _    _    _____  _    _  _____  _____  _        _____  _____  _   _  _____  ____   _____  _____   ___   ____  
|  _ \ |  _  || \ | ||  _ \  / _ \ | \  / |  |  ___|| \  / ||  _  ||_   _|| |      | ____||  ___|| \ | ||  _  ||  _ \ |  _  ||_   _| / _ \ |  _ \ 
| |_| || | | ||  \| || | | || | | ||  \/  |  | |___ |  \/  || | | |  | |  | |      ||  __ | |___ |  \| || | | || |_| || | | |  | |  | | | || |_| |
|    / | |_| || |\  || | | || | | ||      |  |  ___||      || |_| |  | |  | |      || |_ ||  ___|| |\  || |_| ||    / | |_| |  | |  | | | ||    / 
| |\ \ |  _  || | | || | | || | | || |\/| |  | |    | |\/| ||  _  |  | |  | |      ||   ||| |    | | | ||  _  || |\ \ |  _  |  | |  | | | || |\ \ 
| | | || | | || | | || |_| || |_| || |  | |  | |___ | |  | || | | | _| |_ | |___   ||___||| |___ | | | || | | || | | || | | |  | |  | |_| || | | |
|_| |_||_| |_||_| |_||____/  \___/ |_|  |_|  |_____||_|  |_||_| |_||_____||_____|  |_____||_____||_| |_||_| |_||_| |_||_| |_|  |_|   \___/ |_| |_|

****** Tool Name ::Random Email Genator For Idea ******
       Why This tool :: This tool Is Made for Random Email Genarator
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 
''')

print('''
01. For Gmail
02. For Yahoo
03. For Hotmail
04. For Custom
''')

num = int(input("Enter your Number:"))

if(num == 1):
    import random
    import string

    def emailgen():
        charlen = int(input("Enter the number between 4 to 20::"))

        if(charlen < 4 or charlen > 20):

            print("Enter the Number between 4 to 20!!!")
            exit()

        else:
            letterlist = [string.digits,string.ascii_lowercase,string.ascii_uppercase]
            letterlisttostr = "".join(letterlist)
            emailformat = '@gmail.com'


            emailgen = "".join(random.choices(letterlisttostr, k=charlen)) + emailformat
            print(emailgen)
    emailgen()


if(num == 2):
    import random
    import string

    def emailgen():
        charlen = int(input("Enter the number between 4 to 20::"))

   

        if(charlen < 4 or charlen > 20):
            print("Enter the Number between 4 to 20!!!")
            exit()

        else:
            letterlist = [string.digits,string.ascii_lowercase,string.ascii_uppercase]
            letterlisttostr = "".join(letterlist)
            emailformat = '@yahoo.com'


            emailgen = "".join(random.choices(letterlisttostr, k=charlen)) + emailformat
            print(emailgen)
    emailgen()  

if(num == 3):
    import random
    import string

    def emailgen():
        charlen = int(input("Enter the number between 4 to 20::"))

   

        if(charlen < 4 or charlen > 20):
            print("Enter the Number between 4 to 20!!!")
            exit()

        else:
            letterlist = [string.digits,string.ascii_lowercase,string.ascii_uppercase]
            letterlisttostr = "".join(letterlist)
            emailformat = '@hotmail.com'


            emailgen = "".join(random.choices(letterlisttostr, k=charlen)) + emailformat
            print(emailgen)
    emailgen() 

if(num == 4):
    mail = input("Enter your Domain with @:")

    import random
    import string

    def emailgen():
        charlen = int(input("Enter the number between 4 to 20::"))

   

        if(charlen < 4 or charlen > 20):
            print("Enter the Number between 4 to 20!!!")
            exit()

        else:
            letterlist = [string.digits,string.ascii_lowercase,string.ascii_uppercase]
            letterlisttostr = "".join(letterlist)
            emailformat = str(mail)


            emailgen = "".join(random.choices(letterlisttostr, k=charlen)) + emailformat
            print(emailgen)
    emailgen()                
