class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:

    def __init__(self, title, duration):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *args):
        self.videos.append(args)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)

# Добавление видео
ur.add(v1, v2)
print(v1)

