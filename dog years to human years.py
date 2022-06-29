def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)
        if d_age == 0:
            human_age = 0
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 0 < d_age <= 1:
            human_age = d_age * 15
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 1 < d_age <= 2:
            human_age = d_age * 12
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 2 < d_age <= 3:
            human_age = d_age * 9.3
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 3 < d_age <= 4:
            human_age = d_age * 8
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 4 < d_age <= 5:
            human_age = d_age * 7.2
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        elif 5 < d_age :
            human_age = (5 * 7.2) + ((d_age - 5) * 7)
            print ('The given dog age ', d_age , 'is', round (human_age, 2) , 'in human years')
        else:
            print('age cannot be a negative number')
 
        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        # your code here
        

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function
