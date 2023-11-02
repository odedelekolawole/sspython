from . add import add
from . sub import subtract
from . mult import multiply
from . div import division
from . pi import PI

def calculate_all(x, y):
    sum_ = add(x, y)
    difference = subtract(x, y)
    product = multiply(x, y)
    divi = division(x, y)
    
    
    return sum_, difference, product, divi