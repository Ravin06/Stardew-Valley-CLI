game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
}
 
seed_list = ['LET', 'POT', 'CAU']

seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}
farm = [ [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, 'House', None, None],
         [None, None, None, None, None],
         [None, None, None, None, None] ]

def show_stats(game_vars):
    width = 50  # total width of the box
    print(f"+{'-' * width}+")
    day_line = f" Day {game_vars['day']}      Energy: {game_vars['energy']}      Money: ${game_vars['money']}"
    print(f"|{day_line:<{width}}|")
    # Filter seeds with quantity greater than 0
    available_seeds = [seeds[seed]['name'] for seed, qty in game_vars['bag'].items() if qty > 0]
    if not available_seeds:
        no_seeds_line = " You have no seeds."
        # Print the line with the width of the box
        print(f"|{no_seeds_line:<{width}}|")
    else:
        seeds_line = "You have the following seeds: "
        # Join the list of seeds with a comma and space
        seeds_content = ", ".join(available_seeds)
        full_seeds_line = seeds_line + seeds_content
        # Print the line with the width of the box
        print(f"|{full_seeds_line:<{width}}|")
    print(f"+{'-' * width}+")
    pass

def in_town(game_vars):
    show_stats(game_vars)
    print("You are in Albatross Town")
    print(f"{'-'*25}")
    print("1) Visit the shop")
    print("2) Visit the farm")
    print("3) End the day")
    print()
    print("9) Save the game")
    print("0) Exit the game")
    print(f"{'-'*25}")

def in_shop(game_vars):
    while True:
        print("Welcome to Pierce's Seed Shop!")
        show_stats(game_vars)
        print("What do you wish to buy?")
        print(f"{'Seed':<12} {'Price':<10} {'Days to Grow':<7} {'Crop Price':<10}")
        print("-" * 50)
        #create a list of available seeds
        for i, seed in enumerate(seed_list, 1): #The enumerate function adds a counter to "seed_list", starts from 1
            '''
            Example of enumerate:
            seed_list = ['apple', 'banana', 'cherry']
            for i, seed in enumerate(seed_list, 1):
                print(i, seed)
            Output:
            1 apple
            2 banana
            3 cherry
            '''
            #display the available seeds, their price, growth time and crop price
            print(f"{i}) {seeds[seed]['name']:<12} {seeds[seed]['price']:<10} {seeds[seed]['growth_time']:<12} {seeds[seed]['crop_price']:<10}")
        print("0) Leave")
        print("-" * 50)
        choice = input("Your choice? ")
        if choice == "0":
            break
        #Validation
        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue
        choice = int(choice)
        if choice < 0 or choice > len(seed_list):
            print("Invalid choice. Please select a valid option.")
            continue
        if choice == 0:
            break
        seed = seed_list[choice - 1]
        price = seeds[seed]['price']
        qty = input("How many do you wish to buy? ")
        #More Validation
        if not qty.isdigit():
            print("Invalid quantity. Please enter a positive number.")
            continue
        qty = int(qty)
        if qty <= 0:
            print("Invalid quantity. Please enter a positive number.")
            continue
        total_cost = price * qty
        if game_vars['money'] >= total_cost:
            if seed in game_vars['bag']:
                game_vars['bag'][seed] += qty
            else:
                game_vars['bag'][seed] = qty
            game_vars['money'] -= total_cost
            print(f"You bought {qty} {seeds[seed]['name']} seed(s).")
        else:
            print("You don't have enough money.")

