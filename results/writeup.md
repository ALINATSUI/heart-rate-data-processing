1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

phase1's file appears to represent the most active period by comparing the Median(88.5) and Average heart rate(87.30). Both figures are pretty close to each other which is what we would expect since median would represent the number that appears most in the middle of the data. 

Comparing phase1's data to the "Target HR Zone 50-85%", the individuals in our study came a bit under the target zone. 

2) Which file had the **poorest** data quality? How do you know?
I would have to say that phase2 file had the poorest data quality due to the large range. Out of all the files, phase2's range was the widest. 
...

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
Range = Max - Min
Range = Max(180) - Min(68)
Range = 112




median = 72


b) Explain how the extreme value affects the range.

The range (112) is wider than all the numbers (except for the glitch). We also see that this range is pretty wide-casting and suggesting a large difference between the min and max values (volatility). 

If we omit the value 180 when calculating the range, the new range would be 7. This is a much smaller range (represents a more stable heart rate) than when we calculated the range with sensor glitch. 

Modified Range  = Max - Min
                = 75 - 68
                = 7


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

Some other statistics may be: age, income level to account for the variability of dataset. For income level, I would think that someone in a higher income level bracket would have the economic resources to focus on living a more healthy lifestyle (working out, eating well, managing stress) which could then lead to a more desirable HR.
