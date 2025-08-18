# define the sem_att as a set
#range to specify number of attendees
#use for in and range to specify the numbers when collecting names
# use .add to put all names in the set
#use ssorted for alphabetical order
seminar_attendees = set()
number_of_attendees = range(5)
for i in range(5):
    attendees = input(f"Enter your name here {i+1}: ")
    seminar_attendees.add(attendees)
alphatical_order = sorted(seminar_attendees)
all_sem_attenddee = set(alphatical_order)
print(all_sem_attenddee)

