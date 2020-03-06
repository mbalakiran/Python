class Team:
    def __init__(self, name, city, fee, number):
        self.name = name
        self.city = city
        self.fee = fee
        self.number = number

class User_Interface:
    def __init__(self):
        self.menu_team = {}


    def create_new_team(self, team_info):
        city = input("Please insert the city name of the team: ").lower()
        fee = input("Please enter the Fee(Paid/Not Paid: ").lower()
        if fee not in ['Paid', 'Not Paid']:
            print(F"{fee} is not a correct option. Please enter the correct value")
            return False
        number = int(input("Please enter the number of players in Team: "))
        self.menu_team[team_info] = Team(team_info, city, fee, number)
        return True

    def read_a_team(self, team_info):
        if team_info in self.menu_team:
            print(F"Name of the team is {self.menu_team[team_info].name}")
            print(F"Mentioned city of the team is {self.menu_team[team_info].city}")
            print(F"Is the Fee Paid{self.menu_team[team_info].fee}")
            print(F"The number of the players in the team are {self.menu_team[team_info].number}")
        else:
            print(F"{team_info} is not there in the list")

    def update_an_team(self,team_info, city, fee, number):
        if team_info in self.menu_team:
            if city != " ":
                self.menu_team[team_info].city = city

