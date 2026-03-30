import CleanData as clean
import Descript_Stats as descr_stats


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
    
    
    filtered_data, removed_values = clean.clean_heartrate_data(data) #Here, we're calling the clean_heartrate_data function by creating 2 variables to get the returned info.
    
    print(f'\n\tClean Data: ', filtered_data, f'\n\n\tNumber of rows that could not be processed: {removed_values}') #printing clean data list & number of rows of erroneous data
    
    
    med = descr_stats.median(data)
    print(f'\n\tMedian of HR: ', f'{med:.2f}')
    
    range_of_hr = descr_stats.range(data) #calling range function by assigning it to a variable.
    print(f'\n\tHR Range: ', f'{range_of_hr:.2f}')
    
    
    avg = descr_stats.average(data) #calling average function by assigning it to a variable
    print(f'\n\tAvg heart rate: ', f'{avg:.2f}')
    
    roll_avg = descr_stats.rolling_avg(data, 5)
    print(f'\n\n\tRolling Average: ', roll_avg)
    
    # calculate the average, median, and range of this file using the functions you've wrote
    
    var = descr_stats.variance(data)
    print(f'\n\tHR Variance: ', f'{var:.2f}')

    challenge = descr_stats.variance_challenge(data)
    print(challenge)

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
