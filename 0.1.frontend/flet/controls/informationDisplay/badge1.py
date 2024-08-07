import flet as ft

def main(page: ft.Page):
    page.title = "Badge on a NavigationBar destination icon"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon_content=ft.Badge(
                    content=ft.Icon(ft.icons.EXPLORE),
                    small_size=10,
                ),
                label="Explore",
            ),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon_content=ft.Badge(content=ft.Icon(ft.icons.PHONE), text="10")
            ),
        ]
    )
    page.add(ft.Text("Body!"))


ft.app(target=main)