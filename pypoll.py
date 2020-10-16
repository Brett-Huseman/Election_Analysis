# Add our Dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize Variables
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning Candidate And Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print the Headers row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        #Add Total Votes
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the Candidate does not match an exisiting name...
        if candidate_name not in candidate_options:
            #Add it to list of candidates
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #Add a vote for the candidate chosen
        candidate_votes[candidate_name] += 1


#Determine the percentage of votes each candidate

#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate Percentage of Votes
    vote_percentage = float(votes) / float(total_votes) *100

    #Determine winning vote count and candidate

    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    #Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
