import random
subjects = ["Sharukh Khan","Abitab Bachan", "Rajni didi ","Nirmala Sitarama","Ajay Devgan ","Kajol "," Sita Maa","Group of Monkey","Insaan","Narendra Modi","Kashish"]
actions = ["lunch with","breaks up","eat food",'make meggie',"seems angrey","declears war","cancles the party","show anger","buy dress","fall in mud","seen clothless"]
place_of_things = ["at the red fort","in ganga","in home","in temple","in mannat","behind red fort","apple of eye", "at moon","in woshroom","at their boyfrind's room","in under bleket","in room"]
while True :
    subject=random.choice(subjects)
    action =random.choice(actions)
    place = random.choice(place_of_things)

    headline = f"BREAKING NEWS : {subject} {action} {place}"
    print("\n"+ headline)
    
    user_input=input("\n Do you want to add more headline? (yes\no)").strip().lower()
    if user_input == "no" :
        break 

    print("\n Thanks for using this Fake Headline Generator made by Kashish!!\n Have a good day :)")