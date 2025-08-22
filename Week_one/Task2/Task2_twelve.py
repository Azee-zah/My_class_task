print("Welcome to Safe bank !, we are pleased to have you")
USSD_code = "*908#"
Dial_USSD = input(f"Dial {USSD_code} to proceed ")
print("1.Purchase data\n2.Purchase airtime\n3.Check account balance")
order = int(input("Enter your option: "))
if order ==1: {
    print("1== 10GB\n2==20GB\n3==30GB")
}
if order == 2: {
        print("1==#200\n2==#200\n3==#300")
}
a = int(input("Enter amount"))   
print("Your transaction is being processed, Thank you for banking with us")
