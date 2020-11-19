from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("this scene in not yet configured!")
        print("sub class it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def Play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

    
class Death(Scene):
    quips = [
        "you died you kinda suck at this ,",
        "your mom would be proud ... if she were smarter",
        "such a loooooooser",
        "i have a small puppy that's better at this.",
        "you're worse than your dad's jokes"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])

        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent(""""cooooooooooooooooooooooooooooooooomeeeeeeeeeeeeeeeeeeeent"""))

        action = input("> ")
        
        if action == "shoot!":
            print(dedent(""" quick on draw"""))

            return 'death'
        elif action == "dodge!":
            print(dedent("""dodge like a world class boxor"""))

            return 'death'

        elif action == "tell a joke!":
            print(dedent("""lucky for you """))

            return 'laser_weapon_armory'

        else:
            print("does not compute")
            return 'central_corridor'
            
        