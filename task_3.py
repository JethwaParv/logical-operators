# Compulsory Task 1
# Input function asking the user for time taken to complete each task in minutes for the Triathlon.

swimming = int(input('Please input the time taken to complete swimming: '))
cycling = int(input('Please input the time taken to complete cycling: '))
running = int(input('Please input the time taken to complete running: '))

# assigned variable.

qualifying_time = 100

# Calculating total time taken to complete all triathlon activities
# ARITHMETIC operator used to calculate.
total_time_taken = swimming + cycling + running
print('Total time taken to complete triathlon: ', total_time_taken)

# Comparison operators used to allocate awards.
if total_time_taken <= 100:
    print('Congratulations you have been awarded the Provincial colours.')
elif 100 < total_time_taken <= 105:
    print('You have been awarded Provincial Half Colours')
elif 105 < total_time_taken <= 110:
    print('You have been awarded a Provincial Scroll')
else:
    print('You have failed to secure an award')



