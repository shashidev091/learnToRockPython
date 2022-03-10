
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
like = 0
for post in facebook_posts:
    try:
        like = post['Likes']
    except KeyError:
        like = 0
    finally:
        total_likes = total_likes + like

print(total_likes)
