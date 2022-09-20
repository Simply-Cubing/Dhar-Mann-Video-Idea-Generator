import random
word1 = ["Kid", "Teacher", "Daughter", "Mean girls", "Rich mom", "Rich dad", "Adult", "Daughter", "Little sister", "Rich bride", "Spoiled brat", "Spoiled girl", "Twin", "Kid with down syndome", "Autistic kid"]
word2 = ["backstabs", "pranks", "steals", "cheats", "cheats on", "breaks", "takes", "gets", "humiliates", "catches", "accuses", "shame",  "jealous of", "ditches", "bullies"]
pt3 = ["on test", "test answers", "poor boyfriend", "fat kid", "school spelling bee",  ]
pt4 = [", what happens will shock you", ", INSTANTLY regrets it", ", lives to regret it", ", what happens is shocking" ]
seed1 = random.randint(1, 15)
seed2 = random.randint(1, 15)
seed3 = random.randint(1,5)
seed4 = random.randint(1, 4)


#generates first part of the title
if seed1 == 1:
  a = (word1[0]) 
if seed1 == 2:
  a = (word1[1])
if seed1 == 3:
  a = (word1[2])
if seed1 == 4:
  a = (word1[3])
if seed1 == 5:
  a = (word1[4])
if seed1 == 6:
  a = (word1[5])
if seed1 == 7:
  a = (word1[6])
if seed1 == 8:
  a = (word1[7])
if seed1 == 9:
  a = (word1[8])
if seed1 == 10:
  a = (word1[9])
if seed1 == 11:
  a = (word1[10])
if seed1 == 12:
  a = (word1[11])
if seed1 == 13:
  a = (word1[12])
if seed1 == 14:
  a = (word1[13])
if seed1 == 15:
  a = (word1[14])

#generates second part of title  
if seed2 == 1:
  b = (word2[0])
if seed2 == 2:
  b = (word2[1])
if seed2 == 3:
  b = (word2[2])
if seed2 == 4:
  b = (word2[3])
if seed2 == 5:
  b = (word2[4])
if seed2 == 6:
  b = (word2[5])
if seed2 == 7:
  b = (word2[6])
if seed2 == 8:
  b = (word2[7])
if seed2 == 9:
  b = (word2[8])
if seed2 == 10:
  b = (word2[9])
if seed2 == 11:
  b = (word2[10])
if seed2 == 12:
  b = (word2[11])
if seed2 == 13:
  b = (word2[12])
if seed2 == 14:
  b = (word2[13])
if seed2 == 15:
  b = word2[14]

#generates third part of the title
if seed3 == 1:
  c = (pt3[0])
if seed3 == 2:
  c = (pt3[1])
if seed3 == 3:
  c = (pt3[2])
if seed3 == 4:
  c = (pt3[3])
if seed3 == 5:
  c = (pt3[4])

#generates fourth part of the title
if seed4 == 1:
  d = (pt4[0])
if seed4 == 2:
  d = (pt4[1])
if seed4 == 3:
  d = (pt4[2])
if seed4 == 4:
  d = (pt4[3])

print(a,b,c,d)  
    
    
     
        
        


