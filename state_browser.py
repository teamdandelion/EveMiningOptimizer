class stateBrowser:

    def __init__ (self, skill_set):

        self.end_skill_state = {}
        for skill in skill_set:
            end_skill_state[skill.myTypeID] = 5

        self.state_index = {}
        for skill in skill_set:
            self.state_index[skill.myTypeID] = skill

        self.aggregate_mining = 0;

    def update_index ():
        for skill in self.my_skills:
            self.state_index[skill.myTypeID] = skill.myLevel
        
