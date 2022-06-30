from  functools  import  reduce
import operator
list_of_numbers = [1,2,3,4,5]
list_of_dict = [{"name": "Asake", "gender": "F"}, {"name": "Boyo","gender": "M"}]
mapped_list_of_dict = list(map(lambda x:("Mr. "if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict))

print(mapped_list_of_dict)
print([("Mr. "if x["gender"] == "M" else "Mrs. ") + x["name"]for x in list_of_dict])

filtered_list_of_dict = list(filter(lambda x: x["gender"] == "M" , list_of_dict))
print(filtered_list_of_dict)

# list comprehension
print([name for name in list_of_dict if name["gender"] == "M"])

sum_reduce = reduce(lambda acc,val: acc + val, list_of_numbers)
m_reduce2 = reduce(operator.add, list_of_numbers)
print(sum_reduce)
print(m_reduce2)
fruit = ["pear","cucumber","water melon","banana"]
print(reduce(lambda x,y: x if len(x) > len(y) else y ,fruit))
