class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                "I don't want to get used",
                "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                "With pockets full of shells"])

sheldon_cooper = Song(["soft kitty warm kitty little ball of fur",
                "happy kitty sleepy kitty pur pur pur"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
print("\n")
sheldon_cooper.sing_me_a_song()