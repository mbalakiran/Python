from ClassTeam import Team
from datetime import datetime, date

class User_Interface:
    def __init__(self):
        self.menu_team = {}


    def create_new_team(self, team_info):
        city = input("Please insert the city name of the team: ").lower()
        fee = input("Please enter the Fee(Paid/Not Paid): ").lower()
        if fee not in ['paid', 'not paid']:
            print(F"{fee} is not a correct option. Please enter the correct value")
            return False
        number = int(input("Please enter the number of players in Team: "))
        self.menu_team[team_info] = Team(team_info, city, fee, number)
        return True

    def read_a_team(self, team_info):
        if team_info in self.menu_team:
            print(F"\nName of the team is: {self.menu_team[team_info].name}")
            print(F"Mentioned city of the team is: {self.menu_team[team_info].city}")
            print(F"Is the Fee Paid: {self.menu_team[team_info].fee}")
            print(F"The number of the players in the team are: {self.menu_team[team_info].number}")
            print(F"The amount paid by the team is: {self.menu_team[team_info].fee_amount}")
            registeredtime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            print(F"The team has been registered on: ",registeredtime)
            print(F"{self.menu_team[team_info].name} team is "
                  F"{(date.today() - self.menu_team[team_info].registered).days} days old \n")
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

    def teams_enrolled(self):
        print(F"The number of the teams which have been enrolled till now are: {len(self.menu_team)}")

    def sum_of_amount_paid(self):
        print(F"The sum amount paid by all teams: {sum(int(self.menu_team[i].fee_amount) for i in self.menu_team)}")

    def teams_with_fee_not_paid(self):
        not_paid = len([self.menu_team[i]
                       for i in self.menu_team
                       if self.menu_team[i].fee == "not paid"])
        print(F"\n{round(not_paid/len(self.menu_team)*100, 2)}% have not paid the fees")

    def exit(self):
        print("Thank you")

    def user_interface_menu(self):

        n = 1
        choice = 99
        create_an_team = 1
        read_an_team = 2
        update_an_team = 3
        delete_an_team = 4
        teams_enrolled = 5
        total_sum_of_fees_paid = 6
        percentage_of_teams_unpaid = 8
        exit = 0

        while choice != exit:

            print("\n1. Add a Team")
            print("2. Read a Team")
            print("3. Update a Team")
            print("4. Delete a Team")
            print("5. Number of the teams Enrolled")
            print("6. Total sum of the fees Paid")
            print("7. Percentage of the teams who have not paid fees")
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

            elif choice == teams_enrolled:
                self.teams_enrolled()

            elif choice == total_sum_of_fees_paid:
                self.sum_of_amount_paid()

            elif choice == percentage_of_teams_unpaid:
                self.teams_with_fee_not_paid()

            else:
                print("Thanks")

myteam = User_Interface()
myteam.user_interface_menu()
