# Jonathan Scannell
# My code helps you find out how many calories you are supposed to eat in a day based off of your weight
# I used a TDEE calculator to find how many calories one should eat in a day
# The calorie intake is based off of someone who is 5'10 and workout once or twice a week
# The cutting and bulking are found by taking away 500 calories and adding 500 calories
print(
    "Hello! today we are going to find out how many calories you should eat in a day based off of your goals.")
weight = int(input("enter your weight in pounds: "))
height = int(input("enter your height in inches: "))
age = int(input("enter your age: "))
# this is the general equation that takes your height weight and age and shows your bmr but i had to tweak it so it can turn inches into centimeters
bmr = 10 * weight * 0.45359237 + 6.25 * height * 2.54 - 5 * age + 5
print("Your basal metabolic rate is: ", round(bmr))
activity = float(input(
    "Enter how much activity you have per day,\n1.2 = 0-2 days of activity\n1.375 = 3-4 days per week of light activity\n1.55 = 3-5 days per week of moderate 60-70 percent MHR for 30-60min activity\n1.725 = 6-7 days per week of high intensity activity\n1.9 = 6-7 days of extreme activity for 90+ min per day: "))
# the numbers are what turn your bmr into how many calories you should eat based off of your activity levels
cals = (bmr * activity)
# this is the equation that converts into calories
print("your daily calorie intake should be: ", round(cals), 'calories')
goal = float(input(
    "Select option weight goal\n1 for maintain weight\n2 for cutting weight\n3 for Gaining weight: "))
while goal > 3 or goal < 1:
    goal = float(input(
        "Invalid in put, please select option weight goal\n1 for maintain weight\n2 for cutting weight\n3 for Gaining weight: "))
if goal == 2:
    print("When cutting you should eat around", round(cals - 500),
          "calories per day.")
    print(
        "When trying to cut eat about 1.5x your body weight in protein the a little lower than maintenance but\ncut the carbs by a lot and eat healthy fats")
# this is how you find the cutting calories you take 500 calories away from your maintenance
elif goal == 3:
    print("When bulking you should eat around", round(cals + 500),
          "calories per day.")
    print(
        "When bulking eat about 2x your body weight in protein and also\nup the carbs a little as well")
# This is how you find bulking calories you add 500 to your
elif goal == 1:
    print("When maintaining you should eat around", round(cals),
          "calories per day.")
    print(
        "When maintaining weight eat around 1-1.5x your body weight in protein\nand keep the carbs and fats at a moderate level")
else:
    print("Error, try again")
busy_lvl = float(input(
    "Select one of the options that describes your level of business\nso we can find a workout split that fits your lifestyle\nselect 1 for not busy\nselect 2 for kinda busy\nselect 3 for busy\nselect 4 for very busy: "))
while busy_lvl != 1 and busy_lvl != 2 and busy_lvl != 3 and busy_lvl != 4:
    busy_lvl = float(input(
        "Invalid input, please select one of the options that describes your level of business\nso we can find a workout split that fits your lifestyle\nselect 1 for not busy\nselect 2 for kinda busy\nselect 3 for busy\nselect 4 for very busy: "))
if busy_lvl == 1:
    print(
        "You should follow a PPL twice a week program, which is\nPush (Chest, Shoulders, and Triceps)\nPull (Back and Biceps)\nLegs (Quads, Hamstrings, Calves, and Glutes)")
elif busy_lvl == 2:
    print("You should follow a Upper body-Lower body twice a week")
elif busy_lvl == 3:
    print(
        "You should follow a PPL once a week program, which is\nPush (Chest, Shoulders, and Triceps)\nPull (Back and Biceps)\nLegs (Quads, Hamstrings, Calves, and Glutes)")
elif busy_lvl == 4:
    print("You should follow a full body twice a week program")
else:
    print("Error, try again")
def get_max(lift_weight, reps):
    answer = weight * (1 + (reps / 30))
    return answer
def main():
    print("Before we start lifting we should try and find your max first")
    print("This formula will find your 1 rep max of any lift")
    print(
        "It will find it by taking a lift you have done for multiple repetitions in the past\nand find out the amount you can do for one repetition.")
    lift_weight = int(input("Enter the amount of weight used for lift: "))
    reps = int(
        input("Enter the amount of repetitions you did that weight for: "))
    one_rep_max = get_max(lift_weight, reps)
    print("Your one rep max for this lift is: ", round(one_rep_max))
