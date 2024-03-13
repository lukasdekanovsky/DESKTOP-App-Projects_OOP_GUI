import pandas

class StateManager():


    def __init__(self):
        self.score = 0
        self.states_to_guess = 50
        self.list_to_learn = []
        self.open_data()
        
    def open_data(self):
        data = pandas.read_csv("50_states.csv")
        list_of_states = data["state"].to_list()
        self.list_to_learn = list_of_states

    def check_correct_answer(self, answer):
        data = pandas.read_csv("50_states.csv")
        list_of_states = data["state"].to_list()  # all states in the list
        if answer in list_of_states:
            list_of_states.remove(answer)
            position = data[data["state"] == answer]
            self.increase_score()
            self.update_to_learn_list(answer)
            return (position.x, position.y)

    def update_to_learn_list(self, answer):
        self.list_to_learn.remove(answer)

    def increase_score(self):
        self.score += 1
        self.states_to_guess -= 1

    def create_learning_csv(self):
        new_data = pandas.DataFrame(self.list_to_learn)
        new_data.to_csv("states_to_learn.csv")
    

    

