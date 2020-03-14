from ClassTeam import Team

class User_Interface:
    def __init__(self):
        self.menu_team = {}


    def create_new_team(self, team_info):
        city = input("Please insert the city name of the team: ").lower()
        fee = input("Please enter the Fee(Paid/Not Paid: ").lower()
        if fee not in ['paid', 'not paid']:
            print(F"{fee} is not a correct option. Please enter the correct value")
            return False
        number = int(input("Please enter the number of players in Team: "))
        self.menu_team[team_info] = Team(team_info, city, fee, number)
        return True

    def read_a_team(self, team_info):
        if team_info in self.menu_team:
            print(F"\nName of the team is {self.menu_team[team_info].name}")
            print(F"Mentioned city of the team is {self.menu_team[team_info].city}")
            print(F"Is the Fee Paid{self.menu_team[team_info].fee}")
            print(F"The number of the players in the team are {self.menu_team[team_info].number}")
        else:
            print(F"{team_info} is not there in the list")

    def update_an_team(self,team_info, city, fee, number):
        if team_info in self.menu_team:
            if city != "":
                self.menu_team[team_info].city = city
            if fee != " ":
                self.menu_team[team_info].fee = fee
            if number != " ":
                self.menu_team[team_info].number = number
            else:
                print(F"{team_info} has not found in the list")

    def delete_an_team(self,team_info):
        if team_info in self.menu_team:
            del self.menu_team[team_info]
            print(F"{team_info} has been successfully deleted")
        else:
            print(F"{team_info} has not found in the list")

    def exit(self):
        print("Thank you")

    def user_interface_menu(self):

        n = 1
        choice = 99
        create_an_team = 1
        read_an_team = 2
        update_an_team = 3
        delete_an_team = 4
        exit = 0

        while choice != exit:

            print("\n1. Add a Team")
            print("2. Read a Team")
            print("3. Update a Team")
            print("4. Delete a Team")
            print("0. Exit")

            try:
                choice = int(input("Please enter a option: "))
            except ValueError as err:
                print(err,"Is not a valid option")

            if choice == create_an_team:
                name = input("Please enter you team name: ").lower()
                if self.create_new_team(name):
                    print(F"{name} has been created")

            elif choice == read_an_team:
                team_info = input("Enter the team name for the search: ").lower()
                self.read_a_team(team_info)

            elif choice == update_an_team:
                team_info = input("Please enter the team name for the update: ").lower()
                if team_info in self.menu_team:
                    city = input("Please Enter the new city of the team or leave it blank: ").lower()
                    fee = input("Please enter the fee status or leave it blank: ").lower()
                    number = input("Please enter the size of the team or leave it blank: ").lower()
                    self.update_an_team(team_info,city,fee,number)
                    print(F"{team_info} has been sucessfully updated")
                else:
                    print(F"{team_info} is not in the list")

            elif choice == delete_an_team:
                team_info = input("Please enter the team name to delete")
                if team_info in self.menu_team:
                    self.delete_an_team(team_info)
                    print(F"{team_info} has been deleted")
                else:
                    print(F"{team_info} is not in the list")

            else:
                print("Thanks")

myteam = User_Interface()
myteam.user_interface_menu()
