from get_pic_info import get_pic


def get_char_pic(name):
    url = f"https://starrail.mana.wiki/c/characters/{name}"
    type_pic = 'Background Image - Main'
    return get_pic(url, type_pic)


def get_char_icon_pic(name):
    url = f"https://starrail.mana.wiki/c/characters/{name}"
    type_pic = 'Icon'
    return get_pic(url, type_pic)

