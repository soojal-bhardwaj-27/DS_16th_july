# name = "sujal"
# # print("dt of name ",type(name))
# # print("len of name ", len(name))
# # print(name[0:3])
# print(name[::-1])


# lastname =  "bhardwaj"
# print(name+lastname)


# from audioop import avg


# lst = [1,2,3,45,6,"hello",0.2]  ##syntx
# print(lst)
# print(type(lst))
# print(len(lst))

# lst.append(1000)
# print(lst)
# print(lst.clear())
 
# lst1 = [1,2,3,4,5,3,4,4,[1,2,3,4,5,6,[2,3,4,54,5]]]
# print(lst1[8][6][3])


#TUPLE 

# tpl = (1,2,3,4,45,"hello",23)
# print(type(tpl))
# print(len(tpl))

# print(tpl[0])
# print(tpl[0:4])

a = 1,2,3
# print(type(a))
# print(len(a))
# print(a[0])



## tupleee unpacking >>>>>>

# a, b, c ,d= (9,1,6,8)
# print(a)
# print(b)
# print(c)
# print(d)



# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

# tpl = (1,2,2,43,4,5,6)
# lst = list(1,2,2,43,4,5,6)
# print(lst)
# print(lst.append[10
# 0])

# lst.append(100)
# print(lst)

# print(sum(tpl))
# print(avg(tpl))


#/////////////     DICTIONARY
#dictionary work on key and values
# dct = {
#       "name" : "Soojal Bhardwaj",
#       "subject" : "computer science", #type : ignore
#       "roll no.": 123, # type: ignore
#     }

# print("this is my first dicitonary ",dct)
# print(len(dct))
# print(type(dct))

#hw 
# copy
# deepcopy
# update
# get

# dct['address']="jaipur"
# print(dct)

# del dct ["name"]
# # print(dct)

# dct["subject"].append("english")
# print(dct)



# >>>>>>>>>>>>>>>>> SET <<<<<<<<<<<<<<<#

# sat = {1,2,32,54,"hello"}
# print("this is my first set :-", sat)
# print("len of sat ",len(sat))

# print("type of sat " ,type(sat))

# import copy 
# old_list = [1,2,3]

# new_list = old_list
# new_list[2] = 300
# new_list = copy.copy(old_list)
# print(new_list)

# fruit_list = ["apple","banana","mango","banana"]
# fruit = fruit_list
# fruit[0] = "pineapple"
# fruit = copy.copy(fruit_list)
# # print(fruit)



# car  = ["bmw", "audi", "toyota"]
# car2 = copy.copy(car)
# car2[0] = "lamborgini"
# # print(car2)
# # print(car)

# myself = { 
#        "name" : "soojal",
#        "class" : "12th",
#        "subject": "computer science"
#        }
# myself2 = {
#     "last name ": "bhardwaj",
#     "my friend" : "HP VICTUS"
# }
# myself.update(myself2)
# # print(myself)

# fruit = {"fruit1" : "apple","fruit2" : "banana","fruit3" : "mango"}
# my_fruit = fruit.get("fruit1")
# # print (my_fruit)

# a = "text"

# if a == "word" or "alphabet":
#     print("letter")

# else:
#     print("number")




import copy 
#/// normal copy 
# a = [1,2,3]
# b = copy.copy(a)
# b[0]= 100 
# print(b)



#//deep copy

# cars = ["bmw", "audi", "toyota"]
# cars2 = copy.deepcopy(cars)
# cars2[0] = "lamborgini"
# print(cars)
# print(cars2)

# cars = [["bmw", 2020], ["audi", 2019]]
# cars2 = copy.deepcopy(cars)
# cars2[0][1] = 2024
# print(cars)
# print(cars2)


#//// deepcopy
# fruit = [["tasty" , "apple" , 2000 ],["sweet" ,"Mango", 3000] ]
# fruit2 = copy. deepcopy(fruit)
# fruit2[0][2]= 5000
# print(fruit2)

# print(fruit)

#///get 

# fruit = {"fruit1" : "apple","fruit2" : "banana","fruit3" : "mango"}
# my_fruit = fruit.get("fruit1")
# print(my_fruit)

#assignment operator >>>>>>>>>


# a,b,c,d,e,f,g,h,i,j = 1,2,3,4,5,6,7,8,9,10


#dictionary

# fruit = {
#     "fruit1" : "apple",
#     "fruit2" : "banana",
#     "fruit3" : "mango",
#     "fruit4" : "nothing"
#     }
# my_fruit = fruit.get("fruit1")
# fruit["fruit4"] = "orange"
# print(fruit)



