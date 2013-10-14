class Fitting:
  def __init__(self, ship, modules):
    self.ship = ship
    self.modules = modules
    self.effects =

  def canFit(self, skillDict):
    pg_available = self.ship.calc_pg(skillDict)
    cpu_available = self.ship.calc_pg(skillDict)


    for mod in self.modules:
