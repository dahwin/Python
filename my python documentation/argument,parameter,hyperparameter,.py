# function definition with one parameter
def greet(name):
    print("Hello, " + name + "!")

# function call with one argument
greet("Alice")
# function definition with two parameters
def add_numbers(a, b):
    return a + b

# function call with two arguments
result = add_numbers(5, 7)
print(result)
from sklearn.ensemble import RandomForestClassifier

# create a random forest classifier with hyperparameters
rf = RandomForestClassifier(n_estimators=100, max_depth=5)

# train the model on a dataset
X_train, y_train = load_dataset('train.csv')
rf.fit(X_train, y_train)

# evaluate the model on a test dataset
X_test, y_test = load_dataset('test.csv')
accuracy = rf.score(X_test, y_test)
print("Accuracy:", accuracy)


def calculate_discount(price, discount_rate=0.1, max_discount=50):
    """
    Calculates the discounted price of a product.

    Arguments:
        price (float): The original price of the product.

    Parameters:
        discount_rate (float, optional): The percentage discount rate to apply (default: 0.1).
        max_discount (float, optional): The maximum discount amount in dollars (default: 50).

    Returns:
        float: The discounted price of the product.
    """
    # calculate the discount amount
    discount_amount = min(price * discount_rate, max_discount)

    # calculate the discounted price
    discounted_price = price - discount_amount

    return discounted_price
'''
In this example:

Argument: The price argument is a required value that the function expects to receive when it is called. It represents the original price of a product.

Parameter: The discount_rate and max_discount parameters are defined in the function signature and represent values that the function expects to receive when it is called, but have default values if not provided. They control the behavior of the function and are used to calculate the discounted price.

Hyperparameter: The max_discount hyperparameter is a parameter that controls the behavior of the function, but is set by the user before the function is called and is not learned by the function during execution. It determines the maximum discount amount that can be applied to the price. It is set to a default value of 50, but can be changed by the user if necessary.

To use this function, you can call it with the price argument, and optionally specify the discount_rate and max_discount parameters:
'''
# calculate the discounted price with default discount rate and max discount
discounted_price = calculate_discount(100)

# calculate the discounted price with a custom discount rate and max discount
discounted_price = calculate_discount(100, discount_rate=0.2, max_discount=75)
'''
In the first example, the price argument is provided with a value of 100, and the function uses the default discount_rate of 0.1 and max_discount of 50 to calculate the discounted price. 
In the second example, the price argument is again provided with a value of 100, but the discount_rate and max_discount parameters are explicitly set to 0.2 and 75, respectively, to calculate a different discounted price.'''