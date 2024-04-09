from friends import graph
from data import data
import json




user = 3

def get_friends(user):
    return graph[str(user)]

# Function to recommend friends using collaborative filtering and BFS
def recommend_friends(user):
    friends = get_friends(user)
    queue = []
    visited = set()
    for friend in friends:
        queue.append(friend)
        visited.add(friend)
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return visited - set(friends) - {user}


# Function to recommend friends using common interests and BFS
def recommend_friends_interests(user):
    interests = data[user]['hobbies']
    friends = get_friends(user)
    queue = []
    visited = set()
    for friends in friends:
        queue.append(friends)
        visited.add(friends)
    
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                friend_interest = data[friend]['hobbies']
                if len(set(interests).intersection(set(friend_interest))) > 0:
                    queue.append(friend)
    return visited - {user}


# Function to calculate the degree of centrality of a user
def centrality(user):
    friends = get_friends(user)
    queue = []
    visited = set()
    for friend in friends:
        queue.append(friend)
        visited.add(friend)
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return len(visited)


# Function to create cluster of user having similar interests indicating a community
def create_cluster():
    clusters = []
    visited = set()
    for user in data:
        if user not in visited:
            interests = data[user]['hobbies']
            queue = []
            cluster = []
            queue.append(user)
            visited.add(user)
            while queue:
                current = queue.pop(0)
                cluster.append(current)
                current_friends = get_friends(current)
                for friend in current_friends:
                    if friend not in visited:
                        visited.add(friend)
                        friend_interest = data[friend]['hobbies']
                        if len(set(interests).intersection(set(friend_interest))) > 0:
                            queue.append(friend)
            clusters.append(cluster)
    return clusters

print(create_cluster())


