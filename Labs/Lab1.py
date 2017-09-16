# IPython log file
# Problem 1 Solution
def problem_1():
    print("*********")
    for x in range(3):
        for y in range(5):
            if y % 2 == 0:
                print("")
            else:
                print("*\t*")
        print("*********")
# Problem 2 Solution        
def problem_2():
    lis = ['O', 'X', 'X', 'X', 'X', 'X', 'X']
    count = 1
    for x in range(len(lis) - 1):
        for y in lis:
            print(y, end='')
        print('')
        lis[count] = 'O'
        count += 1

# Problem 3 Solution
def problem_3():
    subscriptions = []
    print('Enter number of months for subscription:')
    months = int(input())
    print('Do you want Hulu ($8/month) [y = yes, anything else = no] :')
    hulu = input()
    print("Do you want Netflix ($10/month) [y = yes, anything else = no] :")
    netflix = input()
    print("Do you want Prime ($7/month) [y = yes, anything else = no] :")
    prime = input()
    total_monthly_cost = 0
    if hulu == 'y' or hulu == 'Y':
        total_monthly_cost = 8 * months
        subscriptions.append("Hulu")
    if netflix == 'y' or netflix == 'Y':
        total_monthly_cost += 10 * months
        subscriptions.append("Netflix")
    if prime == 'y' or prime == 'Y':
        total_monthly_cost += 7 * months
        subscriptions.append("Prime")
    if len(subscriptions) == 0:
        print("No monthly payments")
    elif len(subscriptions) == 1:
        print("Total cost for {} for {} months is {}".format(subscriptions[0], months, total_monthly_cost))
    else:
        p_string = "Total cost for "
        for x in range(len(subscriptions) - 1):
            p_string += subscriptions[x] + " " + "and "
        p_string += subscriptions[len(subscriptions) - 1]
        p_string += " for {} months is {}".format(months, total_monthly_cost)
        print(p_string)
                 
quit()
