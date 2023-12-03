thefilepath = "01_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

first_digits = []
last_digits = []
final_digits = []

#Get first digits:
for line in file_list:
    #digits.append(line[0])
    #digits.append(line[-1])
    for char in line:
        if char.isdigit():
            first_digits.append(char)
            break

    #print(first_digits)

#Get last digits:
for line in file_list:
    #digits.append(line[0])
    #digits.append(line[-1])
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
