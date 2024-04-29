from rxconfig import (
    config,
)

import reflex as rx


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

        def database_all(
            self,
        ):
            return self.users


"""class database_management(rx.State):
    name: str
    users: list[User]

    def __init__(self):
        return"""


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
        ),
    )

    """return rx.center(
        rx.vstack(
            rx.box(
                rx.heading("My digital consent form", font_size="2em"),
                padding_top="20px",
            ),
            rx.form(
                rx.vstack(
                    rx.text("Patient"),
                    rx.input(
                        name="first_name",
                        label="First name",
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
            rx.html(db_all()),
            spacing="4",
        ),
        width="100%",
        justify_content="center",
        align_items="center",
    )"""


app = rx.App()
app.add_page(index)
