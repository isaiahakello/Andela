def find_max_min(my_list):
    # check to ensure variables in least are equal
    if all(x == my_list[0] for x in my_list):
        other_list = [len(my_list)]
        # returns length of list
        return other_list
    else:
        maxim = max(my_list)  # find maximum value
        minim = min(my_list)  # find minimum value
        # adding maximum and minimum  values to a list and returning the list
        maxmin = [minim, maxim]
return maxmin