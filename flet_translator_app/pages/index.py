import asyncio

import flet as ft
from flet import View
from googletrans import Translator
from googletrans.constants import LANGUAGES
from googletrans.models import Translated

dict_bahasa: dict[str, str] = {value.title(): key for key, value in LANGUAGES.items()}
bahasas: list[str] = list(dict_bahasa.keys())
trans: Translator = Translator()


def view_index() -> ft.View:
    def theme_mode(e: ft.ControlEvent) -> None:
        if e.page.theme_mode == "dark":
            e.page.theme_mode = "light"
            e.control.icon = ft.icons.LIGHT_MODE
            input_text.border_color = "dark"
            output.border_color = "dark"
            bahasa_input.border_color = "dark"
            bahasa_output.border_color = "dark"
            e.page.update()
        else:
            e.page.theme_mode = "dark"
            input_text.border_color = "white"
            output.border_color = "white"
            bahasa_input.border_color = "white"
            bahasa_output.border_color = "white"
            e.control.icon = ft.icons.DARK_MODE
            e.page.update()

    def swicth_bahasa(e: ft.ControlEvent) -> None:
        bahasa_input.value, bahasa_output.value, input_text.value, output.value = (
            bahasa_output.value,
            bahasa_input.value,
            output.value,
            input_text.value,
        )
        e.page.update()

    def copy_clibboard(e: ft.ControlEvent) -> None:
        e.page.set_clipboard(output.value)
        e.page.update()

    async def terjemahan(e: ft.ControlEvent) -> None:
        if len(input_text.value) == 0:
            await asyncio.sleep(0.5)
            output.visible, copy_button.visible = 0, 0
            e.page.update()

        if len(input_text.value) <= 500:
            await asyncio.sleep(2)
            res: Translated = trans.translate(
                text=input_text.value,
                dest=dict_bahasa[bahasa_output.value],
                src=dict_bahasa[bahasa_input.value],
            )
            output.value = res.text
            output.visible, copy_button.visible = True, True
            e.page.update()
        else:
            input_text.error_text = "Maksimal 500 huruf"
            input_text.value = ""
            e.page.update()

    def clear_output(e: ft.ControlEvent) -> None:
        output.visible, copy_button.visible = False, False
        output.value = ""
        input_text.error_text = ""
        input_text.counter_text = ""
        e.page.update()

    async def clear_input(e: ft.ControlEvent) -> None:
        input_text.value = ""
        await asyncio.sleep(0.5)
        output.visible, copy_button.visible = False, False
        e.page.update()

    bahasa_input: ft.Dropdown = ft.Dropdown(
        expand=True,
        alignment=ft.alignment.center_left,
        value="English",
        options=[ft.dropdown.Option(text=bahasa) for bahasa in bahasas],
    )

    bahasa_output: ft.Dropdown = ft.Dropdown(
        expand=True,
        alignment=ft.alignment.center_left,
        value="Indonesian",
        options=[ft.dropdown.Option(text=bahasa) for bahasa in bahasas],
    )

    input_text: ft.TextField = ft.TextField(
        hint_text="Masukan tesk",
        # expand=True,
        multiline=True,
        max_length=500,
        on_focus=clear_output,
        on_change=terjemahan,
    )

    output: ft.TextField = ft.TextField(
        # expand=True,
        visible=False,
        hint_text="Terjemahan",
        multiline=True,
    )
    copy_button: ft.IconButton = ft.IconButton(
        icon=ft.icons.COPY_ALL_ROUNDED,
        on_click=copy_clibboard,
        visible=False,
    )
    return View(
        route="/",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        auto_scroll=True,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=600,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.IconButton(icon=ft.icons.LIGHT_MODE, on_click=theme_mode)
                        ],
                    ),
                    ft.Text(
                        value="Translator App",
                        font_family="manrope",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                    ),
                    ft.Divider(height=24, color="transparent"),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
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
                        wrap=True,
                        controls=[
                            ft.Column(
                                controls=[
                                    input_text,
                                    ft.IconButton(
                                        icon=ft.icons.DELETE_OUTLINE,
                                        on_click=clear_input,
                                    ),
                                ],
                            ),
                            ft.Column(
                                controls=[
                                    output,
                                    copy_button,
                                ],
                            ),
                        ],
                    ),
                    ft.Divider(height=24, color="transparent"),
                ],
            )
        ],
    )
