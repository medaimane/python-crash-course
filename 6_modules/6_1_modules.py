"""
    Modules / from ... import ...
    import file from other file
"""

# import entire module
import greeting

print greeting.sayHello('Mohamed')
print greeting.sayGoodby('Hee')

# import a specific element 
from greeting import sayHello

print sayHello('Aimane')