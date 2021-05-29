
name = input("Enter your name :  ")
age = input("Enter your age :  ")
age = int(age)

chat_point = 0


print("Hello", name)

if (age >= 15):
    print("You can chat...")
    ready_to_chat = input(
        "Are you ready to write some impressive dms and getting some boring responses(yes/no)!").lower()
    if ready_to_chat == "yes":
        print("Hold Tight we are starting chat !")

        print(">>> hi")
        re1 =input("your chance>>> ")

        if re1 == "hi":
           chat_point  += 1
           print("You are dope with talking soo sweet!")
           print("You got", chat_point)

        else:
            print("You loose ", name , "!")
            chat_point -= 1
            print("Only", chat_point ,"🌟"  , "left") 

        print(">>> busy ?..")
        re2 = input("your chance >>> ")

        if re2 == "nai":
            chat_point += 1
            print("You have done this :)")
            print("You score", chat_point)

        else :
            chat_point -= 1
            print("You lose 1 point")
            print("your score is", chat_point)

        print(">>>assignment ?")
        re3 = input("your chance>>> ")

        if re3 == "yepi":
            chat_point +=1
            print("You got one  point.  And  you score is ", chat_point)

        else:
            chat_point -=1
            print("You lose one point. And you current score is", chat_point)

        print(">>> OR...")
        re4 = input("your chance>>> ")

        if re4 == "or kuch ni":
            chat_point += 5
            print("You are awsme....")
            print("You got 5 points and your score is ", chat_point)

        else:
            chat_point -= 1
            print("You lose. Now get lost from here!")

        print(">>> Bye..")
        re5 = input("your chance>>> ")

        if re5 == "💘" :
            print("You are great and you blown my mind")
            print("You got all the points.")

            print(" GAME OVER :):) ")

        else : 
            print("Jaa Na yrrr")
            print("assignment krna h deadline h")

        


    else:
        print("ook ! ! ")

else:
    print("You are not eligible to talk with Miss Assignment....")
