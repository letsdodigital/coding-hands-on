import reflex as rx
from rxconfig import config

from patient_consent import common
from patient_consent import consent_form

class State(rx.State):
    pass


def home_heading() -> rx.Component:
    return rx.vstack(
        rx.heading("Let's Do Digital Patient Consent", size="9"),
        rx.text("Sample consent webapp built for teaching"),
        rx.hstack(
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Create New Consent Form", size="4")),
                rx.dialog.content(consent_form.consent_form()),
            ),
            rx.button("Open Existing Consent Form", size="4"),
        ),
        align="center",
        spacing="7",
        font_size="2em",
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            common.navbar(),
            rx.spacer(),
            rx.section(home_heading()),
        ),
        height="100vh",
    )


@rx.page(route='/help')
def help() -> rx.Component:
    return rx.center(
        rx.tooltip(
            common.help_tooltip(),
            content = "This is a help tooltip",
        )
    )


app = rx.App()
app.add_page(index)
