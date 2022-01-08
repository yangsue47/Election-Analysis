# The data we need to retrieve.
import os
import csv

# assign and set path to file using "join"
file_to_load = os.path.join("Resources", "election_results.csv")

# create a text file 
file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save,"w") as txt_file:

# writing some data or sentence in the text file
    #txt_file.write("Counties in the Election \n-------------------- \nArapahoe \nDenver \nJefferson")

# use with to keep file open
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
