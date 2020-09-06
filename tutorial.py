def instagram_data_usuage():
    # input how many hours we have used on instagram 
    # input how many data does instgram use per hour 
    hours = input("how many hours per day do you spend on instagram?")
    data_plan = input("how much data is on your month phone plan?")
    print(type(hours))
    print(type(data_plan))
    print(hours)
    print(data_plan)
    hours= int(hours)
    print(type(hours))
    data_plan=int(data_plan)
    print(type(data_plan))
# we copy it again just to cross check my answer, to prove it if its converted to an integer 
    result = data_plan * hours
    print("result", result)
    # more readable for the user
instagram_data_usuage()
# we dont want to put anything in there because we want to get the input from the user
    # per hour 100MB

# we need use colon everytime we start a function 
# our function takes two inputs
# we need to inputs to calculate how many total MB we spent in total
# variable is result 
