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
    

    
    
def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    filtered, bad_values = clean_heartrate_data(data) #calling clean_heartrate_data function to calculate average.

    # print(filtered, bad_values)
    total = 0   #creating counter
    new_filtered = list(filtered) #converting clean list type from tuple to list.
    
    for num in new_filtered: #for loop to add each digit in list and divide by length of number of elements in list to calculate average.
        total += num
        avg_hr = total/len(new_filtered)
    return avg_hr #return average hr 

   
        
def median(data: list) -> float:
    
    
    filtered, bad_values = clean_heartrate_data(data) #Calling clean_heartrate_data for filtered list
    
    new_filtered = list(filtered) #converting tuple to list 
    # print(f'\nFiltered List: ', new_filtered)

    sorted_HR_values = sorted(new_filtered) #sorting filtered list 
    print(f'\nSorted Values: ', sorted_HR_values)

    len_lst = len(new_filtered) # Number of elements in clean data

    if len_lst % 2 == 0: #if number of elements in filtered list is even
        index_pos_2 = int(len_lst/2) # dividing length of list in half and typecasting to integer.
        index_pos_1 = (index_pos_2) - 1 #taking halved list and subtracting one to account for zero-index.
        median_hr = (sorted_HR_values[index_pos_2] + sorted_HR_values[index_pos_1])/2 #for even number of datapoints, taking the average of 2 even numbers in the middle

    else: #if number of elements in filtered list is odd
        index_pos = (len_lst - 1 ) / 2 # number of elements in list minus 1(to account for zero index) and divide by half
        for index,value in enumerate(sorted_HR_values):#setting 2 variables in enumerate function.
            if index == index_pos: # if index element is equal to index_pos variable  
                median_hr = value #then, make value of element equal to median_hr variable.
    
    return median_hr 
    
            


def range(data: list) -> float:
#     """
#     """
    filtered, bad_values = clean_heartrate_data(data) #Here, we're calling the clean_heartrate_data and creating two variables so we can use the clean data list. 
    # print(f'\nFiltered Data: ', filtered)
    hr_min = min(filtered) #variable for heart rate minimum
    
    hr_max = max(filtered)#variable for heart rate maximum
    
    hr_range = hr_max - hr_min #formula to calculate range
    
    return hr_range # returning Range value

def rolling_avg(data: list, k: int) -> float:
#     """
#     CHALLENGE FUNCTION (Optional)
#     """
    filtered, bad_values = clean_heartrate_data(data) #calling filtered list from clean_heartrate_data function
    k = 5 # heartrate data was recorded in 5 minute intervals. 
    filtered_list = list(filtered)
    for i in filtered_list: #to get rolling average, we take each number in list and divide by 5.
        roll_avg = i/k
    return roll_avg    

    
   


def run(file: str):
    
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    

    data = [] #empty list
    object = open(file, 'r') #creating a file object and opening file (parameter)
    file_object = object.readlines() #accessing all the lines in the file object

    for line in file_object: #for each line of file, we're adding them to the empty data list.
        data.append(line)
        
    object.close()
    line = '_' #to make output more visually appealing
    print(line*70)
    print(f'\n\nFILE : ', file) #added name of file to make the output easier to read.
    
    
    filtered_data, removed_values = clean_heartrate_data(data) #Here, we're calling the clean_heartrate_data function by creating 2 variables to get the returned info.
    
    print(f'\n\tClean Data: ', filtered_data, f'\n\n\tNumber of rows that could not be processed: {removed_values}') #printing clean data list & number of rows of erroneous data
    
    med = median(data)
    print(f'\n\tMedian of HR: ', med)
    
    range_of_hr = range(data) #calling range function by assigning it to a variable.
    print(f'\n\tHR Range: ', float(range_of_hr))
    
    
    avg = average(data) #calling average function by assigning it to a variable
    print(f'\n\tAvg heart rate: ', f'{avg:.2f}')
    
    roll_avg = rolling_avg(data, 5)
    print(f'\n\n\tRolling Average: ', roll_avg)
    

    # calculate the average, median, and range of this file using the functions you've wrote
    

    # print out your data quality measure to the console
    

    # print out your descriptive statistics to the console
    


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

