"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class Add an
attribute called flavors that stores a list of ice cream flavors. Write a
method that displays these flavors. Create an instance of IceCreamStand,
and call this method.
"""


class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served
class IceCreamStand(Restaurant):
    def __init__(self, name ,cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"[*] {flavor.title()}")


big_one = IceCreamStand('Big One')
big_one.flavors = ['vanilla', 'chocolate', 'strawberry']

big_one.describe_restaurant()
big_one.display()

