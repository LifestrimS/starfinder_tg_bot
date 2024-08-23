import random

class Character:
    skills = [] #Skill

    def __init__(self, skills):
        self.skills = skills



class Skill:
    skill_name = ''
    skill_mod = ''
    skill_abil = ''
    skill_abil_mod = ''

    def __init__(self, skill_name, skill_mod, skill_abil, skill_abil_mod):
        self.skill_name = str(skill_name)
        self.skill_mod = str(skill_mod)
        self.skill_abil = str(skill_abil)
        self.skill_abil_mod = str(skill_abil_mod)

    def rollString(self):
        roll = random.randint(1,20)
        return f'Roll {self.skill_name}: {roll} + {self.skill_mod} => {roll+int(self.skill_mod)}'
    
    def shadowRollString(self):
        roll = random.randint(1,20)
        return f'Roll {self.skill_name}: {roll+int(self.skill_mod)}'