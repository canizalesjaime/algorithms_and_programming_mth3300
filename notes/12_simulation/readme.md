# Lecture Notes

## table of contents
1. Simulations
2. In Class Assignments 


## What is Simulation?

A simulation is the use of a computer program to imitate the behavior of a real-world system.

Instead of solving problems purely with mathematical formulas, we:
- Define rules of the system  
- Run repeated experiments  
- Observe outcomes  


### Key Idea
Simulation allows us to approximate answers by experimentation.

---

### When to Use Simulation
- When analytical solutions are difficult or complex  
- When randomness is involved  
- When we want to test scenarios or behaviors  

---

## Example 1: Probability of Heads or Tails

We simulate flipping a fair coin many times.

---

### Analytical Result
- P(Heads) = 0.5  
- P(Tails) = 0.5  

---

### Simulation
```python
import random

heads = 0
tails = 0
trials = 10000

for i in range(trials):
    if random.random() < 0.5:
        heads += 1
    else:
        tails += 1

print("P(Heads):", heads / trials)
print("P(Tails):", tails / trials)
```

### Insight
As the number of trials increases, the estimated probability approaches the true value. This is an example of convergence.


## Example 2: Probability of Exactly 2 Heads in 5 Flips

### Analytical Result
P(2 heads) = C(5,2) / 2^5 = 10 / 32 = 0.3125

---

### Simulation
```python
import random

success = 0
trials = 100000

for i in range(trials):
    heads = 0
    
    for i in range(5):
        if random.random() < 0.5:
            heads += 1
    
    if heads == 2:
        success += 1

print("Estimated probability:", success / trials)
```
### Insight
We simulate the experiment repeatedly and count how often the desired outcome occurs.


## Example 3: At Least Two Consecutive Heads in 5 Flips
### Key Idea
We are checking for a pattern (HH appearing anywhere), not just counting heads.

---

### Simulation
```python
import random

success = 0
trials = 100000

for i in range(trials):
    flips = []
    
    for i in range(5):
        if random.random() < 0.5:
            flips.append("H")
        else:
            flips.append("T")
    
    found = False
    for i in range(4):
        if flips[i] == "H" and flips[i+1] == "H":
            found = True
            break
    
    if found:
        success += 1

print("Estimated probability:", success / trials)
```

### Insight
Simulation is especially useful for problems involving patterns that are difficult to count analytically.

---

## Example 4: Dice Simulation

We simulate rolling a six-sided die and estimate the probability of rolling a specific value.

---

### Analytical Result
- P(rolling a 3) = 1/6  

---

### Simulation
```python
import random

count = 0
trials = 10000

for i in range(trials):
    roll = random.randint(1, 6)
    if roll == 3:
        count += 1

print("Estimated probability of rolling a 3:", count / trials)
```


### Extension
We can also simulate multiple dice.

Example: Probability that the sum of two dice equals 7
```python
import random

success = 0
trials = 100000

for i in range(trials):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    
    if d1 + d2 == 7:
        success += 1

print("Estimated probability:", success / trials)
```

### Insight
Simulation allows us to easily explore more complex probability questions without deriving formulas.

---

## Example 5: Random Movement with Turtle

We simulate a point moving randomly in two dimensions.

---

### Simulation
```python
import turtle
import random

t = turtle.Turtle()
t.speed(0)

steps = 200

for i in range(steps):
    angle = random.randint(0, 360)
    t.setheading(angle)
    t.forward(20)

turtle.done()
```

### Interpretation
- Each step moves in a random direction  
- The path formed is called a random walk  


### Applications
- Robotics exploration  
- Particle motion  
- Random processes in nature  

---

## Summary

- Simulation approximates real-world behavior through repeated trials  
- Accuracy improves with more trials  
- It is especially useful when:
  - Exact solutions are difficult  
  - Systems involve randomness  
  - We want to experiment with different scenarios  


## In Class Assignments
### 1. 
Write a Python simulation to estimate the probability of getting at least 3 heads in 6 coin flips.

* Run the simulation for at least 100,000 trials
* Print the estimated probability
* Then compare your result to the analytical value (you can compute it using combinations)

### 2.
Write a Python simulation where you roll two six-sided dice 100,000 times.

Estimate the probability that:

* The sum of the dice is greater than or equal to 9
* Given that the first die is even

Your program should:

* Count only trials where the first die is even
* Among those, compute how often the sum ≥ 9
* Output the estimated conditional probability