import os
from random import randint
from ..models import Music, Backgrounds, Avatars


def generate_directory(name, x=0):
    while True:

        dir_name = (name + (' ' + str(x) if x is not 0 else '')).strip()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            os.mkdir(f'{dir_name}\\dialogues')
            os.mkdir(f'{dir_name}\\images')

            return dir_name
        else:
            x += 1


def select_music(category=None):
    if category is None:
        raise Exception('You need to add a category')

    music = Music.objects.filter(category = category)
    return music[randint(0, music.count() - 1)]


def select_background(category=None):
    if category is None:
        raise Exception('You need to add a category')

    back = Backgrounds.objects.filter(category = category)
    return back[randint(0, back.count() - 1)]


def select_avatar(selected='random'):
    if selected == 'random':
        avatars = Avatars.objects.all()
        return avatars[randint(0, avatars.count()-1)]

    if type(selected) == int:
        items = Avatars.objects.filter(id = selected)
        if items.count() == 1:
            return items.first()

    return None