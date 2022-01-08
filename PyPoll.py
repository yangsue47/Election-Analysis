# The data we need to retrieve.
import os
import csv

# assign and set path to file using "join"
file_to_load = os.path.join("Resources", "election_results.csv")

# create a text file 
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = []

candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# use "with" to keep file open
# opening and reading the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # reading the header
    headers = next(file_reader)
    
    # print each row in the csv file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # print candidate name for each row
        candidate_name = row[2]
        
        # this says if a name is "not in" the list
        if candidate_name not in candidate_options:

            # then add the name to the list
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100


    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# 3. print the total vote 

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"------------------------\n"
)

print(winning_candidate_summary)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
