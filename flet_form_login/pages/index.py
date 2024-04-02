from flet import Container, Image, View


def view_index() -> View:
    return View(
        route="/home",
        vertical_alignment="center",
        horizontal_alignment="center",
        controls=[Container(padding=24, content=Image(src="logo.png", width=124))],
    )
