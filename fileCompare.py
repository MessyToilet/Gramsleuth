
with open('reasources\\data\\user\\user_followers.txt', 'r') as f1:
    followers = set(f1.read().splitlines())

with open('reasources\\data\\user\\user_following.txt', 'r') as f2:
    following = set(f2.read().splitlines()) 


with open('reasources\\data\\user\\user_post_likes.txt', 'r') as f3:
    likers = set(f3.read().splitlines())

following_not_likers = following - likers
followers_not_likers = followers - likers 

print(len(following_not_likers), len(followers_not_likers))
for user in following_not_likers:
    print(user)

print("\n---\n")

for user in followers_not_likers:
    print(user)