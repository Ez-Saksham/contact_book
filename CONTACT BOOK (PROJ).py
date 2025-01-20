
#DATE - 2025/01/20                                                                       #by-SAKXAMYDV



contact = {}   #empty dictionaries, You can add your data here too instead of manually typing            




#-------------------------------VEWING ALL CONTACTS---------------------------------#
def viewallcontacts():

 print("NAME-----------------CONTACT NUMBER")

 for v1,v2 in contact.items():
     print("--"+v1,"--"+v2)
   
   



   



#-------------------------------ADDING NEW CONTACTS---------------------------------#

def newcontact(i):
  

  for a in range(i):
  
   name = input('Enter the contact name : ')
   number = input('Enter the contact number : ')
   contact[name.upper()] = number #making it upper case for convinence


  viewallcontacts()







#------------------------------ SEARCHING CONTACTS---------------------------------#

def  searchforacontact():

  name = input('Enter the Contacts name to search for its Number: ')
  name = name.upper()


  if name in contact:  #should not use contact() it is like calling a function not an distionary
   print("-----------------------Here is the your result---------------")
   
  for v1 in contact.keys():
    if name == v1 :
      print(contact.get(name))
    else:
     continue



#-------------------------------UPDATING CONTACTS---------------------------------#
 
def updatephone(i):
 
 for a in range(i):
  name = input('The contact you want to update')
  numb = input('Updated Number')
  contact.update({name:numb})
  a +=1
   

  viewallcontacts()
     
#-------------------------------DELETEING CONTACTS---------------------------------#

def delcontact():

  name = input('Contact You want to delete : ')

  z = input('Warning you cannot undo it ( yes / no ) : ')
  z = z.upper()
  if z == YES :
    del contact[name.upper()]
  else:
   print("Request Terminated")


  viewallcontacts()
     






#-------------------------------------------MAIN---------------------------------------------#




print('-------------------THIS PROJECT IS AN EXERCISE PROJECT MADE BY "SAKXAMYDV"----------------------- ')
print("----------THIS IS NOT PERFECT THERE ARE PROBLEMS WHICH I WILL SOLVE AS I LEARN MORE --------------")

print('-----------------------------------------------------------------------------------------------')


print('FOR ADDING - 1 , FOR VEWING - 2 , FOR SEARCHING - 3 , FOR UPDATING - 4 , FOR DELETING - 5')
s = input('YOUR REQUEST : ')
s = int(s)




#------------------------------CALLING FUN ACCORDING TO REQUEST---------------------------------#





if s == 1:  #FOR ADDING



  i = input("-------How Many Contact You want to add ? : ")
  newcontact(int(i))
         
#print(type(i)) # ---------------------Checking the data type of input data in varaible i

 #Casting i variable into integer because it took input as a string
 


elif s == 2: #FOR VEWING
 

 viewallcontacts()




elif s == 3: #FOR SEARCHING
 
  
 searchforacontact()



elif s == 4: #FOR UPDATING
 
 n = input('No of Contacts You want to update : ')
 updatephone(int(n))




elif s == 5: #FOR DELETING
  delcontact()


else:
  print('PLEASE! , Enter the valid request')





  #ignore my typing mystakes