"""
    Loops
"""

people = ['John', 'Aimane', 'Mohamed', 'Haitam']


# For loop
for person in people:
    print 'Current person name ', person

# iterate with seq index
for index in range(len(people)):
    print 'Current person name ', people[index], ' in position : ', index

"""for index in range(0, 10):
    print index"""

# While loop
count = 1
while count <= 10:
    print 'Count : ', count
    if count == 5 :
        break
        # continue
    count+=1