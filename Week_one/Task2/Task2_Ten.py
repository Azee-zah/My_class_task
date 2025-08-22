School_name = input("Tell us your school name: ")
Tuition_fee = float(input("How much is your tuition? "))
Hostel_fee = float(input("How much is the hostel fee? "))
Feeding_fee = float(input("How much is the feeding fee? "))
Total_fee = Tuition_fee * Hostel_fee * Feeding_fee
print(f"     Student fee\nTuition\t{Tuition_fee}\nAccommodation\t {Hostel_fee}\nFeedind\t {Feeding_fee}\nGrand total\t {Total_fee}")