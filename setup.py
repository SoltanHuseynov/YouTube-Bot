from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint as rand
import time
import json


alphabet=[

    "a","A","b","B","c","C","d","D",
    "e","E","f","g","h",
    "x","w","s","j",
    "q","r","R","t","T","y",
    "i","o","p","k",
    "l","n","N","m","z","Z",
    "v","u","U"
]
#part-1:name
def idName():#name and password
    name=(

        alphabet[rand(1,35)]+
        alphabet[rand(1,33)]+
        alphabet[rand(1,31)]+
        alphabet[rand(1,29)]+
        alphabet[rand(1,27)]+
        alphabet[rand(1,25)]+
        alphabet[rand(1,23)]+
        alphabet[rand(1,21)]+
        alphabet[rand(1,19)]
    )
    return name

#part-2: lastname
def idlastName():#lastname
    lastname=(

        alphabet[rand(1,35)]+
        alphabet[rand(1,34)]+
        alphabet[rand(1,33)]+
        alphabet[rand(1,32)]+
        alphabet[rand(1,31)]+
        alphabet[rand(1,30)]+
        alphabet[rand(1,29)]+
        alphabet[rand(1,28)]
    
    )
    return lastname

#part-3: password
def idPassword():
    x=rand(1,500)
    passwo=idName()+str(x)
    return passwo

#part-4:get the iphone number
def Tel(number=input("Iphona Number:")):
    return number

#part-5:get the sms verification code and then 
#thsi is add file:"smsCode.txt"
def smsCode():
    code=input("sms-code:")
    value=code.split(",")
    #sms the data json
    data={"sms":value}
    with open("sms-data.json","w") as file:
        #for i in range(len(value)):
        x=json.dumps(data)
        file.write(x)

account=[]

#start firefox
class Run(webdriver.Firefox):
    password=idPassword()
    def __init__(self):
        super().__init__()
        super().get("http://localhost:8080")
    #part1:this the proccess to 
    #create username and passowrd
    @property
    def byname(self):
        name=idName()
        n=super().find_element_by_name("username")
        n.send_keys(str(name))
        return name
    @property
    def bylastname(self):
        lastname=idlastName()
        l=super().find_element_by_name("lastname")
        l.send_keys(str(lastname))
        return lastname
    def byusername(self):
        y=rand(1,200)
        user=self.byname+self.bylastname+str(y)
        z=user+"@gmail.com"
        account.append(z)
        u=super().find_element_by_name("gmail")
        u.send_keys(str(user))
    def bypassword(self):
        password=idPassword()
        account.append(password)
        p=super().find_element_by_name("password")
        a=super().find_element_by_name("approve")
        p.send_keys(str(password))
        a.send_keys(str(password))
    def part1(self):
        self.byusername()
        self.bypassword()
        super().find_element_by_name("Next").click()
    #part-2: the confirm to iphone number and 
    #sms verification
    def bynumber(slef):
        n=super().find_element_by_name("number")
        n.send_keys(str(Tel()))
    def part2(self):
        self.bynumber()
        super().find_element_by_name("go").click()

if __name__=="__main__":
    for i in range(2):
      process=Run()
      process.part1()
      process.part2()

smsCode()
with open("Account.txt","w") as fs:
    fs.write(str(account))

class Google():
    pass