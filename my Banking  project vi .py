import random

class rbi():
    def __init__(self,user,bal):
        self.rbibal=1000000000
        self.usersinfo=user
        self.userbal=bal
        self.totacc=0
        self.tot_users=0
    def totacc_op(self):
        self.totacc=self.totacc+self.tot_users
        print("Total Account",self.totacc)
    def totacc_close(self):
        self.totacc=self.totacc-self.tot_users
        print("Total Account",self.totacc)
class sbi(rbi):
    def __init__(self,user,bal):
        self.sbibal=500000000
        super().__init__(user,bal)
class tn(sbi):
    def __init__(self,user,bal):
        self.tnbal=170000000
        super().__init__(user,bal)
class ka(sbi):
    def __init__(self,user,bal):
        self.kabal=165000000
        super().__init__(user,bal)
class ap(sbi):
    def __init__(self,user,bal):
        self.apbal=165000000
        super().__init__(user,bal)
class che(tn):
    def __init__(self,user,bal):
        self.chebal=85000000
        super().__init__(user,bal)
class mdu(tn):
    def __init__(self,user,bal):
        self.mdubal=85000000
        super().__init__(user,bal)
class ben(ka):
    def __init__(self,user,bal):
        self.benbal=80000000
        super().__init__(user,bal)  
class mys(ka):
    def __init__(self,user,bal):
        self.mysbal=80000000
        super().__init__(user,bal)   
class vis(ap):
    def __init__(self,user,bal):
        self.visbal=80000000
        super().__init__(user,bal)   
class tir(ap):
    def __init__(self,user,bal):
        self.tirbal=80000000
        super().__init__(user,bal) 
