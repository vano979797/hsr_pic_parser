from get_pic_info import get_pic


def get_cone_pic(name):
    url = f"https://starrail.mana.wiki/c/lightCones/{name}"
    type_pic = 'Character Primary Image'
    return get_pic(url, type_pic)


def get_cone_icon_pic(name):
    url = f"https://starrail.mana.wiki/c/lightCones/{name}"
    type_pic = 'Icon'
    return get_pic(url, type_pic)