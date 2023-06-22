file = open("Test/a.txt", "w")
for i in range(5):
    value = input()
    file.writelines(value)
file.close()

file = open("Test/a.txt", "r")
for i in range(5):
    value_out_of_file = file.readline()
    print(value_out_of_file)
file.close()

file = open("Test/a.txt", "r")
value_out_of_file = file.readlines()
print(value_out_of_file)
file.close()