class combine(che,mdu,ben,mys,vis,tir):
    def __init__(self,user,bal):
        super().__init__(user,bal)

    def bal(self):
        b = self.userbal
        res = 0
        for sub in b.values():
            for key,val in sub.items():
                res += val
        print("RBI BALANCE :",self.rbibal+res)
        print("SBI BALANCE:",self.sbibal+res)
        for acc,det in self.usersinfo.items():
                if(det['city'] == 'Chennai'):
                    print("Chennai bal:",self.chebal+self.userbal[acc]["balance"])
                    self.tnbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Madurai'):
                    print("Madurai bal:",self.mdubal+self.userbal[acc]["balance"])
                    self.tnbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Bengaluru'):
                    print("Bengaluru bal:",self.benbal+self.userbal[acc]["balance"])
                    self.kabal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Mysuru'):
                    print("Mysuru bal:",self.mysbal + self.userbal[acc]["balance"])
                    self.kabal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Tirupati'):
                    print("Tirupati bal:",self.tirbal + self.userbal[acc]["balance"])
                    self.apbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Visakapatnam'):
                    print("Visakapatnam bal:",self.visbal + self.userbal[acc]["balance"])
                    self.apbal += self.userbal[acc]["balance"]
        print("TN BALANCE:",self.tnbal)
        print("KA BALANCE:",self.kabal)
        print("AP BALANCE:",self.apbal)
        self.tnbal=170000000
        self.kabal=165000000
        self.apbal=165000000
       


    def amt_credit(self):
        if (self.acc_num in self.userbal and self.usersinfo):
            amt=int(input("Enter the amount:"))
            self.userbal[self.acc_num]['balance'] +=amt
            print("Amount Credited Successfully","current balance:",self.userbal)
            
            
        else:
            print("ERROR TRY AGAIN")
            co.switch()
    def amt_debit(self):
        if (self.acc_num in self.userbal and self.usersinfo):
            amt=int(input("Enter the amount:"))
            if (self.userbal[self.acc_num]['balance']>=amt):
                self.userbal[self.acc_num]['balance']-=amt
                print("Amount debited successfully")
                print("Current Balance:",self.userbal[self.acc_num]['balance'])
                
                
                
            else:
                print("Insufficent balance,Current balnce:",self.userbal[self.acc_num]['balance'])
                co.amt_debit()   
        else:
            print("ERROR TRY AGAIN")
            co.switch()
           
            
    def acc_open(self):
        self.acc_num=random.randint(10000,99999)
        if self.acc_num in self.usersinfo:
            co.ac_open()
        else:
            name=input("Enter the Name:")
            age=int(input("Enter the Age:"))
            print("select your city from options below:\n1.Madurai\n2.Chennai\n3.Mysuru\n4.Bengaluru\n5.Tirupati\n6.Visakapatnam")
            inp = int(input("option:"))
            if(inp == 1):
                city ="Madurai"
            elif(inp == 2):
                city = "Chennai"
            elif(inp == 3):
                city = "Mysuru"
            elif(inp == 4):
                city = "Bengaluru"
            elif(inp == 5):
                city = "Tirupati"
            elif(inp == 6):
                city = "Visakapatnam"
            else: 
                print("please select options from only above please try again")
                co.acc_open()
            balance=0
            self.usersinfo[self.acc_num]={"name":name,"age":age,"city":city}
            self.userbal[self.acc_num]={"balance":balance}
            self.tot_users=len(self.usersinfo)
            print("Account open Successfully","Your Account number is:",[self.acc_num])
            print(self.usersinfo)
            print(self.userbal)

    def acc_close(self):
        if self.acc_num in self.usersinfo and self.userbal:
            if (self.userbal[self.acc_num]['balance']==0):
                self.usersinfo.pop(self.acc_num)
                self.userbal.pop(self.acc_num)
                self.tot_users=len(self.usersinfo)
                print("Account closed successfully")
                print(self.usersinfo)
                print(self.acc_num)
            else:
                print("withdraw your Total balance:",self.userbal[self.acc_num]['balance'])
                co.amt_debit()
                co.acc_close()
        else:
            print("ERROR TRY AGAIN")
            co.switch()
          
    def switch(self):
        print("WELCOME LOGIN YOUR ACCOUNT")
        self.acc_num=int(input("Enter the Account Number:"))
        limit=3
        while limit>0 :
            if (self.acc_num in self.usersinfo and self.userbal):
                print("1.Amount Credit\n2.Amount Debit\n3.Account close\n4.Exit")
                SelectOPtion=int(input("Enter the Option:"))
                
                if SelectOPtion==1:
                    co.amt_credit()
                    co.bal()
                    
                    break
                elif SelectOPtion==2:
                    co.amt_debit()
                    co.bal()
                    
                    break
                elif SelectOPtion==3:
                    co.acc_close()
                    co.totacc_close()
                    
                    break
                else:
                    co.exit()
            else:
                print("Enter the valid Account number")
            limit -=1
            print("retry limit:",limit)
            if (limit>0):
                self.acc_num=int(input("Enter the Account number:"))
        if limit<=0:
            co.exit()
    def exit(self):
        print("Thank You")

    def option(self):
        print("WELCOME\nSelect the below option:")
        print("1.ACCOUNT OPEN\n2.LOGIN\n3.EXIT")
        i=int(input("SELECT OPTION:"))
        if i==1:
            co.acc_open()
            co.option()
                
        elif i==2:
            co.switch()
            co.option()
                
                
        else:
            print("THANK YOU")
            

def load_data():
    try:
        user_data = {}
        bal_data = {}
        with open(r'D:\python\banking.txt', 'r') as filer:
            lines = filer.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.split(':', 1)
                    user_data[int(key.strip())] = eval(value.strip())
        with open(r'D:\python\bankbal.txt', 'r') as filer1:
            lines = filer1.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.split(':', 1)
                    bal_data[int(key.strip())] = eval(value.strip())
    except FileNotFoundError:
        user_data = {}
        bal_data = {}
    except Exception as e:
        print(f"Error reading file: {e}")
        user_data = {}
        bal_data = {}

    return user_data, bal_data
    print(user_data, bal_data)
    



