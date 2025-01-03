def func(strings_list) :
    count = 0
    for string in strings_list :
        if string == "++" :
            count+=1
        elif string == "--" :
            count-=1
        else :
            raise ValueError("invalid input")
    
    return count



my_list = ["++", "++", "--", "++"]
print(func(my_list))