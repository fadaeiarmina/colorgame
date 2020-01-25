
colors= ["red", "black", "blue", "green", "yellow"]


player_1_color= input("player_1 , choose your color : ")
player_2_color= input("player_2, choose your color : ")
player_3_color= input("player_3 , choose your color : ")

player_1_score = colors.index (player_1_color)
#we are finding the index (position)playeryer 1 chosen color 
player_2_score = colors.index (player_2_color)
player_3_score = colors.index (player_3_color)

if player_1_score > player_2_score and player_1_score > player_3_score :
    print ("palyer_1_wins...!")
elif player_2_score > player_1_score and player_2_score > player_3_score:
    print ("player_2wins...!")
elif player_3_score > player_2_score and player_3_score > player_1_score:
    print ("player_3wins...!")
else:
    print ("someting went wrong.....!")



