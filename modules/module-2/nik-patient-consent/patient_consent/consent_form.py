import reflex as rx

class FormState(rx.State):
    form_data = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data


class ProcedureSelect(rx.State):
    values: list[str] = ['Head','Shoulders','Knees','Toes']
    value: str = ''


def consent_form() -> rx.Component:
    form = rx.center(
        rx.form(
            rx.vstack(
                rx.heading("Patient Consent Form", size="4"),
                rx.hstack(
                    rx.input.root(
                        rx.input(
                            placeholder="First Name",
                            name="first_name",
                        ),
                        width="50%",
                    ),
                    rx.input.root(
                        rx.input(
                            placeholder="Last Name",
                            name="last_name",
                        ),
                        width="50%"
                    ),
                    spacing="2",
                    width="100%"
                ),
                rx.input.root(
                    rx.input(placeholder="NHS Number", name="nhs_number"),
                    width="100%"
                ),
                rx.divider(),
                rx.hstack(
                    rx.select(
                        ProcedureSelect.values,
                        value=ProcedureSelect.value,
                        on_change=ProcedureSelect.set_value,
                        placeholder="Select Procedure Location",
                        label="Procedure Location",
                        width="100%"
                    ),
                ),
                rx.text_area(placeholder="Procedure", name="procedure", width="100%"),
                rx.text_area(placeholder="Side Effects", name="side_effects", width="100%"),
                rx.divider(),
                rx.box(
                    rx.heading("Patient Consent", size="3"),
                    rx.text(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed neque elit, tristique placerat feugiat ac, facilisis vitae arcu. Proin eget egestas augue. Praesent ut sem nec arcu 'pellentesque aliquet. Duis dapibus diam vel metus tempus vulputate.",
                        size="1",
                        padding_bottom="1em",
                    ),
                    rx.hstack(
                        rx.hstack(
                            rx.checkbox(
                                spacing="2",
                                size="1",
                                default_checked=False,
                                required=True,
                            ),
                            rx.text("I consent to procedure", size="1"),
                            padding_top="2px",
                        ),
                        rx.spacer(),
                        rx.button(
                            "Submit",
                            size="1",
                            required=True,
                        ),
                    ),
                    direction="column",
                    align_items="start",
                    border="1px solid",
                    border_radius="15px",
                    spacing="3",
                    padding="1em",
                ),
            )
        ),
    )
    return form
