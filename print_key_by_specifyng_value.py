my_dict = {'Spain': 'Europe', 'Japan': 'Asia', 'India': 'Asia', 'Italy': 'Europe', 'Thailand': 'Asia', 'Sudan': 'Africa'} 
key_list = list(my_dict.keys()) 
val_list = list(my_dict.values())
continent_name=input("enter the continent name:")
print(" The countries are")
for key_list,val_list in my_dict.items():
   if (val_list.upper()==continent_name.upper()):
        print(key_list)


