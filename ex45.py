from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and then implement and enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print(current_scene)
        last_scene = self.scene_map.next_scene('finished')
        print(last_scene)

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "opps died",
        "shitty death",
        "imposters win",
        "you jackass",
        "suck it up"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Cafeteria(Scene):

    def enter(self):
        print(dedent(""" here is the beggining of game everynight and it's crappy """))

        action = input("what do u do > ")

        if action == "going navigation":
            print(dedent("""good choice go with everybody there"""))

            return 'navigation'
        
        elif action == "stay":
            print(dedent("""it's tiem for imposter to put his dick in you"""))

            return 'death'

        else:
            print("deos not compute")
            return 'cafeteria'

        
class Navigation(Scene):

    def enter(self):
        print(dedent(""" u reached to another point """))

        action = input("what do u do > ")

        if action == "going admin":
            print(dedent("""good choice go with everybody there"""))

            return 'admin'
        
        elif action == "stay":
            print(dedent("""it's tiem for imposter to put his dick in you"""))

            return 'death'

        else:
            print("deos not compute")
            return 'cafeteria'

class Admin(Scene):

    def enter(self):
        print(dedent(""" last place guess the imposter """))

        action = input("what do u do > ")

        if action == "hashem":
            print(dedent("""good choice u won"""))

            return 'finished'
        
        elif action == "stay":
            print(dedent("""it's tiem for imposter to put his dick in you"""))

            return 'death'

        else:
            print("deos not compute")
            return 'cafeteria'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'

class Map(object):
    
    scenes = {
        'cafeteria': Cafeteria(),
        'navigation': Navigation(),
        'admin': Admin(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('cafeteria')
a_game = Engine(a_map)
a_game.play()
