
import matplotlib.pyplot as plt #plotting various graphs
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from pulp import LpProblem,LpMinimize,LpVariable,LpStatus,LpInteger #linear programming library
x=lambda x:print('\n')
df=pd.read_csv("D:\mini project\sample data.csv")
print(df)
x(1)
print(df.describe()) #describing the dataset
x(1)
print("[ID 916, ID 936, ID 1178]")
x(1)
print('([impressions, clicks, total conversions]\n')
x(1)
class lpp(): #initializing class
    var=[[],[],[]]
    def valfind(self,id,i,obj):
#function to find and store the computational values for the linear programming model
        obj.var[i].append((df.loc[df['company campaign ID'] == id,'impressions'].mean())) #computing the average of the impression for each campaign ID 
        obj.var[i].append((df.loc[df['company campaign ID'] == id,'clicks'].mean())) #computing the average of the clicks for each campaign ID
        obj.var[i].append((df.loc[df['company campaign ID'] == id,'total conversions'].mean())) #computing the average of the total conversions for each campaign ID
lpp.valfind=classmethod(lpp.valfind)
lppvar=lpp() #creating 'lppvar' as an instance/object of class 'lpp'
lppvar.valfind(916,0,lppvar) #invoking function 'valfind()' of class 'lpp' using object 'lppvar' to store average values for ID 916
lppvar.valfind(936,1,lppvar) #invoking function 'valfind()' of class 'lpp' using object 'lppvar' to store average values for ID 936
lppvar.valfind(1178,2,lppvar) #invoking function 'valfind()' of class 'lpp' using object 'lppvar' to store average values for ID 1178
print(lppvar.var) #printing values of the variable 'var' that stores all the values for the programming problem
x(1)
a=df.loc[df['company campaign ID']==916] #splitting the dataset for ID 916
print(a)
x(1)
b=df.loc[df['company campaign ID']==936] #splitting the dataset for ID 936
print(b)
x(1)
c=df.loc[df['company campaign ID']==1178] #splitting the dataset for ID 1178
print(c)
x(1)
y=lambda y:(df.loc[df['company campaign ID'] == y,'spent'].mean()) #lamda function to find the average cost for each campaign ID
a_cost=int(y(916))
b_cost=int(y(936)) #calling the lamda function for ID 936
c_cost=int(y(1178))
const=[]
def intake(): 
#function to accept and store the constraint values
    temp=0
    check=1 #flag variable to check if entered value meets the if condition or not
    temp=int(input("enter the least value of impressions that you wish to obtain: "))
    while(check!=0):
        if temp>=df['impressions'].mean(): #checking if the entered constraint value is atleast equal to or more than the average value of the entire dataset
            const.append(temp) #if condition is true, append list 'const' with entered constraint value
            check=0 #change value of flag to instruct the code to exit the while loop
        else:
            temp=int(input(('value isnt in the range, enter again: '))) #re-enter constraint value
            check=1 #flag value remains the same, so the while loop keeps running and the user keeps entering until the condition is met
    temp=int(input("enter the least value of clicks that you wish to obtain from the viewer: "))
    while(check!=1):
        if temp>=df['clicks'].mean():
            
            const.append(temp)
            check=1
        else:
            temp=int(input(('value isnt in the range, enter again: ')))
            check=0
    temp=int(input("enter the least value of conversions that you wish to obtain: "))
    while(check!=0):
        if temp>=df['total conversions'].mean():
            const.append(temp)
            check=0
    else:
        temp=int(input(('value isnt in the range, enter again: ')))
        check=1
intake()

def linearproblem():
#function to solve the linear programming model
    problem = LpProblem("AD Conversions", LpMinimize) #creating the 'problem' variable to store the optimization equation and the constraints
    a1 = LpVariable("ID_916", lowBound=0, cat=LpInteger) #creating lpp variables
    b1 = LpVariable("ID_936", lowBound=0, cat=LpInteger)
    c1 = LpVariable("ID_1178", lowBound=0, cat=LpInteger)
    problem += a1*a_cost + b1*b_cost + c1*c_cost, 'ObjectiveFunction'
    for i in range (0,3):
        problem += (lppvar.var[0][i])*a1 + (lppvar.var[1][i])*b1 + (lppvar.var[2][i])*c1>=(const[i]) #creating the cnstraint equations
    x(1)
    print(problem)
    x(1)
    #print(LpStatus[problem.status])
    x(1)
    problem.solve()
    x(1)
    #print(LpStatus)
    #print(LpStatus[problem.status])
    x(1)
    print("The amount of money to be spent on ID 916 is: ", a1.varValue)
    x(1)
    print("The amount of money to be spent on ID 936 is: ", b1.varValue)
    x(1)
    print("The amount of money to be spent on ID 1178 is: ", c1.varValue)
linearproblem()

plt.subplot(1,2,1)
plt.scatter(df["impressions"], df["total conversions"])
plt.xlabel("impressions")
plt.ylabel("total conversions")

plt.subplot(1,2,2)
plt.scatter(df["impressions"], df["approved conversions"])
plt.xlabel("impressions")
plt.ylabel("approved conversions")
plt.show()


plt.bar(df['gender'],df['roas'])
plt.ylabel("gender")
plt.xlabel("ROAS")
plt.show()


plt.plot(df['roas'],df['spent'])
plt.ylabel("amount spent")
plt.xlabel("ROAS")
plt.show()


plt.subplot(1,3,1)
plt.boxplot(df['spent'])
plt.xlabel("amount spent")

plt.subplot(1,3,2)
plt.scatter(df['spent'],df['roas'])
plt.ylabel("ROAS")
plt.xlabel("spent")

plt.subplot(1,3,3) 
plt.scatter(df['spent'], df['total conversions'])
plt.ylabel("total conversions")
plt.xlabel("spent")
plt.show()


plt.bar(df['age'], df['click through rate'])
plt.ylabel("clicks to conversion ratio")
plt.xlabel("age")
plt.show()


plt.bar(df['company campaign ID'], df['click through rate'])
plt.ylabel("clicks to conversion ratio")
plt.xlabel("company campaingn ID")
plt.show()


plt.subplot(1,2,1)
plt.bar(df["age"], df['interest'])
plt.xlabel("age")
plt.ylabel("interest")

plt.subplot(1,2,2)
plt.bar(df["gender"], df['interest'])
plt.xlabel("gender")
plt.ylabel("interest")
plt.show()


sns.heatmap(df[["impressions","clicks","spent","total conversions","approved conversions"]].corr(),annot=True ,fmt=".2f", cmap="coolwarm")
plt.show()
sns.barplot(x=df["company campaign ID"], y=df["roas"], hue=df["age"])
plt.show()