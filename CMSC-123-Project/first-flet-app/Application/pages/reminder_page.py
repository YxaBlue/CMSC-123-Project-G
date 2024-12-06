import flet as ft
from abc import ABC, abstractmethod

def reminder_page():
    return ft.Container(
        content=ft.Column(
            [
                ft.Switch(label="Enable Notifications", value=True),

                ft.Row(
                    [ft.TextButton(text="Medicine Intake", width=150),
                     ft.TextButton(text="Appointment", width=150)], 
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),

                # Create List of Reminder Cards
                ft.ListView(
                    controls=[
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.ListTile(
                                            title=ft.Container(
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text("Reminder"),
                                                        ft.ElevatedButton("Check"),
                                                    ],
                                                    spacing=5,
                                                )
                                            )
                                        ),
                                        ft.Container(
                                            content=ft.Column(
                                                controls=[
                                                    ft.Text("Sum reminder hereeee"),
                                                    ft.Text("Go do check up or soomething")
                                                ],
                                                spacing=5,
                                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                            ),
                                            padding=ft.padding.only(left=20)
                                        ),
                                    ],
                                ),
                                padding=10,
                            )
                        )
                        for i in range(5)
                    ],
                    spacing = 10,
                    height=500,
                    expand=True
                )
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
        ),


        visible=False
    )







class Reminder_Card(ABC):
    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def __create_reminder_card(self):
        pass

class Appointments_Card(Reminder_Card):
    def __init__(self, title:str, content):
        self.__CardTitle = title
        self.__content = content
        self.__card = self.__create_reminder_card()

    def __create_reminder_card(self):
        return ft.Card(
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            # Title of Reminder Card + Cupertino Check box
                            ft.ListTile(
                                title=ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(self.__CardTitle),
                                        ],
                                    )
                                ),
                                trailing=ft.CupertinoCheckbox(value=False),
                            ),

                            # Contents of a reminder card
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(self.__content),
                                    ],
                                    spacing=5,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                ),
                                padding=ft.padding.only(left=20, right=20)
                            ),
                        ],
                    ),
                    
                    padding=ft.padding.symmetric(vertical=5),
                )
        )

    def remove(self):
        # This is a deconstructor
        # Will figure out 
        
        # When reminder is checked out
        # This should delete the reminder card and possibly delete the description
        # Another alternative for the sake of file logging, we could add a member
        # variable presciption indicating that the reminder is done
        pass

class MedIntake_Card(Reminder_Card):
    def __init__(self, title:str, content):
        self.__CardTitle = title
        self.__content = content
        self.__card = self.__create_reminder_card() 

    def __create_reminder_card(self):
        return ft.Card(
            content=ft.Container(
                    content=ft.Column(
                        controls=[
                            # Title of Reminder Card + Cupertino Check box
                            ft.ListTile(
                                title=ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(self.__CardTitle),
                                        ],
                                    )
                                ),
                                trailing=ft.CupertinoCheckbox(value=False),
                            ),

                            # Contents of a reminder card
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(self.__content),
                                    ],
                                    spacing=5,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                ),
                                padding=ft.padding.only(left=20, right=20)
                            ),
                        ],
                    ),
                    
                    padding=ft.padding.symmetric(vertical=5),
                )
        )

    def remove(self):
        # This is a deconstructor
        # Will figure out 
        
        # When reminder is checked out
        # This should delete the reminder card and possibly delete the description
        # Another alternative for the sake of file logging, we could add a member
        # variable presciption indicating that the reminder is done
        pass



class Reminder_Page:
    # Function to initialize Reminder Page
    def __init__(self, page: ft.Page):
        self.page = page
        self.page_container = self.__create_Reminder_page()

        # User always lands in appointment sub page when opening Reminder Page
        self.current_view = "Appointment Subpage"


    #-------------------------------------------------------------------------------------------------#
    ## --------------------------------- FOR FUNCTIONALITY OF UI ----------------------------------- ##
    #-------------------------------------------------------------------------------------------------#
    






    #-------------------------------------------------------------------------------------------------#
    ## --------------------------------- FOR FUNCTIONALITY OF UI ----------------------------------- ##
    #-------------------------------------------------------------------------------------------------#
    # Creates a list of reminder cards to be displayed
    # Needed to modify so that it accepts the details of prescription from files
    def __create_reminder_cards_list(self, newCard:Reminder_Card):
        return ft.ListView(
                    controls=[
                            newCard
                            for i in range(5)
                    ],
                    spacing=10,
                    height=500,
                    expand=True
                )
    

    #
    def __create_Reminder_page(self):
        # For buttons' functionality
        def show_MedIntake_Subpage(self):
            pass


        # Create buttons for clicking and ticking events
        MedIntake_Subpage_btn = ft.ElevatedButton("Medicine Intake", width=160)
        Appointment_Subpage_btn = ft.ElevatedButton("Appointment", width=160)
        Reminder_ChckBox = ft.CupertinoCheckbox


        # For validation
        def reminder_Done(self):
            pass


        return ft.Container(
            content=ft.Column(
                [
                    ft.Switch(label="Enable Notifications", value=True),

                    ft.Row(
                        [ft.ElevatedButton(text="Medicine Intake", width=160),
                        ft.ElevatedButton(text="Appointment", width=160)], 
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                    
                    # Create List of Reminder Cards
                    ft.ListView(
                        controls=[

                        ],
                        spacing = 10,
                        height=500,
                        expand=True
                    )
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
            ),

            visible=False
        )
    


    
        
