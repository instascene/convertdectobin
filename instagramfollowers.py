import random
# Create an empty list to store followers
followers = []

# Add 100 random follower names to the list
for _ in range(100):
    follower_name = f"user_{random.randint(1, 1000)}"
    followers.append(follower_name)

print(followers)
