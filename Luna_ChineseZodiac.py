# Chinese Conversion
year = eval(input("Want to find out what is your Chinese Zodiac? \n \n Enter Year of Birth: "))
calculation = year % 12

# solution
if calculation == 0:
    print("\n Congratulations! You got the Year of the Monkey!")
else:
    if calculation == 1:
        print("\n Congratulations! You got the Year of the Rooster!")
    else:
        if calculation == 2:
            print("\n Congratulations! You got the Year of the Dog!")
        else:
            if calculation == 3:
                print("\n Congratulations! You got the Year of the Pig!")
            else:
                if calculation == 4:
                    print("\n Congratulations! You got the Year of the Rat!")
                else:
                    if calculation == 5:
                        print("\n Congratulations! You got the Year of the Ox!")
                    else:
                        if calculation == 6:
                            print("\n Congratulations! You got the Year of the Tiger!")
                        else:
                            if calculation == 7:
                                print("\n Congratulations! You got the Year of the Rabbit!")
                            else:
                                if calculation == 8:
                                    print("\n Congratulations! You got the Year of the Dragon!")
                                else:
                                    if calculation == 9:
                                        print("\n Congratulations! You got the Year of the Snake!")
                                    else:
                                        if calculation == 10:
                                            print("\n Congratulations! You got the Year of the Horse!")
                                        else:
                                            if calculation == 11:
                                                print("\n Congratulations! You got the Year of the Sheep!")
