from enum import Enum, auto, Flag, unique


@unique
class AgeGroup(Flag):
    KID = 1
    ADOLESCENT = 32
    ADULT = 128


kids = AgeGroup.KID | AgeGroup.ADOLESCENT

print(kids)
