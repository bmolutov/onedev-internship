import random


def get_avatar_path(instance, filename):
    random_number = random.randint(0, 2048)
    name, extension = filename.split('.')
    return 'avatars/{}/{}.{}'.format(instance.id, random_number, extension)
