####******************************************#### 
####     HEADER FILE USED IN PROJECT                                #### 
####******************************************#### 
import colorama 
from colorama import Fore 
import time as t 
import random
####******************************************#### 
####     HEADER FILE USED IN PROJECT                                #### 
####******************************************#### 
import colorama 
from colorama import Fore 
import time as t 
import random
from playsound import playsound 
import datetime as dt 
import mysql.connector as c
from playsound import playsound 
import datetime as dt 
import mysql.connector as c
def ti(x): 
    print(x) 
    t.sleep(1.5)
bal=int 
####******************************************#### 
####******************************************####
####******************************************#### 
####      1.Connecting Python with SQL        #### 
####        (Locating the databaes)           #### 
####******************************************#### 
ca=c.connect(host='localhost',user='root',passwd='nhss@123',database='bank') 
####******************************************#### 
####      1.Connecting Python with SQL        #### 
####        (Locating the databaes)           #### 
####******************************************#### 
ca=c.connect(host='localhost',user='root',passwd='nhss@123',database='bank') 
e='YES' or "yes" or 'Yes' 
v='YES' or "yes" or 'Yes' 
co=ca.cursor()
####******************************************#### 
####          ****Creating Database****       #### 
####******************************************#### 
c1=("""create database if not exists bank""") 
co.execute(c1) 
####******************************************#### 
####          ****Creating tables****         ####
c1=("""create table if not exists AddNewCustomer(accountno int primary key ,Aadharid varchar(12) not null, Name varchar(20) not null,address varchar(20) not null, areacode int not null,phoneno int not null,email varchar(30) not null )""") 
co.execute(c1)
c2=("""create table if not exists cusid(username varchar(20) primary key,password varchar(50) not null)""") 
co.execute(c2)
c3=("""create table if not exists manage(username varchar(50) primary key,password varchar(50) not null)""") 
co.execute(c3) 
c4=("""create table if not exists transaction(accountno int primary key,opening_balance int not null, balance int not null)""") 
co.execute(c4)
print("="*70) 
print(" "*15,end='') 
 
print('''\t\t+----------------+----------------+ 
\t\t\t|                                 |           
\t\t\t|             |B A N K |  |M A N A G E M E N T |  | 
\t\t\t|                                 |
\t\t\t+----------------+----------------+''') 
print("="*70)
ram=random.randint(1,4) 
if (ram==1): 
    print("*"*80) 
    print('''  Get our {Home lone} at the rate of 7.5% Only for selected users like you..''') 
    print("*"*80) 
if (ram==2): 
    print("*"*80) 
    print('''  Get our {Private lone} at the rate of 12.5% Only for selected users like you..''')
print("*"*80) 
if (ram==3): 
    print("*"*80) 
    print('''  Get our {Gold lone} at the rate of 6.5% Only for selected users like you..''') 
    print("*"*80) 
if (ram==4):
    print("*"*80)
    print('''  Get our {Car lone} at the rate of 7.5% Only for selected users like you..''') 
    print("*"*80)
####******************************************#### 
#### USING PLAYSOUND(ENHANCING USER INTERFACE) #### 
####******************************************#### 
playsound('D://py//play.mp3')
####******************************************#### 
####******************************************#### 
while e=='YES' or "yes" or 'Yes': 
    print("*"*80) 
    txt=("""/****|𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗕𝗔𝗡𝗞 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗦𝗬𝗦𝗧𝗘𝗠|****\\""")
    x = txt.center(82) 
    print(x) 
    print("*"*80) 
    print('''press 1 for 𝙀𝙈𝙋𝙇𝙊𝙔𝙀𝙀 
press 2 for 𝘾𝙐𝙎𝙏𝙊𝙈𝙀𝙍 
press 3 for 𝙈𝘼𝙉𝘼𝙂𝙀𝙍 
press 4 for 𝙃𝙀𝘼𝘿 
press 5 for 𝙀𝙭𝙞𝙩''') 
op=int(input(''))
if op==1: 
    ti("Loading Employee panal...") 
    print("*"*50) 
    print(" "*15,end='') 
    print("EMPLOYEE PANEL")
    print("*"*50) 
    print('''press 1 for new employee press 2 for existing employee press 3 to exit''') 
    op1=int(input(''))
