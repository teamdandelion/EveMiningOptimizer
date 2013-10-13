class Skill:
  Skill.levelToPoint = {
    0: 0,
    1: 250,
    2: 1415,
    3: 8000,
    4: 45255,
    5: 256000
  }
  def __init__(self, name, effects, primary, secondary, rank, prereqs):
    self.name = name
    self.effects = effects
    self.rank = rank
    self.primary = primary
    self.secondary = secondary
    self.prereqs = prereqs # ["skillname", levelRequired] tuples

  def calcSps(self, level):
    return self.rank * Skill.levelToPoint[level]

  def spsToLevel(self, targetLevel):
    return self.calcSps(targetLevel) - self.calcSps(targetLevel-1)

  def canTrain(self, character):
    canTrain = true
    for (preReqSkill, preReqLevel) in self.prereqs:
      if
