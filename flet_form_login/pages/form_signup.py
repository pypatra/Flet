from flet import (
    BoxShadow,
    ButtonStyle,
    Checkbox,
    Column,
    Container,
    ControlEvent,
    Divider,
    FilledButton,
    Icon,
    IconButton,
    Image,
    Offset,
    OutlinedButton,
    RoundedRectangleBorder,
    Row,
    ShadowBlurStyle,
    Text,
    TextButton,
    TextField,
    TextThemeStyle,
    View,
    colors,
    icons,
)


def view_signup() -> View:

    def thememode(e: ControlEvent) -> None:
        if e.page.theme_mode == "dark":
            e.page.theme_mode = "light"
            e.control.icon = icons.LIGHT_MODE
            e.page.update()
        else:
            e.page.theme_mode = "dark"
            e.control.icon = icons.DARK_MODE
            e.page.update()

        e.page.update()

    return View(
        route="/signup",
        vertical_alignment="center",
        horizontal_alignment="center",
        controls=[
            Container(
                width=500,
                height=900,
                padding=24,
                border_radius=24,
                shadow=BoxShadow(
                    spread_radius=1,
                    blur_radius=4,
                    color=colors.BLUE_GREY_300,
                    offset=Offset(0, 0),
                    blur_style=ShadowBlurStyle.OUTER,
                ),
                content=Column(
                    controls=[
                        # thememode
                        Row(
                            alignment="end",
                            controls=[
                                IconButton(icon=icons.LIGHT_MODE, on_click=thememode)
                            ],
                        ),
                        # Logo
                        Row(
                            alignment="center",
                            controls=[Image(src="logo.png", width=100)],
                        ),
                        Divider(height=16, color="transparent"),
                        # header
                        Column(
                            controls=[
                                Text(
                                    value="Create an account",
                                    font_family="manrope",
                                    style=TextThemeStyle.HEADLINE_LARGE,
                                ),
                                Text(
                                    value="Connect with your friends today!",
                                    font_family="manrope",
                                    style=TextThemeStyle.LABEL_LARGE,
                                ),
                            ]
                        ),
                        Divider(height=8, color="transparent"),
                        # form
                        TextField(
                            label="Email Address", hint_text="Please enter your email"
                        ),
                        TextField(
                            label="Phone Number",
                            hint_text="Please enter phone number",
                        ),
                        TextField(
                            label="Password",
                            password=True,
                            hint_text="Please enter your password",
                            can_reveal_password=True,
                        ),
                        Row(
                            alignment="spacebetween",
                            controls=[
                                Checkbox(label="Remember Me"),
                                TextButton(text="Forgot Password ?", visible=False),
                            ],
                        ),
                        Divider(height=16, color="transparent"),
                        # button signup
                        Row(
                            controls=[
                                FilledButton(
                                    expand=True,
                                    height=48,
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(radius=4)
                                    ),
                                    content=Text(
                                        value="Sign Up",
                                        font_family="manrope",
                                    ),
                                )
                            ],
                        ),
                        Divider(height=16, color="transparent"),
                        # or other
                        Row(
                            spacing=24,
                            controls=[
                                Container(
                                    height=1, bgcolor=colors.GREY_500, expand=True
                                ),
                                Text(value="Or Other", font_family="manrope"),
                                Container(
                                    height=1, bgcolor=colors.GREY_500, expand=True
                                ),
                            ],
                        ),
                        Divider(height=16, color="transparent"),
                        # button facebook&callnumber
                        Row(
                            spacing=32,
                            controls=[
                                OutlinedButton(
                                    expand=True,
                                    height=48,
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(radius=4)
                                    ),
                                    content=Row(
                                        alignment="center",
                                        controls=[
                                            Icon(name=icons.FACEBOOK_SHARP),
                                            Text(
                                                value="Facebook",
                                                font_family="manrope",
                                            ),
                                        ],
                                    ),
                                ),
                                OutlinedButton(
                                    expand=True,
                                    height=48,
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(radius=4)
                                    ),
                                    content=Row(
                                        alignment="center",
                                        controls=[
                                            Icon(name=icons.CALL_SHARP),
                                            Text(
                                                value="Call Number",
                                                font_family="manrope",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        Divider(height=24, color="transparent"),
                        # signup
                        Row(
                            alignment="center",
                            controls=[
                                Text(
                                    value="Already have an account ?",
                                    font_family="manrope",
                                ),
                                TextButton(
                                    content=Text(value="Login", font_family="manrope"),
                                    on_click=lambda e: e.page.go("/login"),
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ],
    )
