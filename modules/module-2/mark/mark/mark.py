from rxconfig import (
    config,
)

import reflex as rx

from consent_types import (
    consent_keys,
    get_full_description,
    get_intended_benefits,
    get_potential_risks,
)
from users import users


class User(
    rx.Model,
    table=True,
):
    username: str
    email: str
    password: str


class FormState(rx.State):
    name: str
    users: list[User]
    form_data: dict = {}
    select_state = ""
    procedure = ""
    full_description = ""
    intended_benefits = ""
    potential_risks = ""

    def handle_submit(
        self,
        form_data: dict,
    ):
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

        with rx.session() as session:
            self.users = session.exec(
                User.select().where(User.username.contains(self.name))
            ).all()

        # print(self.users)

        self.update()

    def update(self, procedure=""):
        self.procedure = procedure
        self.full_description = get_full_description(self.procedure)
        self.intended_benefits = get_intended_benefits(self.procedure)
        self.potential_risks = get_potential_risks(self.procedure)
        return


def db_all():
    name = ""
    users = []
    return_str = ""
    with rx.session() as session:
        users = session.exec(
            User.select().where(User.username.contains(name))
        ).all()

    # print(users)

    for user in users:
        return_str += f"{ user }</br>"

    return return_str


style_main = {
    "direction": "column",
    "spacing": "2",
    "align": "start",
}

style_text = {"width": "500px"}

style_button = {
    "width": "100%",
    "direction": "column",
    "align": "end",
    "spacing": "2",
}


@rx.page(title="Consent form")
def index():

    return rx.center(
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
                        rx.flex(
                            rx.form.label("First name"),
                            rx.form.control(
                                rx.input.input(
                                    type="text",
                                    **style_text,
                                ),
                                as_child=True,
                            ),
                            rx.form.message(
                                "Please enter a first name!",
                                match="typeMismatch",
                            ),
                            name="first_name",
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
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
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
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
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
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
                            **style_main,
                        ),
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
                            name="consent_type",
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
                            rx.form.label("Full description"),
                            rx.text_area(
                                value=FormState.full_description,
                                **style_text,
                                disabled=True,
                            ),
                            name="full_description",
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
                            rx.form.label("Intended benefits"),
                            rx.text_area(
                                value=FormState.intended_benefits,
                                **style_text,
                                disabled=True,
                            ),
                            name="intended_benefits",
                            **style_main,
                        ),
                    ),
                    rx.form.field(
                        rx.flex(
                            rx.form.label("Potential risks"),
                            rx.text_area(
                                value=FormState.potential_risks,
                                **style_text,
                                disabled=True,
                            ),
                            name="potential_risks",
                            **style_main,
                        ),
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
                            name="signed_by",
                            **style_main,
                        ),
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
        ),
    )


app = rx.App()
app.add_page(index)
