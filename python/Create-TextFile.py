# This program can create text file

name = input("Enter name :")  # Enter john

file = open('test.txt', 'w')

file.write(name)

file.close()


# Resalut in test.txt
'''
john


'''
