# WAP that excepts value from user and display that number if and only if it is positive value

'''n = input("Enter value:")
if int(n) <= 0:
    print("value is negative")
else:
    print(n + "is positive")'''

#Write a program which accepts average marks of student and if average is greater than 40 then it will display a message “Congratulation!!!
 #You pass this exam successfully” else it will display “Sorry!!! Better luck next time”'''

'''m1 = int(input("Enter maths marks:"))
m2 = int(input("Enter DBMS marks:"))
m3 = int(input("Enter OOP marks:"))
marks = m1 + m2 + m3
avg = marks // 3
if avg <= 40:
    print("Sorry, You Failed")
else:
    print("Congratulation!!! You cleared the exam")'''

#question_3

'''m1 = int(input("enter maths marks:"))
m2 = int(input("enter dbms marks :"))
m3 = int(input("enter oop marks :"))
m4 = int(input("enter cn marks :"))
m5 = int(input("enter nis marks :"))

marks = m1 + m2 + m3+ m4+ m5
avg = marks // 5
if int(avg) >= 90:
    print("you scored A grade")
elif int(avg) >=70:
    print("you scored B grade")
elif int(avg) >= 50:
    print("C")
elif int(avg) >= 40:
    print("D")
else:
    print("F")'''

#question 4
'''m1 = int(input("Enter Value m1"))
m2 = int(input("Enter Value m2"))
m3 = int(input("Enter Value m3"))

if int(m1 > m2 and m1 > m3):
    print("M1 is greater")
elif int(m2 > m3 and m2 > m3):
    print("M2 is greater")
else:
    print("M3 is greater")'''

#question 5

'''num = int(input("enter value:"))
x = 0
flag = 0
for i in range(2,num):
    if num%i == 0:
        flag = 1

if flag:
    print("Not Prime")
else:
    print("Prime")'''

#question 6

'''names = []
num = input("names:")
for i in names:
    name = input("input name " +i)
    names.append(name)
for i in num:
    print(name[i])'''

#question_7

'''names = ["ramu", "shyamu", "kanu", "manu", "ramu", "radha", "manu"]

x = []

for i in names:
    if i not in x:
        x.append(i)
    print("duplicate removed: ")
    print(x)'''

#question 8

'''X = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("Original List: ", X)
u_value = set(val for dic in X for val in dic.values())
print("Unique Values: ", u_value)'''











