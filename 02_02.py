import math

thefilepath = "02_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

#initialise max no. of cubes allowed:
max_red = 12
max_green = 13
max_blue = 14
possible_games = []
colour_power_sum = 0

for g, game in enumerate(file_list):
    
    all_blue_cubes = []
    all_red_cubes = []
    all_green_cubes = []
    
    
    no_title_game = game.split(":")[1] # remove 'Game 1:' title
    #for h, handful in enumerate(game.split(";")):
    for h, handful in enumerate(no_title_game.split(";")): # split into handfuls
        #print("game:",g+1, " handful:",h+1, " cubes:", handful )

        # This part would FAIL MISERABLY if there is any inconsistent formatting / spaces in the input!!  
        # There is a better way not using indexes probably
        blue_cubes = handful.split(" blue")[0]
        blue_cubes = blue_cubes.split(" ")[-1]
        if not blue_cubes.isdigit(): blue_cubes = 0 
        red_cubes = handful.split(" red")[0]
        red_cubes = red_cubes.split(" ")[-1]
        if not red_cubes.isdigit(): red_cubes = 0 
        green_cubes = handful.split(" green")[0]
        green_cubes = green_cubes.split(" ")[-1]
        if not green_cubes.isdigit(): green_cubes = 0

        #Add no of cubes in each handful to a master list for each colour:
        #print("blue cubes:",blue_cubes)
        all_blue_cubes.append(int(blue_cubes))
        #print("red cubes:",red_cubes)
        all_red_cubes.append(int(red_cubes))
        #print("green cubes:",green_cubes)
        all_green_cubes.append(int(green_cubes))

    # Calculate minimum cubes required for this game:
    min_blue = max(all_blue_cubes)
    min_red = max(all_red_cubes)
    min_green = max(all_green_cubes)

    colour_power = (min_blue*min_red*min_green)
    print("game:",g+1, "min red:",min_red, "min blue:",min_blue, "min green:",min_green,"Product / Power:", colour_power)

    colour_power_sum += colour_power

print("Final colour power sum:", colour_power_sum)


