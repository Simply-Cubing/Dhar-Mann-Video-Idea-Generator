import random
word1 = ["Kid", "Teacher", "Daughter", "Mean girls", "Rich mom", "Rich dad", "Adult", "Daughter", "Little sister", "Rich bride", "Spoiled brat", "Spoiled girl", "Twin", "Kid with down syndome", "Autistic kid"]
word2 = ["backstabs", "pranks", "steals", "cheats", "cheats on", "breaks", "takes", "gets", "humiliates", "catches", "accuses", "shames",  "jealous of", "ditches", "bullies"]
pt3 = ["on test", "test answers", "poor boyfriend", "fat kid", "school spelling bee",  ]
pt4 = [", what happens will shock you", ", INSTANTLY regrets it", ", lives to regret it", ", what happens is shocking" ]
seed1 = random.randint(1, 15)
seed2 = random.randint(1, 15)
seed3 = random.randint(1,5)
seed4 = random.randint(1, 4)

#generates segments of the title
a = word1[seed1-1]
b = word2[seed2-1]
c = pt3[seed3-1]
d = pt4[seed4-1]

print(a,b,c,d)  
