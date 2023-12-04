thefilepath = "01_02_Data_Test.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

first_digits = []
last_digits = []
final_digits = []

text_digit_set = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}

text_locations = []


#Get location of all/any text-digits in line:
for i, line in enumerate(file_list):
    #print("LINE: ", i+1)
    for text_digit in text_digit_set:
        text_digit_location = line.find(text_digit)
        if text_digit_location >-1:
            print("line: ", i+1, "digit:", text_digit, "location: ", text_digit_location)
            #store text_digit and text_digit_location pairs (dictionary?   List of lists?)




#Get all digit locations:
for r, line in enumerate(file_list):
    for char in line:
        if char.isdigit():
            digit_location = line.find(char)
            print("line: ",r+1, "digit:",char, "location: ", digit_location )
            #first_digits.append(char)
            #break


#Now read all the info into a list of lists or multi dimensional array(?)



#Then just find which value exists for the earliest and latest locations in each line.abs




"""
#Get last digits:
for line in file_list:
    for char in reversed(line):
        if char.isdigit():
            last_digits.append(char)
            break

    #print(last_digits)


for i,number in enumerate(first_digits):
    sum = number + last_digits[i]
    final_digits.append(sum)

#print(final_digits)

#Add up all final values:

cumulative_total = 0

for value in final_digits:
    cumulative_total += int(value)

print(cumulative_total)
    
    



#print (digits)
"""