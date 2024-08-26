# str1 = "Emma is a data scientist who knows Python. Emma works at google."
#  Find the last position of a given substring

str1 = "Emma is a data scientist who knows Python. Emma works at google."

substr=input("Enter the substring\n")
idx=str1.rindex(substr)
print("Last occurrence of {} starts at index {}".format(substr,idx))