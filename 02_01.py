thefilepath = "02_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]   #strips out the /n character from each line

#initialise max no. of cubes allowed:
max_red = 12
max_green = 13
max_blue = 14
possible_games = []

for g, game in enumerate(file_list):
    no_title_game = game.split(":")[1] # remove 'Game 1:' title
    #for h, handful in enumerate(game.split(";")):
    for h, handful in enumerate(no_title_game.split(";")): # split into handfuls
        print("game:",g+1, " handful:",h+1, " cubes:", handful )

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

        print("blue cubes:",blue_cubes)
        print("red cubes:",red_cubes)
        print("green cubes:",green_cubes)



        if int(blue_cubes) <= max_blue and int(red_cubes) <= max_red and int(green_cubes) <= max_green:
            game_possible = 1
        else:
            game_possible = 0
        
        if game_possible == 1:
            print("\nGame",g+1,"is possible\n")
            
        else:
            print("\nGame",g+1,"is NOT possible\n")
            break #stop checking handfuls if game is NOT possible:

        
    #After handfuls checked  - final game possible check
        
    if game_possible == 1: possible_games.append(g+1)


print("possible games:",possible_games)


#Add all Possible Game IDs:
game_id_sum = sum(possible_games)
print("Final possible game ID Sum:",game_id_sum)




