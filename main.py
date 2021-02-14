import sys,time as t, random as r

def slow_print(text):
   for character in text + '\n':
     sys.stdout.write(character)
     sys.stdout.flush()
     t.sleep(.055)

def game_over(people, money):
  if people <= 0 or money <= 0:
    return True

print('''
                                             _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\\\";
                        .'                              ;   _____;   \\\\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":           """----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"                      .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------" 
                           _ _        _       
                          | | |      (_)      
       _ __ ___   __ _  __| | |_ _ __ _ _ __  
      | '__/ _ \ / _` |/ _` | __| '__| | '_ \ 
      | | | (_) | (_| | (_| | |_| |  | | |_) |
      |_|  \___/ \__,_|\__,_|\__|_|  |_| .__/ 
                                       | |    
                                       |_|   ''')
slow_print("You start in California and have to drive to New Jersey. It is a 7 day trip.")

slow_print("How many people are going on the trip? Pick 2 or more. \nYour resources will run out faster the more people you have, but there is safety in numbers\nand if anything happens, you will be less likely to die (forshadowing moment):")
people = int(input())
while people < 2:
  slow_print("Pick a number 2 or more:")
  people = int(input())
peopleList = []
for person in range(int(people)):
  slow_print("Name person " + str(person+1) + ": ")
  name = input()
  peopleList.append(name)

slow_print("Before you leave, you need food, water, and other supplies.\nLet's go the the store: they will have whatever we need.")
t.sleep(1)
money = 1000
slow_print(f"You have arrived at the store and have {money} dollars")
slow_print("What do you want to buy? Food costs $25 per person per day, water costs $10 per person per day. The GPS costs $200, a whistle costs $10, and matches costs $5. A jacket costs $30 and dagger costs $100.")

slow_print("How many packages of food do you want? They are enough for one person for one day, and cost $25.")
food = int(input())
money -= food*25
slow_print(f"You have ${money} left.")
slow_print("How many water bottles do you want? They are enough for one person for one day, and cost $10.")
water = int(input())
money -= water*10
slow_print(f"You have ${money} left.")
slow_print("Do you want the GPS? It costs $200. (y/n)")
GPSanswer = input()
if GPSanswer == "y" or GPSanswer == "yes":
  GPS = True
  money -= 200
else:
  GPS = False
slow_print(f"You have ${money} left.")
slow_print("Do you want the whistle? It costs $10. (y/n)")
whistleanswer = input()
if whistleanswer == "y" or whistleanswer == "yes":
  whistle = True
  money -= 10
else:
  whistle = False
slow_print(f"You have ${money} left.")
slow_print("Do you want the box of matches? It costs $5. (y/n)")
matchesanswer = input()
if matchesanswer == "y" or matchesanswer == "yes":
  matches = True
  money -= 5
else:
  matches = False
slow_print(f"You have ${money} left.")
slow_print("How many jackets do you want? They are enough for one person, and cost $30.")
jackets = int(input())
money -= jackets*30
slow_print(f"You have ${money} left.")
slow_print("How many daggers do you want? They are enough to protect three people each, and cost $100.")
daggers = int(input())
money -= daggers*100
slow_print(f"You have ${money} left.")
if money < 0:
  slow_print("You have been arrested by government because you can't pay your debt :(")

# each dagger makes 3 people immune to attacks
# each jacket makes 1 person immune to snowstorm
# GPS makes chance of getting lost drop from 25% each day to 10%
# running out of water means death for a person
# running out of food mean 20% chance of death for every person each day.
# whistle saves you from being lost, but 1 person will die before the save. If no whistle
# matches result in a fire that prevents death of a person if lost
if money > 0: 
  slow_print("You have set out on your journey. Every second, four hours pass")
