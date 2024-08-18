# Find all occurrences of a substring in a given string by ignoring the case
# Input: str1 = "Welcome to USA. usa awesome, isn't it?"
# output: The USA count is: 2

def count_occurence(str1, substr):
    return str1.count(substr)

str_1=input("Enter the string\n").lower()
substr=input("Enter the substring\n").lower()

cnt=count_occurence(str_1, substr)
print("The {} count is: {}".format(substr.upper(),cnt))
