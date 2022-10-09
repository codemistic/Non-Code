# Anjali  wants  to  store  the  number  of  stamps 
#  she  has  collected  for  five  different countries.  
# Write  a  Python  program  to  store  all  country  names 
#  along  with  total number  of  stamps  she  has  for  that  country
#   using  a  dictionary. 
#  Print  the  number  of stamps  she  has  for  ‘Kenya’, 
#  if  available,  else  print  ‘No  stamps  for  Kenya’.
#   Anjali wants  to  update  the  stamp  count  
# for  the  country  ‘China’  to  15. 
#  Also  add  a  new country ‘Pakistan’ with total stamp
#  count as 3 to the dictionary. 
#  Print  the  dictionary after updating these information. 



dict_no = {}
for i in range(0,5):
    name = input("Enter the name of the country : ")
    number = int(input("Enter the no of stamps  :"))
    
    dict_no.update({name : number })

stamp_no = dict_no.get("Kenya")

if stamp_no:
    print("The number of stamps from Kenya is ",stamp_no)
else:
    print("No stamp for kenya")

dict_no["China"]= 15

dict_no.update({"Pakistan" : 3})

print("Updated dictionary ", dict_no)