if op1==1: 
    ti("Loading...") 
    username=input("Enter your username number :") 
    password=input("Enter your password:") 
    confirmpasswd=input("Confirm  your password:")
    if password==confirmpasswd: 
        query="insert into manage values('{}','{}')".format(username,password) 
        co.execute(query) 
        ca.commit()
        e=input("do you want to continue?(yes or no)") 
    if e=="yes": 
        continue 
    else: 
        break
    else: 
        print('your confirm password is incorrect') 
        print('Try again')
        e=input("do you want to continue?(yes or no)") 
        if e=='yes': 
            continue 
        else: 
            break                 
elif op1==2: 
    print("*"*50)
    print(" "*15,end='') 
    print("Employee Panel") 
    print("*"*50) 
    ti("Loading Customer panal...") 
    username=input('Enter your username:') 
    password=input('Enter your password:')
    query="select * from manage where username='{}' and password='{}'".format(username,password) 
    co.execute(query) 
    data=co.fetchall() 
    if data: 
        for i in data: 
            print(':) Logined Successefully........') 
    else: 
            print(':( Logined Unsuccesseful.......') 
    while v=="YES" or "yes" or "Yes":
        if any(data):
            print("1.ACCOUNTS MANAGEMENT") 
            print("2.BALANCE") 
            print("3.VIEW CUSTOMER DETAILS") 
            print('4.EXIT') 
            op3=int(input('ENTER YOUR CHOICE'))
        if op3==1: 
            print("Loading...") 
            t.sleep(1.5) 
            print('1.NEW CUSTOMER')
            print('2.DELETE EXISTING ACCOUNT') 
            op4=int(input('ENTER YOUR CHOICE:'))  
        if op4==1:
            accountno=random.randrange(1000000,9999999,10) 
            print("your accountno is",accountno) 
            Aadharid=input("enter your Aadhar ID:") 
            name=input('Enter custumer name  :') 
            address=input('Enter custumer address  :') 
            areacode=int(input('Enter custumer area PIN CODE  :')) 
            phoneno=int(input('Enter custumer PHONE NUMBER  :')) 
            email=input('Enter custumer email  :') 
            ob=int(input('Enter custumer Opening balance')) 
            bal=ob      
            query="insert into AddNewCustomer(accountno,Aadharid,Name,address,areacode,phoneno,email)values({},'{}','{}','{}',{},{},'{}')".format(accountno,Aadharid,name,address,areacode,phoneno,email) 
            co.execute(query) 
            ca.commit()
            query2=("insert into Transaction(accountno,opening_balance,balance)values({},{},{})").format(accountno,ob,bal) 
            co.execute(query2) 
            ca.commit()
            print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY CREATED")            
            v=input("do you want to continue?(yes or no)") 
        if v=='yes': 
            continue 
        else: 
            break
elif op4==2: 
        print("Loading...") 
        t.sleep(1.5) 
        acc=input("ENTER YOUR ACCOUNT NUMBER:") 
        use=input("ENTER YOUR USERNAME:") 
        info6=co.execute("delete from Transaction where accountno='{}'".format(acc))          
        info7=co.execute("delete from AddNewCustomer where accountno='{}'".format(acc)) 
        co.execute(info6)
        co.execute(info7) 
        ca.commit()
        print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY DELETED") 
        v=input("do you want to continue?(yes or no)") 
        if v=='yes': 
            continue 
        else: 
            break  
elif op3==2:
        accountno=int(input('Enter your account number  :')) 
        query="select balance from Transaction where accountno="+str(accountno) 
        co.execute(query) 
        data3=co.fetchall() 
        toda=dt.date.today()
        print('''Date:-''',toda) 
        print('''Your current balance is ''' , data3) 
        ram=random.randint(1,4)
if (ram==1): 
    print("*"*80) 
    print('''  Get our {Home lone} at the rate of 7.5% Only for selected users like you''') 
    print("*"*80)
if (ram==2): 
    print("*"*80) 
    print('''  Get our {Private lone} at the rate of 12.5% Only for selected users like you ''') 
    print("*"*80) 
