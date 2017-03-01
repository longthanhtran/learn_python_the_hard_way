#!/usr/bin/env python3.6

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = ["Happy birthday to you",
              "I don't want to get sued",
              "So I'll stop right there"]

bulls_on_parade = ["They rally around tha family",
                   "With pockets full of shells"]
