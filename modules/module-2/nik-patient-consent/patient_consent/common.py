import reflex as rx

from patient_consent import consent_form

def menu() -> rx.Component:
    menu = rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon(tag="menu", size=12, variant="ghost", color_scheme="blue")
            ),
        ),
        rx.menu.content(
            rx.menu.item("Home"),
            rx.menu.item("About"),
            rx.menu.separator(),
            rx.menu.item(
                "New Consent Form", 
                shortcut="⌘ N",
            ),
            rx.menu.item("Open Consent Form", shortcut="⌘ O"),
            variant="soft",
            align="start",
        ),
    )

    return menu


def navbar() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        menu(),
        width="100%",
    )
