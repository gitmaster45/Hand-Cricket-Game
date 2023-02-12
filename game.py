#Hand Cricket
import random
print("Hand cricket")
while True:
  decision = int(input("Enter 1 to Begin game and 0 to End game\n"))
  if decision == 1:
    print("Let the toss begin")
    toss = input("Choose odd or even\n")
    number = input("Choose a number between 1 to 6\n")
    num = random.choice([1,2,3,4,5,6])

    print("You entered "+str(number))
    print("Computer enterd "+str(num))
    toss_decision = int(number) + int(num)
    

    if(toss == "odd"):
        if((toss_decision)%2==0):
     
            print("You have lost the toss and the computer has choosen to bat ")
            wish = "ball"
        else:
            wish = input("You have won the toss and do you wish to bat or ball : ")
    elif(toss == "even"):
            if((toss_decision)%2==0):
              wish = input("You have won the toss and do you wish to bat or ball \n")

            else:
          
              print("You have lost the toss and the computer has choosen to bat")
              wish = "ball"
          
    def odd():
        print("You are batting")
        user_score = 0
        while True:
            num1 = int(input("Choose a number : "))
            num2 = random.choice([1,2,3,4,5,6])
            print("Computer entered : "+str(num2))
            if(num1 != num2):
                print('You have choosen ' + str(num1) + ' and the Computer has choosen ' + str(num2) )
                user_score= num1+user_score
            else:
                print("You are OUT and the total run for the computer to win is " + str((user_score)+1))
                break
        print("You are bowling")
        computer_score = 0
        while True:
            num1 = int(input("Choose a number : "))
            num2 = random.choice([1,2,3,4,5,6])
            print("Computer entered : "+str(num2))
            if(num1 != num2):
                print('You have choosen ' + str(num1) + ' and the Computer has choosen ' + str(num2) )
                computer_score= num2+computer_score
            else:
                print("Computer is OUT and its score is " + str(computer_score))
                break
            return user_score,computer_score

    def even():
        print("You are bowling")
        computer_score = 0
        while True:
            num1 = int(input("Choose a number : "))
            num2 = random.choice([1,2,3,4,5,6])
            print("Computer entered : "+str(num2))
            if(num1 != num2):
                print('You have choosen ' + str(num1) + ' and the Computer has choosen ' + str(num2) )
                computer_score= num2+computer_score
            else:
                print("Computer is OUT and the total runs required for you to win is " + str((computer_score)+1))
                break
        print("You are batting")
        user_score=0
        while True:
            num1 = int(input("Choose a number : "))
            num2 = random.choice([1,2,3,4,5,6])
            print("Computer entered : "+str(num2))
            if(num1 != num2):
                print('You have choosen ' + str(num1) + ' and the Computer has choosen ' + str(num2) )
                user_score= num1+user_score
            else:
                print("You are OUT and your score is " + str(user_score))
                break
        return user_score,computer_score

    if wish == "bat":
        result_1,result_2 = odd()
        if result_1>result_2:
            print("You won the game")
        else:
            print("You lose the game")
    else:
      result_1,result_2 = even()
      if result_1>result_2:
          print("You won the game")
      else:
          print("Computer won the game")

  elif decision == 0:
    print("Game ended\nHave a nice day")
    break

  else:
    print("Invalid input")
