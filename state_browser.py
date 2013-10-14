class stateBrowser:

    def __init__ (self, list_of_skills, target_skill_state):
        self.my_skills = list_of_skills
        self.end_skill_state = target_skill_state

        self.state_index = {}
        for skill in self.my_skills:
            self.state_index[skill.myTypeID] = skill.myLevel
