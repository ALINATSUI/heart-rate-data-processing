import statistics as stats
import CleanData as clean
#import matplotlib.pyplot as plt


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    filtered, bad_values = clean.clean_heartrate_data(data)
    new_filtered = list(filtered) #converting clean list type from tuple to list.
    avg_hr = stats.mean(new_filtered) 
    return avg_hr 
   
def median(data: list) -> float:
    
    filtered, bad_values = clean.clean_heartrate_data(data) #Calling clean_heartrate_data for filtered list
    new_filtered = list(filtered) #converting tuple to list 
    hr_median = stats.median(new_filtered)
    return hr_median   

def range(data: list) -> float:

    filtered, bad_values = clean.clean_heartrate_data(data) #Here, we're calling the clean_heartrate_data and creating two variables so we can use the clean data list. 
    
    
    new_filtered = list(filtered)
    hr_min = min(new_filtered) #variable for heart rate minimum
    hr_max = max(new_filtered)#variable for heart rate maximum
    hr_range = hr_max - hr_min #formula to calculate range
    return hr_range # returning Range value

def variance(data: list):
    filtered, bad_values = clean.clean_heartrate_data(data) #Here, we're calling the clean_heartrate_data and creating two variables so we can use the clean data list. 
    
    new_filtered = list(filtered)
    hr_variance = stats.variance(new_filtered)
    return hr_variance

def rolling_avg(data: list, k: int) -> float:
#     """
#     CHALLENGE FUNCTION (Optional)
#     """
    filtered, bad_values = clean.clean_heartrate_data(data) #calling filtered list from clean_heartrate_data function
    k = 5 # heartrate data was recorded in 5 minute intervals. 
    filtered_list = list(filtered)
    for i in filtered_list: #to get rolling average, we take each number in list and divide by 5.
        roll_avg = i/k
    return roll_avg    

#def plot(data: list):
    #fig, ax = plt.subplots() 


