def time(hour,minute):
    hour = int(hour)
    minute = int(minute)
    if hour>1 and hour<23 and minute>1 and minute<59:
        if hour > 12:
            hour = hour - 12
            print(f"{hour} : {minute} Pm")
        else:
            print(f"{hour} : {minute} Am")
    
        
    else:
        print('I can not understand')

hour = input('Enter hour : ')
minute = input('Enter minute : ')

time(hour,minute)
