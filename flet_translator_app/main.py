import flet as ft

from pages.index import view_index


def main(page: ft.Page) -> None:
    page.title = "Translator App | Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"manrope": "Manrope-SemiBold.ttf"}
    page.theme_mode = ft.ThemeMode.LIGHT

    page_index: ft.View = view_index()

    def route_change(route) -> None:
        page.views.clear()
        if page.route == "/":
            page.views.append(page_index)

        page.update()

    def view_pop(view) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(page_index)

    page.update()


ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
