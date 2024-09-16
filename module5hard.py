class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(self.password)

    def __int__(self):
        return self.age

class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []

    def add(self, i, Video):
        if i != Video:
            self.videos.append(i)




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur)
print(v1)
print(v2)
