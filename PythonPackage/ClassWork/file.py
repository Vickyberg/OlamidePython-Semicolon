# with open("hello.txt", mode="r", encoding='utf-8') as file:
#     # file.write("I love writing\n")
#     # file.write("I love reading\n")
#     # file.writelines(['I am prone to violence\n', "I am Olamide\n"])
#     # read = file.read()
#     # print(read)
#     for index, line in enumerate(file.readlines()):
#         print(f"line {index + 1}: {line}")

import json
import pathlib
file_path = pathlib.Path("./json/twitter_users.json").resolve()
file_path.parent.mkdir(parents=True,exist_ok=True)
twitter_users = [
    {
        'name': 'Olamide Victor',
        'username': '@olavictor_',
        'age': 32,
        'is_verified': True,
        'number_of_tweet': 45,
        'followers': 100,
        'following': 40,
        'tweets': [
            {
                'content': 'Be yourself, strive to be happy',
                'likes': 5,
                'comments': 20
            },
            {
                'content': 'We are obediently waiting',
                'likes': 5,
                'comments': 20
            },
        ]
    },

    {
        'name': 'Temi Dayo',
        'username': '@dayo',
        'age': 31,
        'is_verified': True,
        'number_of_tweet': 75,
        'followers': 1000,
        'following': 110,
        'tweets': [
            {
                'content': 'God is good',
                'likes': 45,
                'comments': 120
            },
            {
                'content': 'Jesus is coming soon',
                'likes': 50,
                'comments': 80
            },
            {
                'content': 'Jesus is Lord',
                'likes': 150,
                'comments': 110
            },
        ]
    },

    {
        'name': 'Diego Khaled',
        'username': '@diego',
        'age': 30,
        'is_verified': True,
        'number_of_tweet': 75,
        'followers': 10000,
        'following': 70,
        'tweets': [
            {
                'content': 'God is good',
                'likes': 95,
                'comments': 65
            },
            {
                'content': 'No space for Tinubu',
                'likes': 500,
                'comments': 80
            },
            {
                'content': 'We need change',
                'likes': 150,
                'comments': 110
            },
            {
                'content': 'Naija will be great again',
                'likes': 15,
                'comments': 10
            },
            {
                'content': 'We are tired of corruption',
                'likes': 95,
                'comments': 40
            },
        ]
    },

    {
        'name': 'Khaled Malam',
        'username': '@khaled',
        'age': 30,
        'is_verified': False,
        'number_of_tweet': 75,
        'followers': 10000,
        'following': 70,
        'tweets': [
            {
                'content': 'God is love',
                'likes': 85,
                'comments': 115
            },
            {
                'content': 'No space for Tinubu as presido',
                'likes': 700,
                'comments': 80
            },
            {
                'content': 'We need change in naija',
                'likes': 150,
                'comments': 110
            },
            {
                'content': 'Naija is doom',
                'likes': 153,
                'comments': 40
            },
            {
                'content': 'We are tired of corruption',
                'likes': 25,
                'comments': 140
            },
            {
                'content': 'No old cargo',
                'likes': 1700,
                'comments': 800
            },
            {
                'content': 'Python is fun to write',
                'likes': 1700,
                'comments': 800
            }
        ]
    }
]
with file_path.open(mode="w", encoding="utf-8") as file:
    json.dump(twitter_users,file,indent=4)

x = json.dumps(twitter_users)
print(type(x))
y = json.load(x)
print(type(y))