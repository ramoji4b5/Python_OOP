"""
Till now, we’re working with an example of one student. In the problem statement,
it’s defined that we’ve to perform this same task (which we did above) for ‘n’ number of students.

Say, if n = 10, one way to implement it is that we repeat our code ten times and add an additional
if condition to monitor the current value of the student.
"""

#########################Optimized Code #########################################################
students_arrival_time = [9, 25, 39, 45, 9, 75, 84, 2, 18, 13]

student_counter = 0

while student_counter < 10:
    if students_arrival_time[student_counter] == 9:
        print("On time")

    elif students_arrival_time[student_counter] > 9 and students_arrival_time[student_counter] <= 19:
        print("10 minutes late")

    elif students_arrival_time[student_counter] > 19 and students_arrival_time[student_counter] <= 39:
        print("30 minutes late")

    else:
        print("Zero marks")
    student_counter += 1

###########################################Basic flow idea####################################
# students_arrival_time = [9, 25, 39, 45, 9, 75, 84, 2, 18, 13]
#
# student_counter = 0
#
# if student_counter == 0:
#     if students_arrival_time[student_counter] == 9:
#         print("On time")
#         student_counter += 1
#
#     # all conditional statements here…
#
# if student_counter == 1:
#     if students_arrival_time[student_counter] == 9:
#         print("On time")
#         student_counter += 1
#
#     # all conditional statements here...
# if student_counter == 2:
#     if students_arrival_time[student_counter] == 9:
#         print("On time")
#         student_counter += 1
# # all conditional statements here

