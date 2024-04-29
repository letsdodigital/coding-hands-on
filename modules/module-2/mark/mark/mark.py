from rxconfig import config

import reflex as rx


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handles the form submit."""
        self.form_data = form_data


@rx.page(title="Consent form")
def index():
    return rx.center(
        rx.vstack(
            rx.box(
                rx.heading("My digital consent form", font_size="2em"),
                padding_top="20px",
            ),
            rx.text("This is where I build the consent form"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Test text...",
                        name="test_data",
                        max_length="100",
                        required=True,
                    ),
                    rx.button("Submit", type="submit"),
                    spacing="4",
                ),
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.heading("Results"),
            rx.text(FormState.form_data.to_string()),
            spacing="4",
        ),
        width="100%",
        justify_content="center",
        align_items="center",
    )


app = rx.App()
app.add_page(index)
