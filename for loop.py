## brek ,continu and pass statement 



# for i in [1,2,4,2.3,"sangamesh"]:
#     if i==2.3:
#         break
#     print(i)
# print("exited")


# for i in range(1,11):
#     if i%2==0:
#         continue
#     print (i)
# print("Exited")


# for i in range(20,1,-1):
#     if i%2!=0:
#         pass
#     else:
#         print(i)
        
# print("Exited")


#wap for 1-10
# for i in range(1,10):
#     print(i)


# #Wap for 01-1


# for i in range(10,1,-1):
#     print(i)


#wap to print list in reverse order


# list=[1,2,3,4,5,6,7,8,9,0]
# # i=len(list)-1

# # for i in list[::-1]:
# #     print(i)

# for i in range(len(list)-1,-1,-1):
#     print(i)


#Wap to program to find the factorial of given number


# n=int(input("enter the number :") )
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)



#Wap to print table

# n=int(input("enter the num:"))
# table=1
# for i in range(1,11):
#     table=n*i
#     print(table)                          

#WAp to count even and odd in list using for


# list1=[2,5,4,2,8,6,3,54,5,53,8]
# even_counter=0
# odd_counter=0

# for i in list1:
#     if i%2==0:
#         even_counter+=1
#     else:
#         odd_counter+=1
# print(f"the even elements are {even_counter}")
    
# print(f"the odd elements are {odd_counter}")



#wap to split the even and odd element in list



# list1=[2,5,4,2,8,6,3,54,5,53,8]

# even=[]
# odd=[]

# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even,odd)




#WAP to print sum of list


# list1=[2,5,4,2,8,6,3,54,5,53,8]
# sum=0
# for i in list1:
#     sum+=i 
#     print(sum)




# #wap to print cummelative sum


# list1=[2,5,4,2,8,6,3,54,5,53,8]
# sum=0
# list2=[]
# for i in list1:
#     sum+=i
#     list2.append(sum)
# print(list2)



#wap to print the special char , vowel ,  consonent , numbers and spaces. 

 
# string="Hi Welcome To @ India #indian at @14567 $"

# special=0
# vowel=0
# consonent=0
# digit=0
# space=0

# for i in string:
#     if i.isnumeric():
#         digit+=1
#     elif i in "aeiouAEIOU":
#         vowel+=1
#     elif i.isspace():
#         space+=1
#     elif not i.isalnum():
#         special+=1
#     elif i.isalpha():
#         consonent+=1
        
# print(vowel,consonent,digit,space,special)
    
    
    
#Use a for loop to print numbers from 10 to 0, decrementing by 2 each time.
    
    


# print("hello")  
# for i in range(10,0,-1):
#     if i%2==0:
#         print(i)
# print("bye")



#wap to print factorial of given number :


# num=int(input("enter the Number :"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)


#wap to print the sum of all digits 


# digit=12345

# digit2=str(digit)

# sum=0
# for i in digit2:
#     sum+=int(i)
    
# print(sum)





#Write a program to reverse a given string using a for loop.

# string="sangamesh is a good communicator."
# reverse=""
# for i in string:
#     reverse=i+reverse 
# print(str(reverse))



#wap to print thr priime number 1-50



# m=int(input("enter the number until you get list of prime number :"))
# prime=[]
# for i in range(2,m):
#     for j in range(2,i):
#         if i%j==0:
#            break
#     else:
#        prime.append(i)
# print(prime)


#wap for fibo series



# n=10
# n1=0
# n2=1
# fibo=1
# print(n1)
# print(n2)
# for i in range(1,10):
#     fibo=n1+n2
#     n1=n2
#     n2=fibo
#     print(fibo)



# *
# **
# ***




# for  i in  range(0,5):
#     for j in range(0,i):
#         print("*",end="")
#     print()





#Given a list of numbers, use a for loop to find the maximum value.



# list=[1,2,3,4,5]
# #print(max(list))
# greater=list[0]
# for i in list:
#     if i<greater:
#         break
#     else:
#         greater=i
# print(greater)




# #
# #Keep Multiplying a Number by 2 Until It Becomes Greater Than 1000


# n = int(input("Enter the number: "))

# # For loop to multiply the number by 2 until it exceeds 1000
# for result in range(n * 2, 1001, n * 2):  # Start from n*2, and increment by n*2
#     print(result)





# # # #Calculate the Power of a Number Without Using the  Operator



# base=int(input("enter the base :"))
# exponent=int(input("enter the exponent:"))
# result=1
# count=(abs(exponent))
# # while count > 0:
# for i in range(count,0,-1):
#     result*=base
# #     count-=1
#     if exponent<0:
#         result=1/result
       
# print(result)