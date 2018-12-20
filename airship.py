class Airship():
    FIRE = 'fire'
    ARMOR = 'armor'
    SPEED = 'speed'
    LUCK = 'luck'

    def __init__(self, name, fire, armor, speed, luck):
        self.name = name
        self.fire = fire
        self.armor = armor
        self.speed = speed
        self.luck = luck

    def stats(self):
        return(self.armor, self.fire, self.luck, self.speed)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{} (f{} a{} s{} l{})".format(
            self.name,
            self.fire,
            self.armor,
            self.speed,
            self.luck
        )


airships = [
    #  Name, fire, armor, speed, luck
    Airship("Evil Eye Tyrant", 43, 18, 28, 18),
    Airship("Shadow Dragon", 38, 23, 18, 28),
    Airship("Devil", 36, 35, 18, 18),
    Airship("Behemoth's Claw", 35, 23, 28, 23),
    Airship("Universal Master", 33, 33, 20, 23),
    Airship("Goblin", 33, 28, 28, 20),
    Airship("Ufo", 33, 25, 28, 23),
    Airship("Carribean", 33, 23, 23, 28),
    Airship("Steel Fist", 33, 23, 33, 18),
    Airship("Smuggler", 33, 23, 33, 20),
    Airship("Hovering", 33, 20, 28, 28),
    Airship("Montezuma", 33, 19, 19, 38),
    Airship("Mushashi", 33, 18, 23, 33),
    Airship("Behemoth's Horn", 28, 35, 23, 23),
    Airship("Tech Ball", 28, 33, 23, 23),
    Airship("Gumball", 28, 28, 26, 25),
    Airship("Void Stingray", 28, 28, 20, 33),
    Airship("The Behemoth", 28, 28, 28, 28),
    Airship("Orbit Satellite", 28, 28, 33, 20),
    Airship("Elemental", 28, 27, 21, 33),
    Airship("Cube", 28, 27, 27, 27),
    Airship("Lucifer", 28, 23, 33, 25),
    Airship("Alastor", 28, 23, 30, 28),
    Airship("Viking Fighter", 27, 31, 23, 28),
    Airship("Eternal Tower", 27, 27, 28, 27),
    Airship("Alliance", 25, 33, 28, 23),
    Airship("Frozen Throne", 25, 33, 23, 28),
    Airship("Arcane Snail", 25, 33, 18, 33),
    Airship("Chimera Wings", 25, 23, 26, 33),
    Airship("Yamato", 23, 38, 28, 18),
    Airship("Eden 1", 23, 32, 29, 25),
    Airship("Eden 2", 23, 32, 29, 25),
    Airship("Eden 3", 23, 32, 29, 25),
    Airship("Overlord", 23, 30, 33, 23),
    Airship("Universal Falcon", 23, 28, 23, 35),
    Airship("Behemoth's Heart", 23, 28, 23, 35),
    Airship("Night Wing", 23, 25, 33, 28),
    Airship("Traveller", 23, 25, 23, 38),
    Airship("Darla Montes", 23, 23, 25, 38),
    Airship("Behemoth's Wings", 23, 23, 35, 28),
    Airship("Sixth Heaven", 23, 23, 33, 30),
    Airship("Eternal Throne", 21, 33, 27, 28),
    Airship("Prometheus", 21, 27, 33, 28),
    Airship("Knights of the Round", 19, 38, 31, 19)
]
