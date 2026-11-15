num_str = "42"
num_int = int(num_str). #Convert string (str) to integer (int)
print(num_int + 1)

#Error: you can only do math with string and string or interger and interger. You cant combine them
#print(num_str + 1)

float_str = "3.14"
num_float = float(float_str). #Convert string to float
print(num_float + 2.19)

#Error:
#print(float_str + 2.19)

int_num = 7
float_num = float(int_num).  #Converting integer to float
print(float_num)

float_num2 = 9.99
int_num2 = int(float_num2).  #Converting float to integer
print(int_num2)

num = 20
num_str2 = str(num).  #Convert integer to string
print("This shirt costs $" + num_str2)

#Error
#print("This shirt costs $" + num)
