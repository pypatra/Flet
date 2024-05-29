import flet as ft
from flet_core import View

from pages.form_login import view_login
from pages.form_signup import view_signup
from pages.index import view_index


def main(page: ft.Page):

    page.title = "Flet Form Login"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.fonts = {"manrope": "Manrope-SemiBold.ttf"}
    page.theme_mode = "light"

    page_login: View = view_login()
    page_signup: View = view_signup()
    page_index: View = view_index()

    def route_change(route: object) -> None:
        page.views.clear()
        if page.route == "/home":
            page.views.append(page_index)

        if page.route in  ["/login","/"]:
            page.views.append(page_login)

        if page.route == "/signup":
            page.views.append(page_signup)

        page.update()

    def view_pop(view: object) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(page_login)

    page.update()


ft.app(main, assets_dir="assets")
