def max(num1,num2):
    if(num1>num2):
        resert = num1
    else:
        resert = num2
    return resert

x=eval(input("first number"))
y=eval(input("secend number"))

print(x,"와",y,"중 큰수는",max(x,y),"이고 작은수는",min(x,y),"이다")
