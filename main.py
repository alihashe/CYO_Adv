## Author: Ali Hashem
## Choose your own adventure game
import time as t

class Charater:
    """The object used to define character stats and descriptions."""
    def __init__(self, race, classs, description, hth, gld, atk, deff, int, fth, luck):
        self.race = race
        self.classs = classs
        self.description = description
        self.hth = hth
        self.gld = gld
        self.atk = atk
        self.deff = deff
        self.int = int
        self.fth = fth
        self.luck = luck 

    def getRace(self):
        """Returns the race of the character.\n Note: For now, only human characters."""
        return self.race

    def setRace(self, raceInput="human"):
        """Sets the race of the character.\n Note: For now, only human characters."""
        self.race = raceInput

    def getHth(self):
        """Returns the amount of health a character currently has."""
        return self.hth

    def setHth(self, hthInput=0):
        """Sets the initial amount of health for a character."""
        self.hth = hthInput

    def addHth(self, hthAdd):
        """Adds more health to the character."""
        self.hth += hthAdd

    def subHth(self, hthSub):
        """Subtracts gold away from character inventory."""
        self.hth -= hthSub

    def getGld(self):
        """Returns the amount of gold a character is currently carrying."""
        return self.gld

    def setGld(self, gldInput=0):
        """Sets the initial amount of gold on the character."""
        self.gld = gldInput

    def addGld(self, gldAdd):
        """Adds more gold to the character inventory."""
        self.gld += gldAdd

    def subGld(self, gldSub):
        """Subtracts gold away from character inventory."""
        self.gld -= gldSub
    
    def getAtk(self):
        """Returns attack stat for the character."""
        return self.atk

    def setAtk(self, atkNum=0):
        """Sets initial attack stat for the character."""
        self.atk = atkNum

    def addAtk(self, atkAdd):
        """Adds to the attack stat for the character."""
        self.atk += atkAdd

    def subAtk(self, atkSub):
        """Subtracks from the attack stat for the character."""
        self.atk -= atkSub

    def getDeff(self):
        """Returns defense stat for the character."""
        return self.deff

    def setDeff(self, deffNum=0):
        """Sets initial defense stat for the character."""
        self.deff = deffNum

    def addDeff(self, deffAdd):
        """Adds to the defense stat for the character."""
        self.deff += deffAdd

    def subDeff(self, deffSub):
        """Subtracks from the defense stat for the character."""
        self.deff -= deffSub

    def getInt(self):
        """Returns intelligence stat for the character."""
        return self.int

    def setInt(self, intNum=0):
        """Sets initial intelligence stat for the character."""
        self.int = intNum

    def addInt(self, intAdd):
        """Adds to the intelligence stat for the character."""
        self.int += intAdd

    def subInt(self, intSub):
        """Subtracks from the intelligence stat for the character."""
        self.int -= intSub

    def getFth(self):
        """Returns faith stat for the character."""
        return self.fth

    def setFth(self, fthNum=0):
        """Sets initial faith stat for the character."""
        self.fth = fthNum

    def addFth(self, fthAdd):
        """Adds to the faith stat for the character."""
        self.fth += fthAdd

    def subFth(self, fthSub):
        """Subtracks from the faith stat for the character."""
        self.fth -= fthSub

    def getLuck(self):
        """Returns luck stat for the character."""
        return self.luck

    def setLuck(self, luckNum=0):
        """Sets initial luck stat for the character."""
        self.luck = luckNum

    def addLuck(self, luckAdd):
        """Adds to the luck stat for the character."""
        self.luck += luckAdd

    def subLuck(self, luckSub):
        """Subtracks from the luck stat for the character."""
        self.luck -= luckSub

    def getClasss(self):
        """Returns the character class."""
        return self.classs

    def setClasss(self, classsInput="warrior"):
        """Sets the character starting class."""
        classsInput = self.classs
        self.setHth(24)
        if classsInput == "warrior":
            self.description = "The most basic class.\n Use your superior strength to muscle through most problems.\n However, be wary of more intelligent foes and obstacles."
            self.setAtk(10)
            self.setDeff(9)
            self.setInt(3)
            self.setFth(4)
            self.setLuck(4)
            self.addGld(20)
        if classsInput == "mage":
            self.description = ""
            self.setAtk(4)
            self.setDeff(6)
            self.setInt(10)
            self.setFth(5)
            self.setLuck(5)
            self.addGld(20)
        if classsInput == "thief":
            self.description = ""
            self.setAtk(8)
            self.setDeff(7)
            self.setInt(3)
            self.setFth(2)
            self.setLuck(9)
            self.addGld(25)
        if classsInput == "apostle":
            self.description = "The strangest of the classes.\n You may not be the strongest, smartest, or luckiest of the classes,\n but unique events may only be available to you."
            self.setAtk(4)
            self.setDeff(4)
            self.setInt(4)
            self.setFth(13)
            self.setLuck(5)
            self.addGld(15)
        if classsInput == "peasant":
            self.description = "The hardest class.\n Fumble through the world with nothing\n but your intuition and sheer dumb luck."
            self.setAtk(2)
            self.setDeff(1)
            self.setInt(1)
            self.setFth(2)
            self.setLuck(24)
            self.addGld(5)