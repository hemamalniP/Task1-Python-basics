input1=input()
str1 =list(input1)
new=[]
for j in str1 :
    if j not in new:
        new.append(j)
        cnt=0
 for i in range(len(str1)):
if j==str1[i]:
 cnt+=1
        print("{}:{}".format(j,cnt))