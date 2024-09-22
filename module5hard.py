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
        for new_video in args:
            for video in self.videos:
                if new_video.title == video.title:
                    break
            else:
                self.videos.append(new_video)



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)
print(ur.videos)
for video in ur.videos:
    print(video.title)
