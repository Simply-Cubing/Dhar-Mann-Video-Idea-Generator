import random

#various words
topics = ["School", "Cheating", "Bullying", "Pranking"]
word1 = ["Kid", "Teacher", "Daughter", "Mean girls", "Rich mom", "Rich dad", "Adult", "Daughter", "Little sister", "Rich bride", "Spoiled brat", "Spoiled girl", "Twin", "Kid with down syndome", "Autistic kid" , "Little boy", "Karen"]
word2 = ["backstabs", "pranks", "steals", "cheats", "cheats on", "breaks", "takes", "gets", "humiliates", "catches", "accuses", "shames",  "jealous of", "ditches", "bullies"]
pt3 = ["on test", "test answers", "poor boyfriend", "fat kid", "school spelling bee",  ]
pt4 = [", what happens will shock you", ", INSTANTLY regrets it", ", lives to regret it", ", what happens is shocking" ]

#generates a random word from the list
seed1 = random.randint(0, 16)
seed2 = random.randint(0, 14)
seed3 = random.randint(0,4)
seed4 = random.randint(0, 3)

#generates segments of the title

a = word1[seed1]
b = word2[seed2]
c = pt3[seed3]
d = pt4[seed4]

#prints title
print(a,b,c,d)  
