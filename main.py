## Author: Ali Hashem
## Choose your own adventure game
import time as t

class Charater:
    def __init__(self, race, classs, description, atk, deff, mag, fth, luck):
        self.race = race
        self.classs = classs
        self.description = description
        self.atk = atk
        self.deff = deff
        self.mag = mag
        self.fth = fth
        self.luck = luck

    def getRace(self):
        return self.race

    def setRace(self, raceInput="human"):
        raceInput = self.race
    
    def getAtk(self):
        return self.atk

    def setAtk(self, atkNum=0):
        self.atk = atkNum

    def getDeff(self):
        return self.deff

    def setMag(self, magNum=0):
        self.mag = magNum

    def getMag(self):
        return self.mag

    def setDeff(self, deffNum=0):
        self.deff = deffNum

    def getFth(self):
        return self.fth

    def setFth(self, fthNum):
        self.fth = fthNum

    def getLuck(self):
        return self.luck

    def setLuck(self, luckNum):
        self.luck = luckNum

    def getClasss(self):
        return self.classs

    def setClasss(self, classsInput="warrior"):
        classsInput = self.classs
        if classsInput == "warrior":
            self.description = ""
        if classsInput == "mage":
            self.description = ""
        if classsInput == "thief":
            self.description = ""
        if classsInput == "apostle":
            self.description = ""