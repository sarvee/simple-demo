from Utility.UI import Menus
import Loginfunction
import SignUp, ForgetPassword
#this is a dummy welcome function which is used to call welcome again from any other module

def welcome():
    end=False

    while(end==False):
        choice = Menus.display_main_menu('Welcome to PySpace','Login,Sign Up,Forget Password,Exit')
        if(choice.isdigit() and (int(choice)>=1 and int(choice)<=4)):
            if(int(choice)==1):
                Loginfunction.login()
                end=True
                #ViewFunctions.view_product()
            if(int(choice)==2):
                SignUp.signup()
            
            if(int(choice)==3):
                ForgetPassword.forget_password() 
                end=True
                break   
    #     
            if(int(choice)==4):
                print("Thank you!")
                end=True
                break
        else:
            print("Please enter a valid option ( 1,2,3 )")