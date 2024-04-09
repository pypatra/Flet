import flet as ft
from flet import Text, View
from googletrans import Translator
from googletrans.constants import LANGUAGES
from googletrans.models import Translated

dict_bahasa: dict[str, str] = {value.title(): key for key, value in LANGUAGES.items()}
bahasas: list[str] = list(dict_bahasa.keys())
trans: Translator = Translator()


def view_index() -> ft.View:

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

    def swicth_bahasa(e: ft.ControlEvent) -> None:
        bahasa_input.value, bahasa_output.value, input.value, output.value = (
            bahasa_output.value,
            bahasa_input.value,
            output.value,
            input.value,
        )
        e.page.update()

    def terjemahan(e: ft.ControlEvent) -> None:
        if len(input.value) <= 500:
            res: Translated = trans.translate(
                text=input.value,
                dest=dict_bahasa[bahasa_output.value],
                src=dict_bahasa[bahasa_input.value],
            )
            output.value = res.text
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
        options=[ft.dropdown.Option(text=bahasa) for bahasa in bahasas],
    )

    bahasa_output: ft.Dropdown = ft.Dropdown(
        expand=True,
        value="Indonesian",
        options=[ft.dropdown.Option(text=bahasa) for bahasa in bahasas],
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
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                bahasa_input,
                                ft.IconButton(
                                    icon=ft.icons.COMPARE_ARROWS, on_click=swicth_bahasa
                                ),
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
