#  i/o experimentation

#files
infile = open('myfile.txt', 'r')

print("Welcome to the experiment.")

for line in infile:
    print(line)

infile.close()

outfile = open('output.txt', 'w')

outfile.write("This is a test")

outfile.close()

# from keyboard
x = input("Enter a string: ")
print(x)

