"""
    Working with filesystem
"""

# Open file
fo = open('7_files/test.txt', 'w')

# Get Some infos
print 'File name is : ' + fo.name
print 'Is Closed : ' + str(fo.closed)
print 'Opening mode : ' + fo.mode

# write on this file
fo.write('I love python')
fo.write(' and JavaScript.')

# Close the file
fo.close()

# reopen to append text
fo = open('7_files/test.txt', 'a') # append mode to add text to file
fo.write('\nI also like PHP')
fo.close()

# read mode
fo = open('7_files/test.txt', 'r+')

# read file content text
text = fo.read()
# text = fo.read(10) # that read just 10 chars

# Ply with the file content
for word in text.split():
    print word

fo.close()

# Create new file
fo = open('7_files/test2.txt', 'w+')

fo.write('My name\'s Mohamed Aimane Skhairi')

fo.close()