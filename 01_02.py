thefilepath = "01_02_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

final_digits = []
text_digit_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
text_locations = []

#Start processing each line:
for i, line in enumerate(file_list):
    ordered_digits = [] 

    #Get location of all/any text-digits in line:
    for p, text_digit in enumerate(text_digit_list):
        text_digit_location = line.find(text_digit) # returns index of a string within a line
        if text_digit_location >-1:
            digit_with_location = (text_digit_location,p+1) # bring location and digit_text together
            ordered_digits.append(digit_with_location) # add those to a list
      
    #Get location of all integer digits in line:
    for c, char in enumerate(line):
        if char.isdigit():
            digit_location = c   # line.find(char) just doesn't work to return position of digits
            digit_with_location = (digit_location,int(char)) # bring location and digit together
            ordered_digits.append(digit_with_location) # add those to list
    
    #final processing for line:
    sorted_digits = sorted(ordered_digits) # sort the list (lowest location first)      
    print("Line: ",i+1, "orderd_digits: ", sorted_digits)

    digit_pair = (str(sorted_digits[0][1]),str(sorted_digits[-1][1])) # bring first and last digits together
    joined_pair = "".join(digit_pair)
    final_digits.append(joined_pair) # add pairs to a list


#Add all pairs of digits together:
print(final_digits) #check contents of final_digits

cumulative_total = 0

for value in final_digits:
    cumulative_total += int(value)

print(cumulative_total)
