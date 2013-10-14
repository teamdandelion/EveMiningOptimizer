class Skill:
  Skill.levelToPoint = {
    0: 0,
    1: 250,
    2: 1415,
    3: 8000,
    4: 45255,
    5: 256000
  }
  def __init__(self, id, effects, primary, secondary, rank, prereqs):
    self.id = id
    self.effects = effects
    self.rank = rank
    self.primary = primary
    self.secondary = secondary
    self.prereqs = prereqs # {int skill_id: int level_required} map

  def calcSps(self, level):
    return self.rank * Skill.levelToPoint[level]

  def spsToLevel(self, targetLevel):
    return self.calcSps(targetLevel) - self.calcSps(targetLevel-1)

  def canTrain(self, character):
    for (prereq_id, prereq_level) in self.prereqs.iteritems():
      if prereq_id not in character.skills or character.skills[prereq_id] < prereq_level:
        return False
    return True
