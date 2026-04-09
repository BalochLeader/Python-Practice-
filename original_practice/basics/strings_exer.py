
username = input("Enter Your Username : ")

if (len(username)) > 12:
    print("You Need Short Username To Proceed")
elif  " " in username:
    print("Your UserName Contains Spaces ")
elif not username.isalpha():
    print("Your Number Must Be Doest Not contains Digit")
    

else:
    print(f"Your Username Meet All Requirements : {username}")