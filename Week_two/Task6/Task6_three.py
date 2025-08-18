# store the seat numbers in a set
# collect the booked seat from user using input
seat_num = set(range(1,51))
book_a_seat =int((input("Enter yout seat number here: ")))
removed = seat_num.remove(book_a_seat)
print("Removed:", book_a_seat)
print("Remaining:", seat_num)