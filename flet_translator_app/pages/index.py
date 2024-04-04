import flet as ft
from flet import Text, View
from translate import Translator


def view_index() -> ft.View:
    translator: Translator = Translator(to_lang="id")

    def check_input(e: ft.ControlEvent) -> None:
        e.control.counter_text = f"Jumlah Huruf {(500 - len(input.value)) if len(input.value) <= 500 else 0} Tersisa"
        e.page.update()

    def thememode(e: ft.ControlEvent) -> None:
        if e.page.theme_mode == "dark":
            e.page.theme_mode = "light"
            e.control.icon = ft.icons.LIGHT_MODE
            input.border_color = "dark"
            output.border_color = "dark"
            bahasa_input.border_color = "dark"
            bahasa_output.border_color = "dark"
            e.page.update()
        else:
            e.page.theme_mode = "dark"
            input.border_color = "white"
            output.border_color = "white"
            bahasa_input.border_color = "white"
            bahasa_output.border_color = "white"
            e.control.icon = ft.icons.DARK_MODE
            e.page.update()

    def terjemahan(e: ft.ControlEvent) -> None:
        if len(input.value) <= 500:
            output.value = translator.translate(input.value)
            e.page.update()
        else:
            input.error_text = "Maksimal 500 huruf"
            input.value = ""
            e.page.update()

    def clear_output(e: ft.ControlEvent) -> None:
        output.value = ""
        input.error_text = ""
        input.counter_text = ""
        e.page.update()

    def clear_input(e: ft.ControlEvent) -> None:
        input.value = ""
        e.page.update()

    bahasa_input: ft.Dropdown = ft.Dropdown(
        expand=True,
        value="English",
        options=[
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Indonesia"),
        ],
    )

    bahasa_output: ft.Dropdown = ft.Dropdown(
        expand=True,
        value="Indonesia",
        options=[
            ft.dropdown.Option("Indonesia"),
            ft.dropdown.Option("English"),
        ],
    )

    input: ft.TextField = ft.TextField(
        hint_text="Masukan text",
        # expand=True,
        multiline=True,
        on_focus=clear_output,
        on_change=check_input,
    )

    output: ft.TextField = ft.TextField(
        expand=True,
        hint_text="Terjemahan",
        multiline=True,
    )

    return View(
        route="/",
        vertical_alignment="center",
        horizontal_alignment="center",
        controls=[
            ft.Container(
                width=800,
                padding=24,
                border_radius=24,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=4,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                ),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                # bgcolor="yellow",
                content=ft.Column(
                    horizontal_alignment="center",
                    height=800,
                    controls=[
                        ft.Row(
                            alignment="end",
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.LIGHT_MODE, on_click=thememode
                                )
                            ],
                        ),
                        ft.Text(
                            value="Translator App",
                            font_family="manrope",
                            theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                        ),
                        ft.Divider(height=24, color="transparent"),
                        ft.Row(
                            alignment="center",
                            controls=[
                                bahasa_input,
                                ft.IconButton(icon=ft.icons.COMPARE_ARROWS),
                                bahasa_output,
                            ],
                        ),
                        ft.Divider(height=24, color="transparent"),
                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            height=400,
                            controls=[
                                ft.Column(
                                    expand=True,
                                    controls=[
                                        input,
                                        ft.IconButton(
                                            icon=ft.icons.DELETE_OUTLINE,
                                            on_click=clear_input,
                                        ),
                                    ],
                                ),
                                output,
                            ],
                        ),
                        ft.Divider(height=24, color="transparent"),
                        ft.FilledButton(
                            height=48,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=4),
                            ),
                            content=Text(
                                value="Terjemah",
                                font_family="manrope",
                            ),
                            on_click=terjemahan,
                        ),
                    ],
                ),
            )
        ],
    )
