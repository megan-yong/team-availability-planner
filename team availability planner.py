### Team availability planner ###

## (1) Empty list for team members

members = []

## (2) Adding members to list and their availability

def add_member(member, members_list):
    if member.get("name") and member.get("availability"):
        members_list.append(member)
    else:
        print("Team member missing critical information")

add_member({'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}, members)
add_member({'name':'Thomas Nelson','availability': ["Monday", "Tuesday", "Thursday", "Saturday"]}, members)
add_member({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Thursday", "Saturday"]}, members)
add_member({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, members)
add_member({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, members)
add_member({'name':'Joanne Lynn','availability': ["Monday", "Thursday"]}, members)
add_member({'name':'Latasha Bryan','availability': ["Monday", "Friday", "Sunday"]}, members)
add_member({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, members)
add_member({'name':'James Barnes Jr.','availability': ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"]}, members)
add_member({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday", "Thursday"]}, members)

## (3) Table to count daily availability

def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }

count_availability = build_daily_frequency_table()

def calculate_availability(members_list, available_frequency):
    for member in members_list:
        for day in member["availability"]:
            available_frequency[day] += 1 

calculate_availability(members, count_availability)
print(count_availability)
# {'Monday': 7, 'Tuesday': 4, 'Wednesday': 4, 'Thursday': 8, 'Friday': 3, 'Saturday': 5, 'Sunday': 3}

## (4) Select day with most availability 

def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

team_dinner = find_best_night(count_availability)
print(team_dinner)
# Thursday

## (5) Make a list of all the people available that day

def availability_on_night(members_list, day):
    return [member for member in members_list if day in member['availability']]

attending_dinner = availability_on_night(members, team_dinner)

print(attending_dinner)
# [{'name': 'Thomas Nelson', 'availability': ['Monday', 'Tuesday', 'Thursday', 'Saturday']}, {'name': 'Joyce Sellers', 'availability': ['Monday', 'Wednesday', 'Thursday', 'Saturday']}, {'name': 'Michelle Reyes', 'availability': ['Wednesday', 'Thursday', 'Sunday']}, {'name': 'Stephen Adams', 'availability': ['Thursday', 'Saturday']}, {'name': 'Joanne Lynn', 'availability': ['Monday', 'Thursday']}, {'name': 'Crystal Brewer', 'availability': ['Thursday', 'Friday', 'Saturday']}, {'name': 'James Barnes Jr.', 'availability': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday']}, {'name': 'Michel Trujillo', 'availability': ['Monday', 'Tuesday', 'Wednesday', 'Thursday']}]

## (6) Generate email for participants

form_email = """
Dear {name},

The {organisation} team will be having our quarterly team dinner and wishes you will attend. We will be meeting at {restaurant} on {day_of_week} at 7pm!

See you there, 
The {organisation} committee <3
"""

def send_email(members_who_can_attend, day, organisation, restaurant):
    for member in members_who_can_attend:
        print(form_email.format(name=member['name'], day_of_week=day, organisation=organisation, restaurant=restaurant))
        
send_email(attending_dinner, team_dinner, "Wild Society", "Delicious Cravings")

## (7) Email those unavailable to attend

unable_to_attend_dinner = [member for member in members if team_dinner not in member['availability']]

form_alt_email = """
Dear {name},

We are sorry you are unable to join the {organisation} team for our quarterly team dinner at {restaurant} on {day_of_week} at 7pm. 

Fortunately, we will be having after-dinner drinks at {bar}. We hope you can join us if you are free then! 

See you there, 
The {organisation} committee <3
"""

def send_alt_email(unable_to_attend_dinner, day, organisation, restaurant, bar):
    for member in unable_to_attend_dinner:
        print(form_alt_email.format(name=member['name'], day_of_week=day, organisation=organisation, restaurant=restaurant, bar=bar))

send_alt_email(unable_to_attend_dinner, team_dinner, "Wild Society", "Delicious Cravings", "Chill Bar")