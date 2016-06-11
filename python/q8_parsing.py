# The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

res = []
with open('football.csv') as f:
    f.readline() # ignore the header row
    for line in f:
        data  = line.strip().split(',')
        name,for_goal,against_goal = data[0],data[5],data[6]
        diff = abs(int(against_goal) - int(for_goal))
        res.append((diff,name))

print sorted(res)[0][1]
