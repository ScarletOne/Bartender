import random

fails = [
    'https://media.giphy.com/media/ADr35Z4TvATIc/giphy.gif',
    'https://media.giphy.com/media/26ybwvTX4DTkwst6U/giphy.gif',
    'https://media.giphy.com/media/LJemLPJs6dBhm/giphy.gif',
    'https://media.giphy.com/media/ADr35Z4TvATIc/giphy.gif',
    'https://media.giphy.com/media/AAnIjZPUhrUM8/giphy.gif',
    'https://media.giphy.com/media/ADr35Z4TvATIc/giphy.gif',
    'https://media.giphy.com/media/ADr35Z4TvATIc/giphy.gif',
    'https://media.giphy.com/media/7YWmWqIoFZH6U/giphy.gif'

]

wins = [
    'https://media.giphy.com/media/b09xElu8in7Lq/giphy.gif',
    'https://media.giphy.com/media/3o7TKQdHShF1NtQgRq/giphy.gif',
    'https://media.giphy.com/media/QhRju4SJl5BGU/giphy.gif',
    'https://media.giphy.com/media/fDzM81OYrNjJC/giphy.gif'

]


def random_fail():
    return fails[random.randrange(len(fails))]


def random_win():
    return wins[random.randrange(len(wins))]
