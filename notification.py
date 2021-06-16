from get_words import random_word
from get_words import info
from plyer import notification

def notify_vocab(words="God", info="The Most Merciful"):
    notification.notify(
        title=words,
        message=info,
        app_icon="assets\\dictionary.ico",
        timeout=10
    )

notify_vocab(random_word,info)