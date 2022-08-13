import random as rd

from logging import raiseExceptions









'''Created a class called Customer, with Total_user and active_user counting  '''
class Customer:
    total_Customer = 0
    active_Customer = 0
    
    """Created __init__ function with 10 parameter has it's own unique methods"""
    def __init__(self,first_name,last_name,phone,email,Date_of_birth=0,address=0,Adhar_no=0,pancard_no=0,account_no=0,balance=10000):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.Adharcard = Adhar_no
        self.pancard = pancard_no
        self.accounts = account_no
        self.dob = Date_of_birth
        self.balance = balance
        '''keep the count of customer'''
        Customer.total_Customer += 1

    print("************Welcome to RSTF Bank*****************")

    '''
        Created a Login function for Customer count +1 has given below.
    '''
    def login(self):
        Customer.active_Customer += 1
        print(f"{self.first_name} {self.last_name} has now logged in\n")

    """
       Created a Logout function for Customer count -1 has given below

    """
    def logout(self):
        Customer.active_Customer -= 1
        print(f"{self.first_name} {self.last_name} has now logged out\n")

    '''
       Created a function to add email_id
    '''
    def add_email(self):
        return input(f"Add new Email {self.first_name} {self.last_name}\n")

        
    '''
   
       Created a function to add your home address

    '''
    def add_address(self):
        return input(f"Add your home address {self.first_name} {self.last_name}\n")


    '''
       Created a function to add your 12 digit Adharcard.
    '''

    def add_adharcard(self):
        add = input(f"Add your 12 digit Adharcard {self.first_name} {self.last_name}\n")

        '''
        It will give incorrect id, if you put less then or bigger then 12 digit number.
        
        while loop has been use for the exact number of digit (You can change accordingly)
        '''

        while len(add) != 12:
            print("Incorrect Adharcard ")
            add = input(f"{self.first_name} {self.last_name} please enter your Adharcard again:-")
        print(f'{self.first_name} {self.last_name} you have succesfully added Adharcard_No')

    '''
        Created a function to add your 10 digit pancard 
    '''   

    def add_pancard(self):
        add = input(f"Add your 10 digit pancard {self.first_name} {self.last_name}\n")

        
        ''' 
           It will give incorrect id, if you put less then or bigger then 10 digit number.

           while loop has been use for the exact number of digit (You can change accordingly).
        '''

        while len(add) != 10:
            print("Incorrect pancard ")
            add = input(f"{self.first_name} {self.last_name} please enter your pancard again: ")
        print(f'{self.first_name} {self.last_name} you have succesfully added pancard_No')

    '''
    Created a function to add your Date of birth
    '''    
    
    def add_DOB(self):
        a = input(f"Add your Date of Birth {self.first_name} {self.last_name}\n")

        '''
            if and else statement is used 
        
            Here the len() function is used for the exact number of digit Eg(( 18/12/2002 )) with value 10 , 9 , 6 
        '''
        if len(a) == 10:
            print('You have successfully added Date of birth')
        elif len(a) == 9:
            print('You have successfully added Date of birth')
        elif len(a) == 6:
            print('You have successfully added Date of birth')
        else:
            raise Exception('You have enter a wrong Date of birth, please enter date Eg(18/1/2002) or (18/1/22)')

    '''
    Created a function to generate automatic Account number of length (8)

    '''

    '''
    Imported Random as rd
    '''

    '''
       Function will work like, you have to give a list of str and then you have give a variable an empty list
       using for loop in range, give the range 2 parameters. Create a new variable name Joined= random.choice
       and then give the list of str(nums). Now use append function to an variable with empty list(Acc_No)
       and then return the value 😊
    '''

    def add_account(self):
        def account(len):
            nums = ['1','2','3','4','5','6','7','8','9','0']
            Acc_No = []
            for x in range(1, len+ 1):
                joined = rd.choice(nums)
                Acc_No.append(joined)
            return ''.join(Acc_No)
        print(f'Your Account number is:-')
        print(f'RSTF-{account(8)}')
        
        
    '''

     Created a function to show balance in your account

    '''
    
    def Acc_created(self):
        print(f"{self.first_name} {self.last_name} your 0 Balance Account is succesfully created")

    def set_balance(self):
        self.balance = 10000
        return (f"{self.first_name} {self.last_name} has balance of {self.balance}")

    def deposite(self):
        d = int(input("Enter Deposit amount:"))
        if d % 100 == 0:
            total_balance = d + self.balance
            print(f"\nYour Updated Balance is:\n{total_balance}")
            
        else:
            print("Enter Amount like: 100,200,500,1000,2000")
            print("Please Try again")
        

    def Withdrawal(self):
        withdrawal = int(input("Enter Withdrawal Amount:\n"))
        if withdrawal % 100 == 0:
            total_balance = self.balance - withdrawal
            if total_balance >= 100:
                print('\nPlease wait while your treansaction being processing...\n')
                print(f"\nPlease Collect your amount:\n {withdrawal}")
                print(f"\nYour Total balance is:\n {total_balance}")

            else:
                print("\nInsufficient balance. Enter Less Amount !!!\n")
        else:
            print("\nEnter Amount like: 100,200,500,1000,2000\n")
            print("Please Try again")

    



        print('*********Thank you for choosing our RSTFBank**********')



'''
   Give the users asked parameters
   first_name,last_name,phone,email,Date_of_birth=0,
   address=0,Adhar_no=0,pancard_no=0,account_no=0,balance=0
   
'''
    
user1 = Customer('Sahil', 'Gupta',9945994299, 'guptasahil@gmail.com')

user1.login()
user1.add_email()
user1.add_address()
user1.add_adharcard()
user1.add_pancard()
user1.add_DOB()
user1.add_account()
user1.Acc_created()
user1.deposite()
user1.Withdrawal()
