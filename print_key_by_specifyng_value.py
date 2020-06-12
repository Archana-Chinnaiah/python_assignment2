my_dict = {'Spain': 'Europe', 'Japan': 'Asia', 'India': 'Asia', 'Italy': 'Europe', 'Thailand': 'Asia', 'Sudan': 'Africa'} 
key_list = list(my_dict.keys()) 
val_list = list(my_dict.values())
continent_name=input("enter the continent name:")
print(" The countries are")
for key_list,val_list in my_dict.items():
    if val_list==continent_name:
        print(key_list)


#print(key_list[val_list.index(continent_name)]) 
#print(key_list[val_list.index()]) 

# one-liner 
#print(list(my_dict.keys())[list(my_dict.values()).index(continent_name)])
'''

my_dict = {'Spain': 'Europe', 'Japan': 'Asia', 'India': 'Asia', 'Italy': 'Europe', 'Thailand': 'Asia', 'Sudan': 'Africa'} 
for name,age in list.iteritems():
    if age == search_age:
            return name

>>> def method2(list,search_age):
...     return [name for name,age in list.iteritems() if age == search_age]
... 
>>> def method3(list,search_age):
...     return list.keys()[list.values().index(search_age)]'''
