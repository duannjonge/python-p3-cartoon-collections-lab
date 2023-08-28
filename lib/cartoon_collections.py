# def roll_call_dwarves(dwarves):
#     for i,dwarf in  enumerate(dwarves,1):
#         print(f"{i}.{dwarf}")

# roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

def roll_call_dwarves(dwarves):
    index = 1
    for dwarf in dwarves:
        print(f"{index}. {dwarf}")
        index += 1
   
roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

def summon_captain_planet(planeteer_calls):

    new_item=[f'"{plane.upper()}!"'for plane in planeteer_calls]
    return new_item



summon_captain_planet(["earth", "wind", "fire", "water", "heart"])

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True  # If any call is longer than 4 characters, return True
    return False  # If no call is longer than 4 characters, return False

def find_the_cheese(items):
    cheese = ["cheddar","gouda","camembert"]
    for item in items:
        if item in cheese:
            return item

    else:
        None
