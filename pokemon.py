import random

class Boxing():
    def __init__(self):
        self.hp = 100

  def battle(self, other):
        # present the user input
        atk = int(input("1.) Jab\n2.) Straight\n3.) Hook\n4.) Uppercut\n"))
        # use branching to open up different routes for attack
        def results(stk):
            self.block = random.randint(0,5)
            dmg = stk - self.block
            other.hp = other.hp - dmg
            print(self.name, "threw a", stk, "damage swing")
            print(other.name, "did a", self.block, "block")
            print(self.name, "did", dmg, "damage to", other.name)
            print(other.name, "has", other.hp, "health")
            if other.hp > 0:
                return other.battle(self)
            else:
                print(other.name, 'is knocked out')
        if atk == 1:
            results(self.jab)
        elif atk == 2:
            results(self.straight)
        elif atk == 3:
            results(self.hook)
        elif atk == 4:
            results(self.upper)
        else:
            print("you were caught cheating!")
            
#define specifc boxer classes
class Mayweather(Boxing):
    #init the class
    def __init__(self):
        super().__init__()
        #give characteristics
        self.jab = 6
        self.straight = 10
        self.hook = 15
        self.upper = 19
        self.name = 'Mayweather'

class Evans(Boxing):
    #init the class
    def __init__(self):
        super().__init__()
        #give characteristics
        self.jab = 5
        self.straight = 5
        self.hook = 20
        self.upper = 20
        self.name = 'Evans'

class Zhou(Boxing):
    #init the class
    def __init__(self):
        super().__init__()
        #give characteristics
        self.jab = 5
        self.straight = 5
        self.hook = 5
        self.upper = 5
        self.name = 'Zhou'

class Tyson(Boxing):
    def __init__(self):
        super().__init__()
        self.jab = 8
        self.straight = 12
        self.hook = 15
        self.upper = 15
        self.name = 'Tyson'

class Pacquiao(Boxing):
    def __init__(self):
        super().__init__()
        self.jab = 12
        self.straight = 8
        self.hook = 13
        self.upper = 17
        self.name = "Pacquiao"

class Kimbo(Boxing):
    def __init__(self):
        super().__init__()
        self.jab = 15
        self.straight = 5
        self.hook = 15
        self.upper = 15
        self.name = "Kimbo"

def player_one():
    player_one = input("player one, what is your name?\nMayweather, Tyson, Pacquiao, Kimbo, Evans, Zhou?")
    #select the character
    if player_one == "Mayweather":
        #call the class
        player_one = Mayweather()
    elif player_one == "Tyson":
        player_one = Tyson()
    elif player_one == "Pacquiao":
        player_one = Pacquiao()
    elif player_one == "Kimbo":
        player_one = Kimbo()
    elif player_one == "Evans":
        player_one = Evans()
    elif player_one == "Zhou":
        player_one = Zhou()
    else:
        print("you are not registered")
    return player_one

def player_two():
    player_two = input("player two, what is your name?\nMayweather, Tyson, Pacquiao, Kimbo, Evans, Zhou?")
    if player_two == "Mayweather":
        player_two = Mayweather()
    elif player_two == "Tyson":
        player_two = Tyson()
    elif player_two == "Pacquiao":
        player_two = Pacquiao()
    elif player_two == "Kimbo":
        player_two = Kimbo()
    elif player_two == "Evans":
        player_two = Evans()
    elif player_two == "Zhou":
        player_two = Zhou()
    else:
        print("you are not registered")
    return player_two

# call functions
player_one = player_one()
player_two = player_two()

player_one.battle(player_two)
