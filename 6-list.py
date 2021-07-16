emp_list=[]
while True:
    inp_list=input()
    if not inp_list:
        break
    emp_list.append(tuple(inp_list.split(",")))
print(sorted(emp_list))