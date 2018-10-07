"""
    Classes and Objects
"""

# Define a class
class Person:
    'This is a person class' # This is a simple documentation

    # Attributes (class variable)
    __name = ''  # '__' represent that the attributes is private
    __email = ''

    # constructor
    def __init__(self, name = 'name', email = 'email@python'):
        print 'create person class'
        self.num = 1 # object or instance variable
        self.__name = name
        self.__email = email

    # methods :
    
    # stters
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    # getters
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email

    # others methods
    def toString(self):
        # return 'Person : Name : ' + self.__name + ', Email : ' + self.__email
        return 'Person : Name : {}, Email : {}'.format(self.__name, self.__email)

# inheritance
class Customer(Person):
    'This is a customer class' # This is a simple documentation
    
    # Attributes
    __balance = 0

    # Constructor
    def __init__(self, name = 'name', email = 'email@python', balance = 0):
        print 'create customer class'
        self.__balance = balance
        Person.__init__(self, name, email)
        # super(type(Customer), self).__init__(name, email) # issues

    # methods
    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    # others methods
    def toString(self):
        return 'Customer : Name : {}, Email : {}, Balance : {}, Num : {}'.format(self.get_name(), self.get_email(), self.__balance, self.num)

# Create Objcts
person = Person()

another = Person('Jonh', 'jonh@python')

customer = Customer('Alan', 'alan@python', 10)

# print type(Customer)

# Use Objects

print customer.get_name()

customer.set_balance(5000)

print customer.toString()
# 
# Person Class Manipulation :

# print person.__class__
# print person.__doc__

# print person.num

# person.set_name('Mohamed Aimane Skhairi')
# person.set_email('medaimane@python')

# print person.get_name()
# print person.get_email()

# print 'Person with name ' + another.get_name() + ' has email ' + another.get_email()
# print another.toString()