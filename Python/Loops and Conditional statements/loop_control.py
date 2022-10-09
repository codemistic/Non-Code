#Continue Statement: 
#It returns the control to the beginning of the loop.
# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
         continue
    print('Current Letter :', letter)
    var = 10

#Break Statement: It brings control out of the loop
for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
         break
 
print('Current Letter :', letter)

#Pass Statement: We use pass statement to write empty loops.
# Pass is also used for empty control statement, function and classes.
# An empty loop
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

