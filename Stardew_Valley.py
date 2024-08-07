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
