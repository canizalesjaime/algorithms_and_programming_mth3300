import random


# Position update with constant velocity
# x = 0
# v = 2  # units per step

# for t in range(5):
#     x += v
#     print(x)

# inside = 0
# total = 10000


# roll a die three times, probability you get consecutive heads
count=0
num_sim=1000000
for i in range(num_sim):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    num3 = random.randint(1,6)
    if num1==num2 or num2==num3:
        count=count+1

print("probability is: ", count/num_sim)
