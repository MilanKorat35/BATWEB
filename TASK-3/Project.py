#-----------------------Kaun Banega Crorepati (KBC)-------------------------------#

Qus=["1. Which one of the following river flows between Vindhyan and Satpura ranges?\n(a) Narmada\t(b) Mahanadi\n(c) Son\t\t(d) Netravati",
     "2. The Central Rice Research Station is situated in?\n(a) Chennai\t(b) Cuttack\n(c) Bangalore\t(d) Quilon",
     "3. Who among the following wrote Sanskrit grammar?\n(a) Kalidasa\t(b) Charak\n(c) Panini\t(d) Aryabhatt",
     "4. The metal whose salts are sensitive to light is?\n(a) Zinc\t(b) Silver\n(c) Copper\t(d) Aluminum",
     "5. Patanjali is well known for the compilation of \n(a) Yoga Sutra\t\t(b) Panchatantra\n(c) Brahma Sutra\t(d) Ayurveda",
     "6. D.D.T. was invented by?\n(a) Mosley\t(b) Rudolf\n(c) Karl Benz\t(d) Dalton",
     "7. The hottest planet in the solar system?\n(a) Mercury\t(b) Venus\n(c) Mars\t(d) Jupiter",
     "8. Where was the electricity supply first introduced in India?\n(a) Mumbai\t(b) Dehradun\n(c) Darjeeling\t(d) Chennai",
     "9. Which peninsular river is least seasonal in flow?\n(a) Narmada\t(b) Krishna\n(c) Godavari\t(d) Cauvery",
     "10. Which of the following is not a nuclear power center?\n(a) Narora\t(b) Chamera\n(c) Kota\t(d) Kakrapara",
     "11. Who developed Python Programming Language?\n(a) Wick van Rossum\t(b) Rasmus Lerdorf\n(c) Guido van Rossum\t(d) Niene Stom",
     "12. Is Python case sensitive when dealing with identifiers?\n(a) no\t\t\t(b) yes\n(c) machine dependent\t(d) none of the mentioned",
     "13. Which of the following is the correct extension of the Python file?\n(a) .python\t(b) .pl\n(c) .py\t\t(d) .p",
     "14. Which of the following is used to define a block of code in Python language?\n(a) Indentation\t(b) Key\n(c) Brackets\t(d) All of the mentioned",
     "15. Which keyword is used for function in Python language?\n(a) Function\t(b) def\n(c) Fun\t\t(d) Define"]

Ans=["a","b","c","b","a","a","b","c","c","b","c","b","c","a","b"]
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
amount=0
print("-----------Welcome to KBC-----------")
print("")
print("If you want to exit Enter 'e'.")
print("")
for i in range(len(Qus)):
    print(Qus[i])
    a=input("Enter the Ans:")
    if(a=="e"):
       print("Congrtulation you Win",amount)
       break
    elif a==Ans[i]:
        amount=level[i]
        print("")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
    else:
       print("")
       print("Congrtulation you Win",money)
       break
    if(i==14):
        print("Congrtulation you Win",amount) 

