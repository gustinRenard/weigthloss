#####################
#Data about the user#
#####################

"""
user_height -> m
user_weight -> kg
user_gender -> 0 if woman et 1 if man
user_fmi_goal -> between 10 and 15
user_pace -> between 0.75 and 1
"""

#Default
user_height = 1.79
user_weight = 87.4
user_age = 17
user_gender = 1
user_fmi_goal = 10
user_pace = 1

#Input version
"""
user_height = float(input("height :"))
user_weight = float(input("weight :"))
user_age = float(input("Age :"))
user_gender = int(input("gender :"))
user_fmi_goal = int(input("goal fmi:"))
user_pace = float(input("pace :"))
"""

#############
#Calculation#
#############

user_bmi = user_weight/(user_height**2)
user_fmi_real = ((1.2*user_bmi)+(0.23*user_age)-(10.8*user_gender)-5.4)/100
user_weight_fat = user_weight*user_fmi_real
user_weight_fat_zero = user_weight-user_weight_fat
user_weight_goal = round(user_weight_fat_zero+(user_weight_fat_zero*(user_fmi_goal/100)),2)
user_weight_loose = round(user_weight-user_weight_goal)

print("\ngoal :",user_weight_goal,"\ntotal to loose:",user_weight_loose)

semaine = 0

while user_weight > user_weight_goal:
    semaine += 1
    user_weight_week = round(user_weight*(user_pace/100),2)
    user_weight = round(user_weight-user_weight_week,2)
    print("\nWeek :",semaine,"goal weight of the week :",user_weight,"\nweight to loose for reach the goal :",user_weight_week)

print("\nMonths :",semaine/4)
print(round(user_weight_loose/(semaine/4),2),"kg/month")

"""
Gustin Renard
Tuesday 30 Avril 2019
English
"""
