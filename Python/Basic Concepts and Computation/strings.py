first_name = "Riya"
last_name = "Sabu "
fullname = first_name +" "+ last_name 

print(fullname*3)#prints the string 3 times 
question = "What's your name?"
#when a single quote is already present put the rest in double quote 
question2 = 'What\'s your name?'
#the next character will be escaped 

##INDEX
first_string = "Hey everyone"

print(
first_string[0],#first character
#first_string[12],#string index out of range
#first_string["12"],#string indices must be integers 
first_string[-1],#last character 
)


##SLICING
fruit="pomegranate"

#string_name[start:stop:step], stop value is length step value by default is 1 and start value is 0
print(
fruit[3:5],#'eg'
fruit[-1:-4:-1],#'eta'
fruit[:2:],#'pom'
fruit[0::3],#'peat'
)


##DELETING STRING 
fruit1="apple"
print(fruit1)
del fruit1
#print(fruit1)#name 'fruit1' not defined 

##CONCATENATION
w1="Happy"
w2="birthday"
print(w1+" "+w2)

##ITERATION OVER STRING
string="Python"
for i in string:
    print(i)

##IN_BUILT FUNCTIONS IN STRING CLASS 
x = "python3"
print(
type(x),#prints the data type 
x.upper()#transfers to upper case
)

y="COMP"
print(
    y.lower(),#prints in lowercase
    y.replace('M','V'),#replace the character 
)
print(len(y))#prints the length of the character 

name="Riya ,Aparna ,Tania ,Maria ,Sarasu "
print(name)#every name
name_s=name.split(",")#the comma separates and make them into lists 
print(name_s[0])#print the first name 


##FORMAT 
x='5'
y='10'
z='15'
print("The sum of {} and {} is {}".format(x,y,z))#autmatically its 0 1 2
print("The sum of {1} and {0} is {2}".format(x,y,z))

##REVERSING STRING 
name="Peace"
print(name[::-1])#step is made negetive