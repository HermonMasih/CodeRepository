# str1 = "Emma is a data scientist who knows Python. Emma works at google."
#  Find the last position of a given substring

str1 = "Emma is a data scientist who knows Python. Emma works at google."

idx=str1.rindex("Emma")
print(f'Last occurrence of Emma starts at index {idx}')