# HW01_ex01_04
# Start the Python interpreter and use it as a calculator. 
# Python's syntax for math operations is almost the same as 
# standard mathematical notation. For example, the symbols 
# +, - and / denote addition, subtraction and division, as you would expect. 
# The symbol for multiplication is *.

# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your 
# average time per mile? What is your average speed in miles per hour? 
# (Hint: there are 1.61 kilometers in a mile).
# Average Speed in MPH:

raceKM = 10 # race distance in kilometers
raceMiles = raceKM / 1.61 # race distance in miles
raceTime = 43.5 # time to complete race in minutes

avgTimePerMile = raceTime / raceMiles # determining the average time per mile
print "Average time per mile:", avgTimePerMile, "minutes."

avgMPH = 60 / avgTimePerMile # compute speed in miles per hour
print "Average speed in miles per hour:", avgMPH, "MPH."