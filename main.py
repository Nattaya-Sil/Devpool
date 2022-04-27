#The Sorting Hat
import random as rd
import time

print("The Sorting Hat of Hogwart")
Gryffindor_house =[]
Hufflepuff_house =[]
Ravenclaw_house =[]
Slytherin_house =[]

for i in range(1,51) :
    name = input("Enter your name : ")

    # 01 Random number for students and make max size of house
    if (len(Gryffindor_house)<=13 and len(Hufflepuff_house)<=13 and
            len(Ravenclaw_house)<=13 and len(Slytherin_house)<=13):         # 1TTTT
            number = rd.randint(1, 4)

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) <= 13 and
          len(Ravenclaw_house) <= 13 and len(Slytherin_house) > 13):        # 2TTTF
            number = rd.randint(1, 3)

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) <= 13 and
              len(Ravenclaw_house) > 13 and len(Slytherin_house) <= 13):    # 3TTFT
            number = rd.choice([1,2,4])

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) <= 13 and
          len(Ravenclaw_house) > 13 and len(Slytherin_house) > 13):         # 4TTFF
            number = rd.choice([1, 2])

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) > 13 and
              len(Ravenclaw_house) <= 13 and len(Slytherin_house) <= 13):   # 5TFTT
            number = rd.choice([1, 3, 4])

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) > 13 and
          len(Ravenclaw_house) <= 13 and len(Slytherin_house) > 13):        # 6TFTF
            number = rd.choice([1, 3])

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) > 13 and
            len(Ravenclaw_house) > 13 and len(Slytherin_house) <= 13):      # 7TFFT
            number = rd.choice([1, 4])

    elif (len(Gryffindor_house) <= 13 and len(Hufflepuff_house) > 13 and
              len(Ravenclaw_house) > 13 and len(Slytherin_house) > 13):  # 8TFFF
            number = 1

    elif (len(Gryffindor_house)>13 and len(Hufflepuff_house)<=13 and
            len(Ravenclaw_house)<=13 and len(Slytherin_house)<=13):         # 9FTTT
            number = rd.choice([2,3 ,4])

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) <= 13 and
            len(Ravenclaw_house) <= 13 and len(Slytherin_house) > 13):      #10 FTTF
            number = rd.choice([2,3])

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) <= 13 and
              len(Ravenclaw_house) > 13 and len(Slytherin_house) <= 13):    #11 FTFT
            number = rd.choice([2, 4])

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) <= 13 and
              len(Ravenclaw_house) > 13 and len(Slytherin_house) > 13):     # 12 FTFF
            number = 2

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) > 13 and
            len(Ravenclaw_house) <= 13 and len(Slytherin_house) <= 13):     # 13 FFTT
            number = rd.choice([3, 4])

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) > 13 and
              len(Ravenclaw_house) <= 13 and len(Slytherin_house) > 13):    # 14 FFTF
            number = 3

    elif (len(Gryffindor_house) > 13 and len(Hufflepuff_house) > 13 and
              len(Ravenclaw_house) > 13 and len(Slytherin_house) <= 13):    # 15 FFFT
            number = 4


    #02 Selecting house
    if (number==1):
        print(">.< You are brave at heart, daring nerve and chivalry ...")
        time.sleep(0.5)
        print(name,", you are going to...")
        time.sleep(0.5)
        print("*** Gryffindor ***")
        Gryffindor_house.append(name)
    elif(number==2):
        print(">.< You are just and loyal, also true and unafraid of toil ...")
        time.sleep(0.5)
        print(name,", you are going to...")
        time.sleep(0.5)
        print("*** Hufflepuff ***")
        Hufflepuff_house.append(name)
    elif(number==3):
        print(">.< You’ve a ready mind who of wit and learning ...")
        time.sleep(0.5)
        print(name,", you are going to...")
        time.sleep(0.5)
        print("*** Ravenclaw ***")
        Ravenclaw_house.append(name)
    else:
        print(">.< You’ll make your real friends, Those cunning folk use any means to achieve their ends ...")
        time.sleep(0.5)
        print(name,", you are going to...")
        time.sleep(0.5)
        print("*** Slytherin ***")
        Slytherin_house.append(name)
    print("You are student no. " , i, " of all")
else:
    #03 end of 50 students and summary
    print("-----------------------------------------------------------------------------------\n"
          "Sorry, The houses are not available!\n -----------------------To summary----------------------\n"
          "The Gryffindor House has " + str(len(Gryffindor_house)) + " peoples\n"
                "That are ", str(Gryffindor_house),"\n"
          "The Hufflepuff House has " + str(len(Hufflepuff_house)) + " peoples\n"
                "That are ", str(Hufflepuff_house), "\n"
          "The Ravenclaw House has " + str(len(Ravenclaw_house)) + " peoples\n"
                "That are ", str(Ravenclaw_house), "\n"
          "The Slytherin House has " + str(len(Slytherin_house)) + " peoples\n"
                "That are ", str(Ravenclaw_house), "\n"
          )