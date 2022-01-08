counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}

for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county in voting_data:
    print(f"{county['county']} county has {county['registered_voters']:,} registered voters.")

for county_dict in voting_data:
    print(county_dict['registered_voters'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"There were {total_votes:,} votes altogether. "
    f"You got {(my_votes / total_votes) * 100:,.1f}% of the votes."
)

print(message_to_candidate)