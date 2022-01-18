nums=[12,35,97,-42,-523,-453]
print("original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x>0,nums))
print("positive numbers in the list:",new_nums)