main()
busy_list = [1, 2, 3, 4]
for x in busy_list:
    if x == 1 and 1 == busy_lvl:
        print(
            "Here's your workout plan suit to fit your lifestyle and you've chosen PPL twice a week for your split\nMonday,\nChest: 4x10 flat bench press, 3x8 incline DB press, 3x12 seated cable flies superset with wide grip push-ups\nShoulders: Seated dumbbell press 5x10, lateral raises super set with face pulls 3x10-12, Reverse flies super set with weight bar raises 4x12\nTriceps: Close grip bench 4x12,12,10,10, Skull crushers 3x15\nTuesday,\nBack: T-BAR rows 12,10,8,6,4, Reverse grip seated cable rows 4x10, Front lat pulldown machine 4x8 heavy super set with bar pulldowns,Pullups to failure x2\nBiceps: Ez bar curls 4x10-12 super set with forearms twist 4x25\nWednesday,\nLegs: Back Squat warm up 2 sets working sets 5x6, RDL 3x15,12,10, Calf raises 4x15, Leg curls 4x25\nRepeat Thursday with Monday's Exercise, Friday with Tuesday's exercise, and Saturday with Wednesday's exercise.")
    elif x == 2 and 2 == busy_lvl:
        print(
            "Here's your workout plan suit to fit your lifestyle and you've chosen Upper Lower Body twice a week for your split\nUpper Day 1,\nIncline dumbbell bench 4X10, Cable chest flies super set with low cable flies 4x15, Barbell row 4x12, Lat pulldowns 4x12,10,8,8, Seated DB military press 5x10,Triple set Lat raises 4x12-DB shrugs 4x12-Reverse DB flies 4x12,Triple set Incline dumbbell curls 3x15, reverse ez bar curl 3x12, plate curls 3xfailure,Close grip bench – 4x12,12,10,10\nLower Day 1,\nBarbell squat 4x12,10,8,6, Lunges 4x10 each leg, leg press 3x12,12,15, calf raises 6x10,Super set Leg extensions 4x25 and leg curls 4x25\nRepeat Upper day 2 with Upper day 1 and Lower day 2 with Lower day 1.   ")
    elif x == 3 and 3 == busy_lvl:
        print(
            "Here's your workout plan suit to fit your lifestyle and you've chosen PPL twice a week for your split\nMonday,\nChest: 4x10 flat bench press, 3x8 incline DB press, 3x12 seated cable flies superset with wide grip push-ups\nShoulders: Seated dumbbell press 5x10, lateral raises super set with face pulls 3x10-12, Reverse flies super set with weight bar raises 4x12\nTriceps: Close grip bench 4x12,12,10,10, Skull crushers 3x15\nTuesday,\nBack: T-BAR rows 12,10,8,6,4, Reverse grip seated cable rows 4x10, Front lat pulldown machine 4x8 heavy super set with bar pulldowns,Pullups to failure x2\nBiceps: Ez bar curls 4x10-12 super set with forearms twist 4x25\nWednesday,\nLegs: Back Squat warm up 2 sets working sets 5x6, RDL 3x15,12,10, Calf raises 4x15, Leg curls 4x25")
    elif x == 4 and busy_lvl == 4:
        print(
            "Here's your workout plan suit to fit your lifestyle and you've chosen Upper Lower Body twice a week for your split\nUpper Day 1,\nIncline dumbbell bench 4X10, Cable chest flies super set with low cable flies 4x15, Barbell row 4x12, Lat pulldowns 4x12,10,8,8, Seated DB military press 5x10,Triple set Lat raises 4x12-DB shrugs 4x12-Reverse DB flies 4x12,Triple set Incline dumbbell curls 3x15, reverse ez bar curl 3x12, plate curls 3xfailure,Close grip bench – 4x12,12,10,10\nLower Day 1,\nBarbell squat 4x12,10,8,6, Lunges 4x10 each leg, leg press 3x12,12,15, calf raises 6x10,Super set Leg extensions 4x25 and leg curls 4x25")
print(
    "Lets find out how much cardio you should do a week based off of your response for if you want to cut weight, gain weight, or maintain weight")
if goal == 2:
    print(
        "Since you chose to cut weight the best option for you should be to do cardio 4-6 days a week for 30 to 60 minutes.")
elif goal == 3:
    print(
        "Since you chose to gain weight the best option for you should be to do cardio 1-2 days a week for 30 to 60 minutes.")
elif goal == 1:
    print(
        "Since you chose to maintain weight the best option for you should be to do cardio 3 days a week for 30 to 60 minutes.")
else:
    print("Error, try again")
print("Done")