def save_data(user_data, bal_data):
    try:
        with open(r'D:\python\banking.txt', 'w') as file:
            for i, j in user_data.items():
                file.write(f"{i}: {j}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

    try:
        with open(r'D:\python\bankbal.txt', 'w') as file1:
            for i, j in bal_data.items():
                file1.write(f"{i}: {j}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
user_data, bal_data = load_data()
co = combine(user_data, bal_data)
co.option()
save_data(co.usersinfo, co.userbal)









'''import random

class rbi():
    def __init__(self,user,bal):
        self.rbibal=1000000000
        self.usersinfo=user
        self.userbal=bal
        self.totacc=0
        self.tot_users=0
    def totacc_op(self):
        self.totacc=self.totacc+self.tot_users
        print("Total Account",self.totacc)
    def totacc_close(self):
        self.totacc=self.totacc-self.tot_users
        print("Total Account",self.totacc)
class sbi(rbi):
    def __init__(self,user,bal):
        self.sbibal=500000000
        super().__init__(user,bal)
class tn(sbi):
    def __init__(self,user,bal):
        self.tnbal=170000000
        super().__init__(user,bal)
class ka(sbi):
    def __init__(self,user,bal):
        self.kabal=165000000
        super().__init__(user,bal)
class ap(sbi):
    def __init__(self,user,bal):
        self.apbal=165000000
        super().__init__(user,bal)
class che(tn):
    def __init__(self,user,bal):
        self.chebal=85000000
        super().__init__(user,bal)
class mdu(tn):
    def __init__(self,user,bal):
        self.mdubal=85000000
        super().__init__(user,bal)
class ben(ka):
    def __init__(self,user,bal):
        self.benbal=80000000
        super().__init__(user,bal)  
class mys(ka):
    def __init__(self,user,bal):
        self.mysbal=80000000
        super().__init__(user,bal)   
class vis(ap):
    def __init__(self,user,bal):
        self.visbal=80000000
        super().__init__(user,bal)   
class tir(ap):
    def __init__(self,user,bal):
        self.tirbal=80000000
        super().__init__(user,bal) 
class combine(che,mdu,ben,mys,vis,tir):
    def __init__(self,user,bal):
        super().__init__(user,bal)

    def bal(self):
        b = self.userbal
        res = 0
        for sub in b.values():
            for key,val in sub.items():
                res += val
        print("RBI BALANCE :",self.rbibal+res)
        print("SBI BALANCE:",self.sbibal+res)
        for acc,det in self.usersinfo.items():
                if(det['city'] == 'Chennai'):
                    print("Chennai bal:",self.chebal+self.userbal[acc]["balance"])
                    self.tnbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Madurai'):
                    print("Madurai bal:",self.mdubal+self.userbal[acc]["balance"])
                    self.tnbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Bengaluru'):
                    print("Bengaluru bal:",self.benbal+self.userbal[acc]["balance"])
                    self.kabal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Mysuru'):
                    print("Mysuru bal:",self.mysbal + self.userbal[acc]["balance"])
                    self.kabal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Tirupati'):
                    print("Tirupati bal:",self.tirbal + self.userbal[acc]["balance"])
                    self.apbal += self.userbal[acc]["balance"]
                elif(det['city'] == 'Visakapatnam'):
                    print("Visakapatnam bal:",self.visbal + self.userbal[acc]["balance"])
                    self.apbal += self.userbal[acc]["balance"]
        print("TN BALANCE:",self.tnbal)
        print("KA BALANCE:",self.kabal)
        print("AP BALANCE:",self.apbal)
        self.tnbal=170000000
        self.kabal=165000000
        self.apbal=165000000
       


    def amt_credit(self):
        if (self.acc_num in self.userbal and self.usersinfo):
            amt=int(input("Enter the amount:"))
            self.userbal[self.acc_num]['balance'] +=amt
            print("Amount Credited Successfully","current balance:",self.userbal)
            
            
        else:
            print("ERROR TRY AGAIN")
            co.switch()
    def amt_debit(self):
        if (self.acc_num in self.userbal and self.usersinfo):
            amt=int(input("Enter the amount:"))
            if (self.userbal[self.acc_num]['balance']>=amt):
                self.userbal[self.acc_num]['balance']-=amt
                print("Amount debited successfully")
                print("Current Balance:",self.userbal[self.acc_num]['balance'])
                
                
                
            else:
                print("Insufficent balance,Current balnce:",self.userbal[self.acc_num]['balance'])
                co.amt_debit()   
        else:
            print("ERROR TRY AGAIN")
            co.switch()
           
            
    def acc_open(self):
        self.acc_num=random.randint(10000,99999)
        if self.acc_num in self.usersinfo:
            co.ac_open()
        else:
            name=input("Enter the Name:")
            age=int(input("Enter the Age:"))
            print("select your city from options below:\n1.Madurai\n2.Chennai\n3.Mysuru\n4.Bengaluru\n5.Tirupati\n6.Visakapatnam")
            inp = int(input("option:"))
            if(inp == 1):
                city ="Madurai"
            elif(inp == 2):
                city = "Chennai"
            elif(inp == 3):
                city = "Mysuru"
            elif(inp == 4):
                city = "Bengaluru"
            elif(inp == 5):
                city = "Tirupati"
            elif(inp == 6):
                city = "Visakapatnam"
            else: 
                print("please select options from only above please try again")
                co.acc_open()
            balance=0
            self.usersinfo[self.acc_num]={"name":name,"age":age,"city":city}
            self.userbal[self.acc_num]={"balance":balance}
            self.tot_users=len(self.usersinfo)
            print("Account open Successfully","Your Account number is:",[self.acc_num])
            print(self.usersinfo)
            print(self.userbal)

    def acc_close(self):
        if self.acc_num in self.usersinfo and self.userbal:
            if (self.userbal[self.acc_num]['balance']==0):
                self.usersinfo.pop(self.acc_num)
                self.userbal.pop(self.acc_num)
                self.tot_users=len(self.usersinfo)
                print("Account closed successfully")
                print(self.usersinfo)
                print(self.acc_num)
            else:
                print("withdraw your Total balance:",self.userbal[self.acc_num]['balance'])
                co.amt_debit()
                co.acc_close()
        else:
            print("ERROR TRY AGAIN")
            co.switch()
          
    def switch(self):
        print("WELCOME LOGIN YOUR ACCOUNT")
        self.acc_num=int(input("Enter the Account Number:"))
        limit=3
        while limit>0 :
            if (self.acc_num in self.usersinfo and self.userbal):
                print("1.Amount Credit\n2.Amount Debit\n3.Account close\n4.Exit")
                SelectOPtion=int(input("Enter the Option:"))
                
                if SelectOPtion==1:
                    co.amt_credit()
                    co.bal()
                    
                    break
                elif SelectOPtion==2:
                    co.amt_debit()
                    co.bal()
                    
                    break
                elif SelectOPtion==3:
                    co.acc_close()
                    co.totacc_close()
                    
                    break
                else:
                    co.exit()
            else:
                print("Enter the valid Account number")
            limit -=1
            print("retry limit:",limit)
            if (limit>0):
                self.acc_num=int(input("Enter the Account number:"))
        if limit<=0:
            co.exit()
    def exit(self):
        print("Thank You")

    def option(self):
        print("WELCOME\nSelect the below option:")
        print("1.ACCOUNT OPEN\n2.LOGIN\n3.EXIT")
        i=int(input("SELECT OPTION:"))
        if i==1:
            co.acc_open()
            co.option()
                
        elif i==2:
            co.switch()
            co.option()
                
                
        else:
            print("THANK YOU")
            

def load_data():
    try:
        user_data = {}
        bal_data = {}
        with open(r'D:\python\banking.txt', 'r') as filer:
            lines = filer.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.split(':', 1)
                    user_data[int(key.strip())] = eval(value.strip())
        with open(r'D:\python\bankbal.txt', 'r') as filer1:
            lines = filer1.readlines()
            for line in lines:
                if line.strip():
                    key, value = line.split(':', 1)
                    bal_data[int(key.strip())] = eval(value.strip())
    except FileNotFoundError:
        user_data = {}
        bal_data = {}
    except Exception as e:
        print(f"Error reading file: {e}")
        user_data = {}
        bal_data = {}

    return user_data, bal_data
    print(user_data, bal_data)
    



def save_data(user_data, bal_data):
    try:
        with open(r'D:\python\banking.txt', 'w') as file:
            for i, j in user_data.items():
                file.write(f"{i}: {j}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

    try:
        with open(r'D:\python\bankbal.txt', 'w') as file1:
            for i, j in bal_data.items():
                file1.write(f"{i}: {j}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
user_data, bal_data = load_data()
co = combine(user_data, bal_data)
co.option()
save_data(co.usersinfo, co.userbal)'''
