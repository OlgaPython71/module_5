import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            for video in self.videos:
                if new_video.title == video.title:
                    break
            else:
                self.videos.append(new_video)

    def get_videos(self, search_word):
        search_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_videos.append(video.title)
        return search_videos

    def watch_video(self, film):
        if self.current_user and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        elif self.current_user:
            for video in self.videos:
                if film in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return self.videos

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
