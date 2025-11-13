"""
$ python pizza.py

PIZZA PARTY CALCULATOR

How many people are coming? 8
How hungry are they?
1. Light eaters (2 slices per person)
2. Normal appetite (3 slices per person)  
3. Very hungry (4 slices per person)
Choose appetite level (1-3): 2

What size pizzas?
1. Small (6 slices, $8.99)
2. Medium (8 slices, $12.99)
3. Large (12 slices, $16.99)
Choose pizza size (1-3): 3

--- PIZZA PARTY PLAN ---
People: 8
Total slices needed: 24
Slices per pizza: 12
Pizzas to order: 2
Total cost: $33.98
Cost per person: $4.25
Leftover slices: 0

Enjoy your party!
"""

def main():
    print("PIZZA PARTY CALCULATOR")
    people_count = get_number_of_people()
    appetite_level = get_appetite_level()
    pizza_size = get_pizza_size()

    pizza_slices = {1: 6, 2: 8, 3: 12}
    pizza_price = {1: 8.99, 2: 12.99, 3: 16.99}


    total_slices = calculate_total_slices(people_count, appetite_level)
    
    #print(total_slices)

    num_pizzas = calculate_pizzas_needed(total_slices, pizza_slices[pizza_size])
    #print(num_pizzas)

    total_cost= calculate_total_cost(num_pizzas, pizza_price[pizza_size])
    #print(total_cost)

    cost_per_person = calculate_cost_per_person(total_cost, people_count)
    #print(cost_per_person)

    leftover_slices = calculate_leftover_slices(num_pizzas, pizza_slices[pizza_size], total_slices)
    #print(leftover_slices)

    display_results(people_count, total_slices, pizza_slices[pizza_size], num_pizzas, total_cost, cost_per_person, leftover_slices)
   
def get_number_of_people():
    people_count = int(input("How many people are coming? "))
    while people_count <= 0:
        people_count = int(input("Please enter a positive number for people coming: "))
    return people_count

def get_appetite_level():
    appetite_level = int(input("How hungry are they?\n1. Light eaters (2 slices per person)\n2. Normal appetite (3 slices per person)\n3. Very hungry (4 slices per person)\nChoose appetite level (1-3): "))
    while appetite_level not in [1, 2, 3]:
        appetite_level = int(input("Invalid choice. Please choose appetite level (1-3): \n1. Light eaters (2 slices per person)\n2. Normal appetite (3 slices per person)\n3. Very hungry (4 slices per person)\nChoose appetite level (1-3): "))
    return appetite_level
def get_pizza_size():
    pizza_size = int(input(f"What size pizzas?\n1. Small (6 slices, $8.99)\n2. Medium (8 slices, $12.99)\n3. Large (12 slices, $16.99)\nChoose pizza size (1-3): "))
    while pizza_size not in [1, 2, 3]:
        pizza_size = int(input("Invalid choice. Please choose pizza size (1-3): n1. Small (6 slices, $8.99)\n2. Medium (8 slices, $12.99)\n3. Large (12 slices, $16.99)\nChoose pizza size (1-3): "))
    return pizza_size

def calculate_total_slices(people, slices_per_person):
    return people * (slices_per_person+1)

def calculate_pizzas_needed(total_slices, slices_per_pizza):
    from math import ceil

    #rint(total_slices,slices_per_pizza)
    
    return ceil(total_slices / slices_per_pizza)

def calculate_total_cost(num_pizzas, price_per_pizza):
    return num_pizzas * price_per_pizza


def calculate_cost_per_person(total_cost, people):
    return total_cost / people

def calculate_leftover_slices(num_pizzas, slices_per_pizza, total_slices):
    return (num_pizzas * slices_per_pizza) - total_slices



def display_results(people, total_slices, slices_per_pizza, num_pizzas, total_cost, cost_per_person, leftover):
    print("\n--- PIZZA PARTY PLAN ---")
    print(f"People: {people}")
    print(f"Total slices needed: {total_slices}")
    print(f"Slices per pizza: {slices_per_pizza}")
    print(f"Pizzas to order: {num_pizzas}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Cost per person: ${cost_per_person:.2f}")
    print(f"Leftover slices: {leftover}\n")
    print("Enjoy your party!")

    
if __name__ == "__main__":
    main()
