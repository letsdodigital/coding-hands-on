from rxconfig import config

import reflex as rx
import re
import reflex.components.radix.primitives as rdxp

from consent_types import (
    consent_keys,
    get_full_description,
    get_intended_benefits,
    get_potential_risks,
)
from users import users


class User(rx.Model, table=True):
    user_name: str
    first_name: str
    last_name: str


class Patient(rx.Model, table=True):
    first_name: str
    last_name: str
    hospital_number: str
    date_of_birth: str
    email: str


class PatientConsent(rx.Model, table=True):
    patient_id: int
    consent_type: str
    get_full_description: str
    intended_benefits: str
    potential_risks: str
    date: str
    signed_by: str


class FormState(rx.State):
    name: str
    users: list[User]
    form_data: dict = {}
    select_state = ""
    procedure = ""
    full_description = ""
    intended_benefits = ""
    potential_risks = ""

    def handle_submit(self, form_data: dict):
        """Handles the form submit."""
        self.form_data = form_data
        """with rx.session() as session:
            session.add(
                User(
                    username="test",
                    email="admin@reflex.dev",
                    password="admin",
                )
            )
            session.commit()"""

        """with rx.session() as session:
            self.users = session.exec(
                User.select().where(User.username.contains(self.name))
            ).all()"""

        # print(self.users)
        print(self.form_data)

        self.update()

    def update(self, procedure=""):
        self.procedure = procedure
        self.full_description = get_full_description(self.procedure)
        self.intended_benefits = get_intended_benefits(self.procedure)
        self.potential_risks = get_potential_risks(self.procedure)
        return

    def reset_state(self):
        self.reset()

    def print_state(self):
        return "blah"

        """state_str = ""
        for key, value in self.form_data.items():
            state_str += f"{key}: {value}</br>"
        return state_str"""


def db_all():
    name = ""
    users = []
    return_str = ""
    """with rx.session() as session:
        users = session.exec(
            User.select().where(User.username.contains(name))
        ).all()"""

    # print(users)

    for user in users:
        return_str += f"{ user }</br>"

    return return_str


style_main = {
    "direction": "column",
    "spacing": "2",
    "align": "start",
    "top-padding": "10px",
}

style_select = {
    "direction": "column",
    "align": "start",
}

style_text = {"width": "500px"}

style_button = {
    "width": "100%",
    "direction": "column",
    "align": "end",
    "spacing": "2",
}

style_navbar = {
    "width": "100%",
    "padding": "10px",
}


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.heading("Consent form", font_size="2em"),
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
            ),
            rx.menu.content(
                rx.menu.item(rx.link("Consent form", href="/")),
                rx.menu.item(
                    rx.link("Previous forms", href="/previous-forms")
                ),
                rx.menu.item(
                    rx.link("Database refresh", href="/database-refresh")
                ),
                width="10rem",
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )


@rx.page(title="Consent form")
@rx.page(on_load=FormState.reset_state)
def index():
    return rx.fragment(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "My digital consent form",
                        font_size="2em",
                    ),
                    padding_top="20px",
                ),
                rx.form.root(
                    rx.flex(
                        rx.form.field(
                            rx.form.label("First name"),
                            rx.form.control(
                                rx.input.input(
                                    type="text",
                                    required=True,
                                    **style_text,
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a first name!",
                                match="typeMismatch",
                            ),
                            name="first_name",
                        ),
                        rx.form.field(
                            rx.form.label("Last name"),
                            rx.form.control(
                                rx.input.input(
                                    type="text",
                                    **style_text,
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a last name!",
                                match="typeMismatch",
                            ),
                            name="last_name",
                        ),
                        rx.form.field(
                            rx.form.label("Hospital number"),
                            rx.form.control(
                                rx.input.input(
                                    type="text",
                                    **style_text,
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a hospital number!",
                                match="typeMismatch",
                            ),
                            name="hospital_number",
                        ),
                        rx.form.field(
                            rx.form.label("Date of birth"),
                            rx.form.control(
                                rx.input.input(
                                    type="date",
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a valid date of birth!",
                                match="typeMismatch",
                            ),
                            name="date_of_birth",
                        ),
                        rx.form.field(
                            rx.form.label("Patient's email"),
                            rx.form.control(
                                rx.input.input(
                                    type="email",
                                    **style_text,
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a valid email address!",
                                match="typeMismatch",
                            ),
                            name="patient_email",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Consent for"),
                                rx.select(
                                    consent_keys(),
                                    value=FormState.procedure,
                                    placeholder="type",
                                    on_change=FormState.update,
                                ),
                                rx.form.message(
                                    "A consent type must be provided",
                                    match="typeMismatch",
                                ),
                                **style_select,
                            ),
                            name="consent_type",
                        ),
                        rx.form.field(
                            rx.form.label("Full description"),
                            rx.text_area(
                                value=FormState.full_description,
                                **style_text,
                                disabled=True,
                            ),
                            name="full_description",
                        ),
                        rx.form.field(
                            rx.form.label("Intended benefits"),
                            rx.text_area(
                                value=FormState.intended_benefits,
                                **style_text,
                                disabled=True,
                            ),
                            name="intended_benefits",
                        ),
                        rx.form.field(
                            rx.form.label("Potential risks"),
                            rx.text_area(
                                value=FormState.potential_risks,
                                **style_text,
                                disabled=True,
                            ),
                            name="potential_risks",
                        ),
                        rx.form.field(
                            rx.flex(
                                rx.form.label("Signed by"),
                                rx.select(
                                    users,
                                ),
                                rx.form.message(
                                    "A signature is needed!",
                                    match="typeMismatch",
                                ),
                                **style_select,
                            ),
                            name="signed_by",
                        ),
                        rx.flex(
                            rx.form.submit(
                                rx.button("Submit"),
                                as_child=True,
                                width="100px",
                            ),
                            **style_button,
                        ),
                        **style_main,
                    ),
                    on_submit=FormState.handle_submit,
                    reset_on_submit=True,
                    **style_main,
                ),
                rx.divider(),
                rx.heading("Results"),
                rx.html(db_all()),
                # rx.html(FormState.print_state()),
            ),
            padding_top="6em",
        ),
    )


@rx.page(title="Consent form")
def previous_forms():
    return rx.fragment(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "Initialise database",
                        font_size="2em",
                    ),
                    padding_top="20px",
                ),
                rx.text("This will refresh the database and remove all data."),
                rx.form.root(
                    rx.flex(
                        rx.flex(
                            rx.form.submit(
                                rx.button("Refresh database"),
                                as_child=True,
                                width="200px",
                            ),
                            **style_button,
                        ),
                        **style_main,
                    ),
                    on_submit=FormState.handle_submit,
                    reset_on_submit=True,
                    **style_main,
                ),
                **style_main,
            ),
            padding_top="6em",
        ),
    )


@rx.page(title="Consent form")
def database_refresh():
    return rx.fragment(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "Initialise database",
                        font_size="2em",
                    ),
                    padding_top="20px",
                ),
                rx.text("This will refresh the database and remove all data."),
                rx.form.root(
                    rx.flex(
                        rx.flex(
                            rx.form.submit(
                                rx.button("Refresh database"),
                                as_child=True,
                                width="200px",
                            ),
                            **style_button,
                        ),
                        **style_main,
                    ),
                    on_submit=FormState.handle_submit,
                    reset_on_submit=True,
                    **style_main,
                ),
                **style_main,
            ),
            padding_top="6em",
        ),
    )


app = rx.App()
app.add_page(index)
app.add_page(database_refresh, route="/database-refresh")
app.add_page(previous_forms, route="/previous-forms")
