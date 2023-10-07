# Define a function named 'cheese_and_buns' that takes another function 'original_fun' as an argument
def cheese_and_buns(original_fun):
    # Define a nested function named 'wrap'
    def wrap():
        # Print a message for the upper bread
        print('I am upper bread')
        
        # Call the original function (in this case, 'chicken')
        original_fun()
        
        # Print a message for the lower bread
        print('I am lower bread')
    
    # Return the 'wrap' function (not called)
    return wrap

# Decorate the 'chicken' function with the 'cheese_and_buns' decorator
@cheese_and_buns
def chicken():
    print('I am roasted chicken')

# Calling 'chicken' will now call the wrapped version of the function
# which includes the bread messages
chicken()
