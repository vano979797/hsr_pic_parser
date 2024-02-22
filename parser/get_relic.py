from get_pic_info import get_pic


def get_relic_icon_pic(name):
    url = f"https://starrail.mana.wiki/c/relicSets/{name}"
    type_pic = 'Icon'
    return get_pic(url, type_pic)