import random

topics = ["topic1", "topic2", "topic3"]

print("These are the topics:")

for x in topics:
  print(x)

y = random.choice(topics)

print("The topic of the day is:", y) 
