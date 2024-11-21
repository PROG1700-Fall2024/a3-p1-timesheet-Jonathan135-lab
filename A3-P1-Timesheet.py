#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    hours_worked = []
    num_days = 5

    for i in range(num_days):
        hours = int(input(f"Enter the number of hours worked on Day #{i + 1}: "))
        hours_worked.append(hours)

    max_hours = max(hours_worked)
    max_day = hours_worked.index(max_hours) + 1 
    print("---------------------------------------------------------------------------")
    print(f"The most hours worked was on: ")
    print(f"Day #{max_day} when you worked {max_hours} hours")

    total_hours = sum(hours_worked) 
    average_hours = total_hours/num_days
    working_hours_less_than_7 = []
    working_days = []
    for i in range(num_days):
        if float(hours_worked[i]) < 7.0:
            working_hours_less_than_7.append(hours_worked[i])
            working_days.append(i + 1)

    total_hours = sum(hours_worked) 
    average_hours = total_hours/num_days

    print("-" * 75)
    print(f"The total number of hours worked was: {total_hours}")
    print(f"The average number of hours worked each day was: {average_hours:.1f}")
    print("-" * 75)
    print("Days you slacked off (i.e. worked less than 7 hours):")

    for i, hours in enumerate(working_hours_less_than_7):
         print(f"Day #{working_days[i]}: {hours} hours")

    # YOUR CODE ENDS HERE

main()