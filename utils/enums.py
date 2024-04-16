from enum import Enum


class UserType(Enum):
    ATHLETE = 1
    COACH = 2
    REFEREE = 3
    FAN = 4
    CAPTAIN = 5
    
    @staticmethod
    def fetch_items(key):
        try:
            key = int(key)
            item = __class__(key)
            return item.name
        except ValueError as e:
            print(f"Error: {e}") 


class CardType(Enum):
    GOLD = 1
    PLATINUM = 2
    DIAMOND = 3

    @staticmethod
    def fetch_items(key):
        try:
            key = int(key)
            item = __class__(key)
            return item.name
        except ValueError as e:
            print(f"Error: {e}") 
    
class SportType(Enum):

    BASEBALL = 1
    BASKETBALL = 2
    CHEERLEADING = 3
    CROSS_COUNTRY = 4
    FIELD_HOCKEY = 5
    FOOTBALL = 6
    GYMNASTICS = 7
    ICE_HOCKEY = 8
    SOCCER = 9
    SOFTBALL = 10
    SWIMMING = 11
    TENNIS = 12
    VOLLEYBALL = 13
    WRESTLING = 14

    @staticmethod
    def fetch_items(key):
        try:
            key = int(key)
            item = __class__(key)
            return item.name
        except ValueError as e:
            print(f"Error: {e}") 


class SchoolGrade(Enum):
    ELEMENTARY_SCHOOL = 1
    MIDDLE_SCHOOL = 2
    JUNIOR_HIGH_SCHOOL = 3
    SENIOR_HIGH_SCHOOL = 4
    PREPARATORY_SCHOOL = 5

    @staticmethod
    def fetch_items(key):
        try:
            key = int(key)
            item = __class__(key)
            return item.name
        except ValueError as e:
            print(f"Error: {e}") 


