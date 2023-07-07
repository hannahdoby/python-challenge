
# Import Dependencies
# sourcery skip: aug-assign
import os
import csv

# Declare file location
csvpath = os.path.join('python-challenge/PyPoll/election_data.csv')


total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header
    csv_header = next(csvreader)

    for row in csvreader:
        
        total_votes = total_votes + 1
        
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = (votes / total_votes) * 100

print(total_votes)
print(candidate_votes)
print(vote_percent,"%")

