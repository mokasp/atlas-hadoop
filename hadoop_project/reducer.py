#!/usr/bin/env python2.7
"""
    python script intended to be used as a reducer for a mapreduce job using
    Hadoop. it takes in lines from STDIN that were printed by the mapper,
    which containts the cleaned and formatted data from salaries.csv and 
    finds 10 the entries that contain the highest salaries

    
    Dependencies
    ------------

    Usage
    -----

    

"""
import sys
import re

# keep track of top salaries
top_salaries = []

# start line count
line_number = 0

# go through each each line from the mapper
for line in sys.stdin:

    # clean the lines of whitespaces
    line = line.strip()

    # we only need to work with the rows with data, not the labels
    if not line.startswith("id"):
        # split the line without storing an array
        employee_id, company, salary = re.split(r'\t|,', line)

        # first we need to populate the top salaries list until it is full
        if len(top_salaries) <= 9:

            # append the information about the first few companies to start
            # the process
            top_salaries.append((employee_id, company, salary))

            # each time the list is updated it needs to be sorted
            # to enable easy compaing
            top_salaries.sort(key=lambda x: int(x[2]), reverse=True)


        # once it has 10 elements we can start comparing salaries
        else:

            # check if the salaru of this current line is greater than the
            # smallest salary 
            if int(salary) > int(top_salaries[9][2]):
                top_salaries[-1] = (employee_id, company, salary)
                top_salaries.sort(key=lambda x: int(x[2]), reverse=True)

    # incremenmt the line counter
    line_number += 1

# sort the top salaries list one final time for good measure
top_salaries.sort(key=lambda x: int(x[2]), reverse=True)

# first print the labels
print('id\tSalary\tcompany')
# print each top salary in ascending order
for j in range(len(top_salaries)):
    print(top_salaries[j][0] + '\t' + str(float(top_salaries[j][2])) + '\t' + top_salaries[j][1])