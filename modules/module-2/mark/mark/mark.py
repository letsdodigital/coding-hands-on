from rxconfig import config

import reflex as rx


@rx.page(title="Consent form")
def index():
    return rx.center(
        rx.vstack(
            rx.box(
                rx.heading("My digital consent form", font_size="2em"),
                padding_top="20px",
            ),
            rx.text("This is where I build the consent form"),
            spacing="4",
        ),
        width="100%",
        justify_content="center",
        align_items="center",
    )


app = rx.App()
app.add_page(index)
