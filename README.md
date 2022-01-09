# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following task to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code 1.63.2

## Summary
The analysis of the election show the following:
- There were 369,711 votes caste in the election.
- The candidates were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane
- The candidate results were: 
   - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
   - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
   - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
   - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
- The voter turnout for each county was:
   - Jefferson produced 10.5% of voters, which is 38,855 voters
   - Denver produced 82.8% of voters, which is 306,055 voters
   - Arapahoe produced 6.7% of voters, which is 24,801 voters
- The county with the largest turnout was:
   - Denver with 82.8% (306,055 voters)

<img src = "Resources/text%20result.png" width = 400>


## Challenge Overview 
This challenge's purpose was to expand on the data by collecting additional information about the county and its percentage turnout. In addition to finding the number of votes for the candidate, the for loop also found the number of voters within the county. 

## Election Audit Summary
Although not necessary when it comes to the candidate out, extracting additional information about the county turnout was useful for further understanding of where the votes are coming from. This additional information can be useful for future candidates to know and understand. For example, allocating more resources to the Denver county can be beneficial to winning.

We can see the benefit of the script modification in this instance as it also extracted information useful to future candidates to ponder. Other useful data that can be calculated would be a breakdown of each candidate's voting percentage per county. This would also give insight to who each county would prefer in the election. Not only can this script by apply to future county elections, but it can also be used for major state elections as well. 

Counting votes by hand would be tedious and time consuming so a script like this certainly saves time.
