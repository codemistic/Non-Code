#Sanjay and Rahul have a set of  color crayons. 
# Sanjay has Red, Blue, Green and Pink whereas
#  Rahul has Green , Violet, Yellow, Blue  and White. 
# Write a Python script to
#  find the colors they have in common.
#  Print the colors that Rahul has but not Sanjay.
#  Sanjay lost his  Green color. Update this information

Sanjay = {'Red','Blue','Green','Pink'}
Rahul = {'Green','Violet','Yellow','Blue','White'}

print("The colours that are common: ",Sanjay&Rahul)
print("The colours that Sanjay has but not with Rahul: ",Sanjay-Rahul)
Sanjay.discard('Green')
