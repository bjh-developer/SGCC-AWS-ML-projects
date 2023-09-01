# with open('data.txt', 'w') as f: #overwrite
#     f.write('line1\n')
#     f.write('line2')

# with open('data.txt', 'r+') as f: #read+write
#     f.write('!@#%')

####

# Opening files
# with open('data.txt') as f:
#     for line in f:
#         print(line, end='')

#Write to files
with open('newfile.txt', 'w') as f:
    f.write('hello everyone\n')
    f.write('have a good day\n')
    f.write('bye everyone\n')
print()

#append to a file
with open('newfile.txt', 'a') as f: #a - append mode
    f.write('This is the last line!\n')