def draw_farm(farm, farmer_row, farmer_col, energy):
    #Iterate through each row in the farm
    for row in range(len(farm)):
        #Top boundary
        print('+-----' * len(farm[row]), end='+\n')
        
        #Iterate through each cell in the current row to print the top content
        for a in farm[row]:
            try:
                if 'House' != a: #If the cell is not the house
                    print(f'| {a[0]:<3} ', end='') #Print the abbreviation of the crop
                else:
                    print(f'| HSE ', end='')  #print house
            except TypeError:
                print('|     ', end='') #Print an empty cell if no crop is planted
        print('|') #Closing the row

        #Iterate again to print the middle row content
        for b in range(len(farm[row])):
            if b == farmer_col and row == farmer_row:
                print('|  X  ', end='') #Print X if the player is in this cell
            else:
                print('|     ', end='') #Print empty cell otherwise
        print('|') #Closing the row

        #Iterate once more to print the bottom row content
        for a in farm[row]:
            try:
                if 'House' != a: #If cell is not the house
                    print(f'|  {a[1]:<2} ', end='') #Print the days left for the crop to grow
                else:
                    print('|     ', end='') #Print an empty space for the house
            except TypeError:
                print('|     ', end='') #Print an empty cell if no crop is planted
        print('|') #Close the row
    print('+-----' * len(farm[row]), end='+\n') #Bottom boundary


    print(f'Energy: {energy}')
    print('[WASD] Move')
    #isinstance() function returns True if the specified object is of the specified type, otherwise False
    #checks if the object is a list and the number of days is 0, if so, it allows the player to harvest the crop
    if isinstance(farm[farmer_row][farmer_col], list) and farm[farmer_row][farmer_col][1] == 0: #if number of days is 0
        print("H)arvest crop")
    print('P)lant seed')
    print('R)eturn to Town')
    print('Your choice?')


def move(farmer_row, farmer_col, move_choice):
    #Check if the move choice is 'w' (move up) and the farmer is not at the top row
    if move_choice.lower() == 'w' and farmer_row > 0:
        farmer_row -= 1
     #Check if the move choice is 's' (move down) and the farmer is not at the bottom row
    elif move_choice.lower() == 's' and farmer_row < 4:
        farmer_row += 1
    #Check if the move choice is 'a' (move left) and the farmer is not at the leftmost column
    elif move_choice.lower() == 'a' and farmer_col > 0:
        farmer_col -= 1
    #Check if the move choice is 'd' (move right) and the farmer is not at the rightmost column
    elif move_choice.lower() == 'd' and farmer_col < 4:
        farmer_col += 1
    #Return new position
    return farmer_row, farmer_col

def plant_seed(farm, farmer_row, farmer_col):
    #Check if the cell is the house, if so dont allow user to plant
    if farm[farmer_row][farmer_col] == 'House':
        print("You cannot plant here. This is your house.")
        return
    
    #create a dictionary of available seeds
    available_seeds = {seed: qty for seed, qty in game_vars['bag'].items() if qty > 0}
    if not available_seeds:
        print("You don't have any seeds to plant.")
        #return to the main menu
        return
    print("What do you wish to plant?")
    print(f"{'-'*40}")
    print(f"{'Seed':<12} {'Days to Grow':<12} {'Crop Price':<12} {'Available':<12}")
    print(f"{'-'*40}")
    #create a list of available seeds
    seed_list = list(available_seeds.keys())
    #display the available seeds
    for i, seed in enumerate(seed_list, 1):
        print(f"{i}) {seeds[seed]['name']:<12} {seeds[seed]['growth_time']:<12} {seeds[seed]['crop_price']:<12} {available_seeds[seed]:<12}")
    print("0) Leave")
    print(f"{'-'*40}")
    choice = input("Your choice? ")

    if choice == "0":
        return
    elif choice.isdigit() and 1 <= int(choice) <= len(seed_list):
        seed = seed_list[int(choice) - 1] #get the seed from the list
        game_vars['bag'][seed] -= 1 #reduce number of seeds by 1
        #The code [seeds[seed]['name'][:3].upper(), seeds[seed]['growth_time']] creates a list containing two elements: the first three uppercase letters of the seed's name and the growth time of the seed
        farm[farmer_row][farmer_col] = [seeds[seed]['name'][:3].upper(), seeds[seed]['growth_time']] #add the seed to the farm
        print(f"You planted a {seeds[seed]['name']} seed.")
    else:
        print("Invalid choice. Please select a valid option.")