day = 1
while day <= 7 and people > 0 and money > 0:
  #food and water stuff
  slow_print("Day " + str(day))
  t.sleep(1)
  if water <= 0:
    people -= 1
    death = r.choice(peopleList)
    slow_print(f"You didn't have enough water, so {death} died.")
    peopleList.remove(death)
  if food <= 0:
    starvation = r.randint(1,20)
    if starvation <= 4:
      people -= 1
      death = r.choice(peopleList)
      peopleList.remove(death)
      slow_print(f"You didn't have enough food, so {death} died.")
  
  food -= people
  water -= people
  #getting in a car crash
  t.sleep(1)
  carcrash = r.randint(1,12)
  if carcrash == 7:
    slow_print("You got in a car crash!")
    severity = r.randint(1,2)
    if severity == 1:
      slow_print("You payed $100 to get your car fixed. Luckily no one was hurt.")
    else:
      slow_print("Everyone died. Big oof.")
      people -= people
  if game_over(people, money):
    break
  #getting the whole group lost chance (based on GPS)
  t.sleep(1)
  group_lost = r.randint(1, 100)
  if GPS:
    if group_lost <= 3:
      if whistle and not matches:
        people -= 2
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        death2 = r.choice(peopleList)
        peopleList.remove(death2)
        slow_print(f"You got lost. You blew on the whistle, and someone came to your rescue. Sadly, they didn't make it before {death} and {death2} died. You also lost a little bit of resources. ")
        food -= people
        water -= people
      elif matches and not whistle:
        food -= 2*people
        water -= 2*people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        slow_print(f"You got lost. Only {death1} died and without the whistle it took too long to be rescued and you lost a lot of resources.")
      elif whistle and matches:
        food -= people
        water -= people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        slow_print(f"You got lost, but you made a fire from the matches to keep you warm until someone heard your whistle and came to your rescue. You lost some supplies and {death1} died.")
      else:
        food -= 2*people
        water -= 2*people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        death2 = r.choice(peopleList)
        peopleList.remove(death2)
        slow_print(f"You got lost. You didn't have any supplies to help you with your scenario. {death1} and {death2} froze to death and you lost a lot of supplies")
  else:
    if group_lost <= 10:
      if whistle and not matches:
        people -= 2
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        death2 = r.choice(peopleList)
        peopleList.remove(death2)
        slow_print(f"You got lost. You blew on the whistle, and someone came to your rescue. Sadly, they didn't make it before {death} and {death2} died. You also lost a little bit of resources. ")
        food -= people
        water -= people
      elif matches and not whistle:
        food -= 2*people
        water -= 2*people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        slow_print(f"You got lost. Only {death1} died and without the whistle it took too long to be rescued and you lost a lot of resources.")
      elif whistle and matches:
        food -= people
        water -= people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        slow_print(f"You got lost, but you made a fire from the matches to keep you warm until someone heard your whistle and came to your rescue. You lost some supplies and {death1} died.")
      else:
        food -= 2*people
        water -= 2*people
        death1 = r.choice(peopleList)
        peopleList.remove(death1)
        death2 = r.choice(peopleList)
        peopleList.remove(death2)
        slow_print(f"You got lost. You didn't have any supplies to help you with your scenario. {death1} and {death2} froze to death and you lost a lot of supplies")
  if game_over(people, money):
    break

  #getting in a snow storm chance
  t.sleep(1)
  snowstorm = r.randint(1, 15)
  if snowstorm <= 1:
    if jackets >= people:
      slow_print("You got caught in a snow storm, but everyone had their jackets to help them to survive")
    elif jackets < people:
      people -= (people - jackets)
      slow_print("You got caught in a snow storm. You didn't have enough jackets for everybody so the rest froze to death. Here is who died: ")
      for person in range(people-jackets):
        death = r.choice(peopleList)
        peopleList.remove(death) 
        slow_print(death)
  if game_over(people, money):
    break
    
  #getting attaked chance
  t.sleep(2)
  attacked = r.randint(1,10)
  if attacked <= 1:
    if daggers*3 < people:
      people -= (people - daggers*3)
      death = r.choice(peopleList)
      slow_print(f"You were attacked. You didn't have enough daggers to scare them off. {death} died in the attack.")
      peopleList.remove(death)
      if len(peopleList)%3 != 0 and daggers >= 1:
        death = r.choice(peopleList)
        peopleList.remove(death)
        slow_print(f"{death} died too.")
      else:
        slow_print("And other people as well, we won't bother with all the names")

    elif daggers*3 >= people:
      slow_print("You were attacked. Thanfully you used your daggers to scare the attackers off. ")
  if game_over(people, money):
    break  
    
  #getting covid chance
  t.sleep(2)
  covid = r.randint(1,7)
  if covid <= 1:
    possible_death = r.choice(peopleList)
    slow_print(f"{possible_death} got Covid! You need to pay $100 to get them the cure. Without it, their chances of survival are slim")
    slow_print("Will you pay? (y/n): ")
    response = input()
    if response == "y":
      money -= 100
      slow_print("Phew! They survived")
    else:
      survival = r.randint(1,20)
      if survival <= 2:
        slow_print("Luckily they recovered.")
      else:
        slow_print(f"{possible_death} died. RIP!")
        people -= 1
        peopleList.remove(possible_death)
  if game_over(people, money):
    break

  day+=1

  if day == 8 and people > 0 and money >= 0:
    slow_print("You did it!")

if game_over(people, money):
  slow_print("You failed!!!")
if people <= 0:
  slow_print("Everyone died!")
if money < 0:
  slow_print("You are in debt and are going to jail!")
