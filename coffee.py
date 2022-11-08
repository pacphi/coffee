from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COFFEE = {
    "Latte": {
        "coffee_name": "Latte",
        "milk": "Whole",
        "timestamp": get_timestamp()
    },
    "Cappuccino": {
        "coffee_name": "Cappuccino",
        "milk": "Oat",
        "timestamp": get_timestamp()
    },
    "FlatWhite": {
        "coffee_name": "FlatWhite",
        "milk": "Soy",
        "timestamp": get_timestamp()
    }
}

# Create a handler for coffee get route
def read():
    """
    This function responds to a request for /api/coffee
    with the complete lists of coffee drinks
    """
    # Create the list of coffee from our data
    return [COFFEE[key] for key in sorted(COFFEE.keys())]

# STUDENT DO Create a get route that accepts a parameter to return one drink
# SOLUTION
def read_one(coffee_name):
    """
    This function responds to a request for /api/coffee/{coffee}
    with one matching coffee from coffee
    :param coffee:   name of coffee drink to find
    :return:        coffee matching the name
    """
    # Does the coffee exist in COFFEE?
    if coffee_name in COFFEE:
        coffee = COFFEE.get(coffee_name)

    # otherwise, nope, not found
    else:
        abort(
            404, "Coffee with name {coffee_name} not found".format(coffee_name=coffee_name)
        )

    return coffee
