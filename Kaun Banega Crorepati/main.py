name = input("Enter your name: ")
ques = ["1: How many states are there in India?", "2: International Literacy day is observed on ","In which group of places the Kumbha Mela is held every twelve years?","4: Bahubali festival is related to ", "5: Which day is observed as the World Standards  Day?"]
options = ["A. 12\nB. 28\nC. 26", "A. Sep 8\nB. Nov 28\nC. Sep 22","A. Ujjain. Purl; Prayag. Haridwar\nB. Prayag. Haridwar, Ujjain,. Nasik\nC. Rameshwaram. Purl, Badrinath. Dwarika","A. Jainsism\nB. Hinduism\nC. Islam","A. June 13\nB. Sep 8\nC. Oct 14"]
ans = ["B. 28", "A. Sep 8", "B. Prayag. Haridwar, Ujjain,. Nasik", "A. Jainism", "C. Oct 14"]
money = 0
for i in range(len(ques)):
    print(ques[i])
    print(options[i])
    userAns = input("Enter the answer: ")
    if( userAns == ans[i]):
        print("Your answer is correct! ")
        money = money + 1000
    else:
        print("Your answer is incorrect! ")
        break  
print("Game over!",name,"have won", money, "Ruppees") 
