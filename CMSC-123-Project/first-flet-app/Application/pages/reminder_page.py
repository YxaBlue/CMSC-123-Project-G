import flet as ft

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


class Reminder_Page:
    # Function to initialize Reminder Page
    def __init__(self, page: ft.Page):
        self.page = page
        self.page_container = self._create_reminder_page()

        # User always lands in appointment sub page when opening Reminder Page
        self.current_view = "Appointment Subpage"

    # Create a list of reminders [Test]
    def _create_reminders_list():
        return ft.ListView(
            controls=[
                # This create's a card containing the reminders
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ListTile(
                                    title=ft.Text(f"Reminder {i+1}"),
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
                for i in range(3)
            ],
            spacing = 10,
            height=300,
            expand=True
        )
    

    


    
        
