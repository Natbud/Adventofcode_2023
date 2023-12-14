import numpy as np

thefilepath = "03_01_Data_Test.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

# Get the size of file_list to help with creating numpy array of same size.
# rows:
file_list_row_len = (len(file_list))
# columns:
file_list_col_len = (len(file_list[0]))

# Create a numpy array (for original given grid values) of same size as file_list and add all zeroes:
np_grid = np.zeros((file_list_row_len,file_list_col_len))

# read in all the values from file_list into np_grid array
for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        if digit == ".":
            digit = -1
        elif not digit.isalnum():
            digit = -2
        
        np_grid[r][d] = digit
print("np_grid:\n", np_grid)



