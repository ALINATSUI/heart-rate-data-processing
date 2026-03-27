

def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    separator_string = ","
    convert_list_to_string = separator_string.join(data) # changes list into string

    
    remove_n = convert_list_to_string.replace('\n','') #using replace method to replace '\n' with an empty string so we can start data clean. 
    
    good_values = [] #empty list to place cleaned data in while keeping original data input as is. 
    
    
    count = 0 #creating count variable to keep track of nondigit character in the row.
    new_list = remove_n.split(",") #calling the list with removed \n characters and adding a comma between the values
    
    for hr in new_list: #for loop to check whether a character is a digit. If it is, we append the digit to empty list (good_values variable).
        if hr.isdigit():
            clean_values = int(hr)
            good_values.append(clean_values)
        else: #otherwise, if the list contains a non-digit character, we increase the count and filter it out of the list.
            count += 1
    
    return good_values, count #Once the for loop runs, we're returning the clean data list and count of data rows that could not be processed