#for loop

# for letter in "Phantomray":
#     print(letter)

# for a in range(10):
#     print(a)

# for a in range(5,10):
#     print(a)


# names = ["Pam", "Jim","Angela","Michael"]
# for name in names:
#     print(name)

# for name in range(len(names)):
#     print(names[name])

# for a in range(20):
#     if a%2 == 0:
#         print("Number is Even")
#     else:
#         print("Number is Odd")



# a=5
# for b in range(a):
#     print("das")

# for a in range(1,20):
#     print(a)

# def expo(base, power):
#     result =1
#     for i in range(power):
#         result =result * base
#     return result

# print(expo(5,3))

# for i in range(3,10):
#     for b in range(2,i):
#         if (i%b) == 0:
#             print(i," Not Prime")
#         else:
#             print(i, " prime")
#             break

# red = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in red:
#     print(row)
#     for col in row:
#         print(col)

# train = "oh my god"

# for i in train:
#     print(i)

# vowel translation
# def translation(phrase):
#     translate = ""
#     for i in phrase:
#         if i == "a" or i == "u" or i == "i"  or i == "o" or i == "e":
#             translate = translate + "g"
#         else:
#             translate = translate + i
#     return translate
# das = input("Enter a phrase : ")
# disk = translation(das)
# print(disk)

# def translation(phrase):
#     translate = ""
#     for i in phrase:
#         if i in "AEOIUaeiou":
#             translate = translate + "g"
#         else:
#             translate = translate + i
#     return translate
# das = input("Enter a phrase : ")
# disk = translation(das)
# print(disk)

# def translation(phrase):
#     translate = ""
#     for i in phrase:
#         if i.lower() in "aeiou":
#             if i.isupper():
#                 translate = translate + "G"
#             else:
#                 translate = translate + "g"
#         else:
#             translate = translate + i
#     return translate
# das = input("Enter a phrase : ")
# disk = translation(das)
# print(disk)

# i = "RRDSAS"
# print(i.lower())
# print(i)

# red = "Drain"
# empty = ""
# for i in red:
#     if i == "a":
#         empty = empty + "g"
#     else:
#         empty = empty + i
# print(empty)

# try:
#     answer = int(input(" Enter the number : "))
#     print(answer)
    
# except ZeroDivisionError:
#     print("Divide by zero")
# except ValueError as err:
#     print(err)

# a = "racecar"
# print(a[0],a[-1])

# a = "racecar"
# das = ""
# for i in a:
#     if a[i] == a[]:
#         das = das + "g"
#     else:
#         das = das + i

# employee_file = open("employee.txt", "r")
# print(employee_file.readline())
# print(employee_file.readline())

# employee_file.close()

# print(employee_file.readlines())


# employee_file = open("employee.txt", "r")
# print(employee_file.readlines()[2])
# employee_file.close()

## File opening 

# emp_file = open("employee.txt", "r+")
# print(emp_file.readable())
# print(emp_file.read())
# print(emp_file.readline())
# print(emp_file.readlines())
# print(emp_file.readlines()[3])
# for emp in emp_file.readlines():
#     print(emp)
# emp_file.close()

## Writing in files 

# # employee_file = open("employees.txt","w")
# # emp_file = open("employee.txt","a")
# # emp_file.write("\n Kelly - Customer Service")
# # emp_file.close()

##Modules  


## class
# from student import Stude

# student1 = Stude("Revant","STEM",3,False)
# student2 = Stude("Trap","Bcom",2,True)

# print(student1.name)
# print(student2.major)
# print(student1.is_on_probation)

# from student import Car 
  
# Tacoma = Car("Ford","Pickuptruck",7,False)
# Camry = Car("Toyato","Sedan",15,True)

# print(Camry.company)
# print(Tacoma.mileage)

# from student import Computer

# lenovo = Computer("i7",16,"1 TB")
# Dell = Computer("i5",8,"2")

# lenovo.print()
# print(lenovo.cpu)
# Dell.print()

#MCQ

# from student import Quest

# question_prompt = [
#     "Colour of ferrari \n (a) Red \n (b) Yellow \n (c) Blue",
#     "Colour of Alpine \n (a) Red \n (b) Yellow \n (c) Blue",
#     "Colour of MClaren \n (a) Red \n (b) Yellow \n (c) Papaya"
# ]

# questions = [
#     Quest(question_prompt[0],"a"),
#     Quest(question_prompt[1],"c"),
#     Quest(question_prompt[2],"c"),

# ]

# def test(questions):
#     score = 0 
#     for question in questions:
#         print(question.question_prompt)
#         answer = input("Enter your answer")
#         if answer == question.answer:
#             score +=1
#     print(" You got a score of " + str(score) +" out of " + str(len(questions)))        

# test(questions)

#inheritance

# from student import chef
# from student import Spechef

# chef.chick()
# Spechef.chick()
# Spechef.mutton()
