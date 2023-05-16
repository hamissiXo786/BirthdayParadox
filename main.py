import datetime, random

def getBirthdays(numberofBirthdays):
    """returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range(numberofBirthdays):
        # the year is unimportant for our simulation, as long as all birthdays have the same year.
        startofYear = datetime.date(2001, 1, 1)

        #get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startofYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None #All birthdays are unique, so return None.

    #compare, each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

#display the intro:
print("""Birthday Paradox, by Hamissi 

the birthday paradox shows us that in a group of N people, 
the odds that two of them have matching birthdays is suprisingly
large. this program does a monte carlo simulation (that is
repeated simulations ) to explore this concept. (its not 
actually a paradox, it's just a suprising result )
""")

#set up a tuple of month names in order:

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
          "Aug", "Sep", "Oct", "Nov", "Dec")

while True: #keep asking until the user enter a valid amount.
    print("how many birthday shall i generate ??(Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break #user has entered a valid amount.
print()

#generate and display the birthdays:
print("here are", numBdays, "birthdays")
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:"""display a coma for each birthday after the first birthday"""
    print(", ", end = "")
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end = "")
print()
print()

#determine if there are two birthdays that match.
match = getMatch(birthdays)

#display the results:
print("In this simulation, ", end = "")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays. ")
print()

#Run through 100,000 simulations:
print("generating", numBdays, "random birthdays 100, 000 times...")
input("press enter to begin....")

print("let's run another 100, 000 simulations. ")
simMatch = 0 #how many simulations had matching birthdays with them
for i in range(100_000):#report progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run....")
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100, 000 simulations run. ")

#display simulation results:
probability = round(simMatch / 100_000 * 100 ,2 )
print("out of 100, 000 simulations of ", numBdays, "people there was a ")
print("matching birthday in that group", simMatch, "times. this means")
print("that", numBdays, "people have a", probability, "%chance of")
print("having a mathcing birthday in their group. ")
print("that's probably more than you would think")


