"""
    Functions
"""

# Create simple function
def sayHello(name = 'Mohamed'):
    'print/return hello for a name'
    # print 'Hello ', name
    return 'Hello ' + name


# Addition
def getSum(num1 = 0, num2 = 0):
    total = num1 + num2
    return total

# Increment print and return
def Inc(num):
    num+=1
    print num
    return

# Add item to a list
def addToList(item = None, list = []):
    if item != None:
        list.append(item)
        return list
    else:
        print 'Item is None'
        return list
# logs

people = ['John', 'Aimane', 'Mohamed', 'Haitam']

print sayHello()
print sayHello('Aimane')


print getSum(200, 500)

Inc(100)

print addToList('Abdel', people)

print addToList()