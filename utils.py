# from friends import graph
# from data import data

# from main import get_friends


# # Calculate similarity between two users based on their hobbies
# def calcualte_similarity(user):
#     friends = get_friends(user)
#     ans = []
#     for friend in friends :
#         user_hobbies = data[user]['hobbies']
#         friend_hobbies = data[friend]['hobbies']
#         common_hobbies = len(set(user_hobbies).intersection(set(friend_hobbies)))
#         total_hobbies = len(set(user_hobbies).union(set(friend_hobbies)))
#         similarity = common_hobbies / total_hobbies
#         ans.append(similarity)
    
#     return ans
        


# similarity_score = []
# for i in range(1, 81):
#     ans = calcualte_similarity(i)
#     similarity_score.append(ans)

# for sim in similarity_score:
#     print(sim)
    


similarity_score = [
    [0.2, 0.2, 0.5, 0.5, 0.5, 0.2, 0.2, 0.5],
    [0.2, 0.0, 0.2, 0.2, 0.2, 0.5, 0.5],
    [0.2, 0.0, 0.0, 0.5, 0.0, 0.2, 0.2, 0.2],
    [0.5, 0.2, 0.0, 0.0, 0.2, 0.5, 0.5, 0.0],
    [0.2, 0.5, 0.0, 0.0, 0.5, 0.2],
    [0.2, 0.0, 0.0, 0.0, 0.5],
    [0.5, 0.5, 0.2, 0.5, 0.0, 0.0],
    [0.2, 0.2, 0.2, 0.0, 0.0],
    [0.5, 0.2, 0.5, 0.0],
    [0.5, 0.2, 0.5, 0.0],
    [0.5, 0.0, 0.2],
    [0.2, 0.2, 0.0],
    [0.5, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.2],
    [0.0, 0.2],
    [0.0, 0.2, 0.2, 0.2],
    [0.2, 0.0, 0.0],
    [0.2, 0.2, 0.0],
    [0.2, 0.2, 0.0, 0.5],
    [0.2, 0.0, 0.0, 0.0],
    [0.5, 0.0, 0.5, 0.0, 0.2],
    [0.2, 0.0],
    [0.0, 0.0],
    [0.0, 0.0, 0.2, 0.2],
    [0.0, 0.0, 0.2, 0.5],
    [0.0, 0.0, 0.2, 0.2],
    [0.2, 0.0, 0.0, 0.5],
    [0.2, 0.2, 0.0, 0.5, 0.2],
    [0.2, 0.5, 0.0],
    [0.5, 0.2, 0.0, 0.2],
    [0.5, 0.2, 0.5, 0.2, 0.5, 0.0, 0.0],
    [0.2, 0.0, 0.0, 0.0],
    [0.2, 0.0],
    [0.0, 0.5, 0.2, 0.2, 0.2],
    [0.0, 0.0, 0.5, 0.2, 0.5, 0.2],
    [0.5, 0.0, 0.0, 0.5, 0.2, 0.2],
    [0.2, 0.5, 0.0, 0.0, 0.5, 0.2],
    [0.2, 0.2, 0.5, 0.0, 0.0, 0.5],
    [0.2, 0.5, 0.2, 0.5, 0.0, 0.0],
    [0.2, 0.2, 0.2, 0.2, 0.5, 0.0],
    [0.0, 0.5, 0.2, 0.5, 0.2],
    [0.0, 0.0, 0.5, 0.0, 0.5],
    [0.5, 0.0, 0.0, 1.0, 0.0],
    [0.2, 0.5, 0.0, 0.0, 0.5],
    [0.5, 0.0, 1.0, 0.0, 0.0],
    [0.2, 0.5, 0.0, 0.5, 0.0],
    [0.2, 0.2, 0.2, 0.5, 0.5],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.0, 0.5, 0.5],
    [0.2, 0.2, 0.0, 0.0, 0.2],
    [0.5, 0.2, 0.5, 0.0, 0.2],
    [0.5, 0.2, 0.5, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 1.0],
    [0.2, 0.0, 0.2, 0.5, 0.2],
    [0.2, 0.0, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.0, 0.2],
    [0.2, 0.5, 0.2, 0.0, 0.2],
    [1.0, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 1.0, 0.0, 0.2],
    [0.2, 0.0, 0.2, 0.5, 0.2],
    [0.2, 0.0, 0.2, 0.2, 0.2],
    [1.0, 0.2, 0.2, 0.0, 0.2],
    [0.0, 0.5, 0.2, 0.0, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 1.0],
    [0.2, 0.0, 0.2, 0.5, 0.2],
    [0.2, 0.0, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.0, 0.2],
    [0.2, 0.5, 0.2, 0.0, 0.2],
    [1.0, 0.2, 0.2, 0.2, 0.2],
    [0.0, 0.5, 0.2, 0.0, 1.0],
    [0.0, 0.0, 0.5, 0.5, 0.0],
    [0.5, 0.0, 0.0, 0.2, 0.5],
    [0.2, 0.5, 0.0, 0.2, 0.2],
    [0.0, 0.5, 0.2, 0.2, 0.0],
    [1.0, 0.0, 0.5, 0.2, 0.0],
    [0.2, 0.2],
    [0.2, 0.0],
    [0.2, 0.0]
]




