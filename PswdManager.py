
class account:
    website=""
    email=""
    password=""

    def __init__(self,ws,em,pw):
        self.website=ws
        self.email=em
        self.password=pw
    
    def show(self):
        print(self.email)
        print(self.password)
        return;

accountsArray=[]



#.........................................................................................
#the main method,lets 
def chooseAction():
    print("You want to enter a new password(press 1) or you wanna look up a password(press2)--End program with \"3\"")
    modeDec= input()
    if modeDec=="1":
        addAccount()
    elif modeDec=="2":
        readAccount("dataFile.txt")
    elif modeDec=="3":
        print("Program shuts down!")
        saveInformation("dataFile.txt")
    else:
        print("Invalid Input")
        chooseAction()
        return;


#method for adding a new Account, asks details then executes initAccount()
def addAccount():
    print("Which website is this Account for?")
    InputWebsite=input()
    print("What email adress does the password belong to?")
    Inputemail =input()
    print("Now enter the password: ")
    Inputpassword =input()
    initAccount(InputWebsite,Inputemail,Inputpassword)
    print("Succesfullly created new Object!")
    chooseAction()
    return;

def readAccount(fileName):
    file=open(fileName,"r")
    doc=file.read()
    file.close()
    print(doc)
    return doc;


#adds a new account to the account array
def initAccount(IWebsite,Iemail,Ipassword):
   tempAccount=account(IWebsite,Iemail,Ipassword)
   accountsArray.append(tempAccount)


#goes to the an txt file and saves the data in it
def saveInformation(fileName):
    file=open(fileName,"a")
    for tempAcc in accountsArray:
        file.write("Website: "+tempAcc.website+"\n")
        file.write("Email: "+tempAcc.email+"\n")
        file.write("Password: "+tempAcc.password+"\n")
        file.write("----------------------"+"\n"+"\n")
    file.close()
    print("Saved Data")


#-------------------- Main Method Call!!!---------------------
chooseAction()
input('Press ENTER to exit')
