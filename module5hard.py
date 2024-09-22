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

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

    def __str__(self):
        return self.title


class UrTube(User, Video):
    def __init__(self):
        self.users = []
        self.videos = []
        # self.current_user = current_user

    def add(self, name):
        if name != super().title:
            self.videos.append(name)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)

# Добавление видео
ur.add(v1, v2)
print(v1)

