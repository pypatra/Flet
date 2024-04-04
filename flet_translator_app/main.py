import flet as ft

from pages.index import view_index



def main(page: ft.Page):
    
    page.title = "Translator App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.fonts = {"manrope": "Manrope-SemiBold.ttf"}
    page.theme_mode = "light"

    page_index = view_index()

    def route_change(route) -> None:
        page.views.clear()
        if page.route == "/":
            page.views.append(page_index)


        page.update()

    def view_pop(view) -> None:
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(page_index)

    page.update()


ft.app(target=main,assets_dir="assets")
