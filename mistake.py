# object which represents an individual eve skill
class skill:

    # constructor takes following arguments
    # typeID: integer ID of skill in API skill tree
    # rank: integer training requirement coefficient of skill
    # prereqs: dictionary of typeIDs and levels of required skills
    # primary: 3 letter string with beginning of primary attribute name
    # secondary: 3 letter string with beginning of secondary attribute name
    def __init__ (self, typeID, rank, prereqs, level, primary, secondary):
        self.myTypeID = typeID
        self.myRank = rank
        self.myPrereqs = prereqs
        self.myLevel = level
        self.myPrimary = primary
        self.mySecondary = secondary
        self.baseSkillCost = {1:250, 2:1165, 3:6585, 4:37255, 5:210745}

    def trainTime (self, attributes):
        skillPointTarget = self.baseSkillCost[self.myLevel + 1] * self.myRank
        skillPerMinute = attributes[self.myPrimary] + (attributes[self.mySecondary] / 2)
        return (skillPointTarget / skillPerMinute)

    def canTrain (self, state_index):
        passes = 1

        if self.myLevel >= 5:
            passes = 0
        
        for skill in self.myPrereqs.keys():
            if not skill in state_index:
                passes = 0
            if skill in state_index:
                if state_index[skill].myLevel < self.myPrereqs[skill]:
                    passes = 0
                    
        return passes

def test():

    attributes = {'int':22, 'mem':22, 'cha':20, 'wil':22, 'per':22}

    science = skill(3402, 1, {}, 5, 'int', 'mem')
    mining = skill(3386, 1, {}, 5, 'mem', 'per')
    astrogeology = skill(3410, 3, {3402:4, 3386:4}, 0, 'int', 'mem')

    skill_index = {3402:science, 3386:mining}
    
    if astrogeology.canTrain(skill_index):
        print('rad')
    else:
        print('bummer')

test()
