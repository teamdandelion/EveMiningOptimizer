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

    # trainTime takes in a dictionary of attribute scores matched to skill name
    # keys and returns time to train the skill to the next rank in minutes
    def trainTime (self, attributes):
        skillPointTarget = self.baseSkillCost[self.myLevel + 1] * self.myRank
        skillPerMinute = attributes[self.myPrimary] + (attributes[self.mySecondary] / 2)
        return (skillPointTarget / skillPerMinute)

    def canTrain (self, state_index):
        for skill in prereqs.keys():
            if skill in state_index and state_index[skill] >= prereqs[skill]:
                return true
            else:
                return false

def test():

    # sample set of attributes
    attributes = {'int':22, 'mem':22, 'cha':20, 'wil':22, 'per':22}

    # create the mining skill with accurate parameters, set current level to 3
    mining = skill(3386, 1, {}, 3, 'mem', 'per')
    print(mining.trainTime(attributes))

    # ^^ tests match game data ^^

# test()