if (ram==3): 
    print("*"*80) 
    print('''  Get our {Gold lone} at the rate of 6.5% Only for selected users like you ''') 
    print("*"*80) 
if (ram==4): 
    print("*"*80)
    print('''  Get our {Car lone} at the rate of 7.5% Only for selected users like you ''') 
    print("*"*80)
    print("THANK YOU FOR USING OUR SOFTWARE!!!!") 
    v=input("do you want to continue?(yes or no)") 
    if v=='yes': 
        continue 
    else: 
        break
elif  op3==3: 
    accountno=int(input('Enter your account number  :')) 
    query="select * from AddNewCustomer where accountno=" + str(accountno) 
    co.execute(query) 
    data=co.fetchall()
    for row in data:
        print("*"*50) 
        print(" "*15,end='') 
        print("CUSTOMER DETAILS") 
        print("*"*50) 
        print("Account Number: ", row[0]) 
        print("Aadhar no:",row[1]) 
        print("Person name:",row[2]) 
        print("Residential address:",row[3]) 
        print("area code:",row[4])
        print("phone number:",row[5]) 
        print("email:",row[6]) 
        info5="select * from Transaction where accountno=" + str(accountno) 
        co.execute(info5) 
        data2=co.fetchall() 
        v=input("do you want to continue?(yes or no)")
        if v=='yes': 
            continue 
        else: 
            break 
elif  op3==4: 
        print("THANK  YOU!!!!  VISIT AGAIN!!!!")
elif op==2: 
    print("*"*50) 
    print(" "*15,end='') 
    print("CUSTOMER PANAL") 
    print("*"*50) 
    print('''press 1 for new User press 2 for existing User press 3 to exit''') 
    op1=int(input(''))
    if (op1==1): 
        username=input("Enter your username number :") 
        password=input("Enter your password:") 
        confirmpasswd=input("Confirm your password:") 
             
    if password==confirmpasswd: 
        query="insert into cusid values('{}','{}')".format(username,password) 
        co.execute(query)
        ca.commit()     
        v=input("do you want to continue?(yes or no)") 
        if v=='yes': 
            continue 
        else: 
            break 
elif op1==2: 
    username=input('Enter your username:')
    password=input('Enter your password:')
    query="select * from cusid where username='{}' and password='{}'".format(username,password) 
    co.execute(query) 
    data=co.fetchall()
if data: 
        for i in data: 
            print(':) Logined Successefully........') 
        else: 
            print(':( Logined Unsuccesseful.......')
while v=='YES' or "yes" or 'Yes':
    if any(data): 
        print("*"*50) 
        print(" "*15,end='')
        print("CUSTOMER PANAL") 
        print("*"*50) 
        print("1.BALANCE") 
        print("2.VIEW YOU'R DETAILS") 
        print('3.EXIT') 
        op1=int(input('ENTER YOUR CHOICE'))
if (op1==1): 
    accountno=int(input('Enter your account number  :')) 
    query="select balance from Transaction where accountno="+str(accountno) 
    co.execute(query) 
    data3=co.fetchall() 
    toda=dt.date.today()
    print('''Date:-''',toda) 
    print('''Your current balance is ''' , data3) 
    v=input("do you want to continue?(yes or no)") 
    if v=='yes':
        continue 
    else: 
        break              
elif (op1==2): 
    accountno=int(input('Enter your account number :')) 
    query="select * from AddNewCustomer where accountno=" + str(accountno) 
    co.execute(query) 
    data=co.fetchall() 
    for row in data: 
        print("*"*50) 
        print(" "*15,end='') 
        print("CUSTOMER DETAILS") 
        print("*"*50) 
        print("Account Number: ", row[0]) 
        print("Aadhar no:",row[1]) 
        print("Person name:",row[2]) 
        print("Residential address:",row[3]) 
        print("area code:",row[4]) 
        print("phone number:",row[5]) 
        print("email:",row[6])
        info5="select * from Transaction where accountno=" + str(accountno) 
        co.execute(info5) 
        data2=co.fetchall() 
        v=input("do you want to continue?(yes or no)") 
    if v=='yes': 
        continue 
    else:
        break                 
elif (op1==3): 
        break 






