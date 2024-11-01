import random

class Hiragana:
    hiragana_dict_romaji = {
        "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
        "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
        "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
        "ta": "た", "chi": "ち", "tsu": "つ", "te": "て", "to": "と",
        "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
        "ha": "は", "hi": "ひ", "fu": "ふ", "he": "へ", "ho": "ほ",
        "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
        "ya": "や", "yu": "ゆ", "yo": "よ",
        "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
        "wa": "わ", "wo": "を", "n": "ん"
    }

    _hiragana_dict_cache = None

    @classmethod
    def Hiragana_gen(cls):
        """生成并缓存所有平假名实例"""
        if cls._hiragana_dict_cache is None:
            cls._hiragana_dict_cache = {romaji: f"media\\{romaji}.jpg" for romaji in cls.hiragana_dict_romaji}
        return cls._hiragana_dict_cache

    @classmethod
    def random_gen(cls):
        """返回一个随机的平假名和图片路径"""
        hiragana_dict = cls.Hiragana_gen()
        random_key = random.choice(list(hiragana_dict.keys()))
        return random_key, hiragana_dict[random_key]


if __name__ == '__main__':
    for _ in range(5):
        romaji, image_path = Hiragana.random_gen()
        print(f"random hiragana -> Romaji: {romaji}, Image Path: {image_path}")
