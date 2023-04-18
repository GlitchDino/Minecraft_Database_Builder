
import ast 

with open('function_types.txt','r') as f:
    r=f.read()
    room_functions=ast.literal_eval(r)


print(room_functions)
for function in room_functions:
    print(function)
    
with open('function_types.txt','w') as f:
    string=str(room_functions)
    f.write(string)