#!/usr/bin/env python2.7
""" 
    python script intended to be used as a mapper for a mapreduce job using Hadoop
    it takes in lines from STDIN printed from salaries.csv, cleans the data by
    skipping duplicates and NaN values, and reformats the data by only id,
    company, and totalyearlysalary to be streamed to the reducer

    this script does not assume that the whole file is being inputted together.
    hadoop may split the data into 2 or more batches, so the script checks the
    starting id

    Dependencies
    ------------

    Usage
    -----

"""
import sys


# keep track of the line numbers so we can take care of duplicates
line_number = 0

# extract the first line in order to know where to start
# this is needed because hadoop may split this map job into
# two runs, so the data may be split and out of order
first_line = sys.stdin.readline().rstrip()
first_line = first_line.strip().split(',')

# if this is the first portion of the data, then the first line
# will contain the column names. in this case the previous id should be 0
# as the starting id will be 1
if first_line[0] == 'id':
    previous_id = 0
# if the first line is not id, we need to make sure the
# previous id aligns with the starting id
else:
    previous_id = int(first_line[0]) - 1


# iterate through each line
for line in sys.stdin:

    # clean up the line of white spaces and seperate by comma
    line = line.strip()
    cleaned_line = line.split(',')

    # extract current id
    employee_id = cleaned_line[0]

    # if this is not the first line we need to make sure the id can
    # be converted to an int for further comparing
    if employee_id != 'id':
        try:
            int(employee_id)
        # if it cannot be converted to an int we will just skip this line
        except ValueError:
            continue

    # incrememnt the line counter
    line_number += 1

    # skipping many duplicates. there are so many
    if line_number < 2163 or previous_id != int(employee_id) - 1:
        continue

    # extract the company name
    company = cleaned_line[1]

    # some of the compensations listed are NaN so we need to set
    # those to 0 so they can be compared with ints
    try:
        compensation = cleaned_line[3]
    except IndexError:
        compensation = '0'

    # handling problematic lines where columns are out of order
    # and removing any apostrophy
    if employee_id == '5808':
        company = 'Bank of America Merill Lynch'
        compensation = '132000'
    elif employee_id == '55811':
        company = "Macys"
        compensation = '150000'
    elif employee_id == '56931':
        company = "Macys"
        compensation = '150000'
    elif employee_id == '57088':
        company = "Macys"
        compensation = '138000'
    elif employee_id == '57985':
        company = "Macys"
        compensation = '115000'
    elif employee_id == '58927':
        company = "Macys"
        compensation = '125000'

    # print the id, company, and salary in the specified format
    if previous_id == 0:
        print('id\ttotalyearlysalary,company')
    print(employee_id + '\t' + company + ',' + compensation)

    # increment the previous id
    previous_id += 1