#Jonathan Scannell
#My code helps you find out how many calories you are supposed to eat in a day based off of your weight
#I used a TDEE calculator to find how many calories one should eat in a day
#The calorie intake is based off of someone who is 5'10 and worksout once or twice a week
#The cutting and bulking are found by taking away 500 calories and adding 500 calories
print('Hello! today we are going to find out how many calories you should eat in a day based off of your goals.')
weight = int(input('enter your weight in pounds: '))
height = int(input('enter your height in inches: '))
age = int(input('enter your age: '))
#this is the general equation that takes your height weight and age and shows your bmr but i had to tweak it so it can turn inches into centimeters
bmr = 10 * weight * 0.45359237 + 6.25 * height * 2.54 - 5 * age + 5
print('Your basal metabolic rate is: ', round(bmr))
activity = float(input('Enter how much activity you have per day,\n1.2 = 0-2 days of activity\n1.375 = 3-4 days per week of light activity\n1.55 = 3-5 days per week of moderate 60-70 percent MHR for 30-60min activity\n1.725 = 6-7 days per week of high intensity activity\n1.9 = 6-7 days of extreme activity for 90+ min per day: '))
#the numbers are what turn your bmr into how many calories you should eat based off of your activity levels
cals = (bmr * activity)
#this is the equation that converts into calories
print('your daily calorie intake should be: ',round(cals), 'calories')
goal = float(input('Select option weight goal\n1 for maintain weight\n2 for cutting weight\n3 for Gaining weight: '))
while goal > 3 or goal < 1:
    goal = float(input('Invalid in put, please select option weight goal\n1 for maintain weight\n2 for cutting weight\n3 for Gaining weight: '))
if goal == 2:
    print(round(cals - 500))
    print('When trying to cut eat about 1.5x your body weight in protein the a little lower than maintenance but\ncut the carbs by a lot and eat healthy fats')
#this is how you find the cutting calories you take 500 calories away from your maintenance
elif goal == 3:
        print(round(cals + 500))
        print('When bulking eat about 2x your body weight in protein and also\nup the carbs a little as well')
#This is how you find bulking calories you add 500 to your 
elif goal == 1:
            print(round(cals))
            print('When maintaining weight eat around 1-1.5x your body weight in protein\nand keep the carbs and fats at a moderate level')
else:
                print('Error, try again')
busy_lvl = float(input('Now lets figure out a workout split that fits your lifestyle\nselect 1 for not busy\nselect 2 for kinda busy\nselect 3 for busy\nselect 4 for very busy: '))
if busy_lvl == 1:
    print('You should follow a PPL twice a week progam, which is\nPush (Chest, Shoulders, and Triceps)\nPull (Back and Biceps)\nLegs (Quads, Hamstrings, Calves, and Glutes)')
elif busy_lvl == 2:
    print('You should follow a Upper body-Lower body twice a week')
elif busy_lvl == 3:
    print('You should follow a PPL once a week progam, which is\nPush (Chest, Shoulders, and Triceps)\nPull (Back and Biceps)\nLegs (Quads, Hamstrings, Calves, and Glutes)')
elif busy_lvl == 4:
    print('You should follow a Fullbody twice a week program')
else:
    print('Error, try again')
cardio_lvl = float(input('Lets find out how much cardio you should do a week\nselect 1 for if you are trying to cut weight\nselect 2 for if you are trying to gain weight\nselect 3 in you are trying to maintain weight:'))
if cardio_lvl == 1:
    print('You should try and do cardio 4-6 days a week for 30 to 60 minutes.')
elif cardio_lvl == 2:
    print('You should try and do cardio 1-2 days a week for 30 to 60 minutes.')
elif cardio_lvl == 3:
    print('You should try and do cardio 3 days a week for 30 to 60 minutes.')
else:
    print('Error, try again')
print('Done')
