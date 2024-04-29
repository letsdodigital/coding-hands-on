import reflex as rx

class Patient(rx.Model, table= True):
    forename: str
    surname: str
    nhs_number: str

class Procedure(rx.Model, table = True):
    procedure: str
    procedure_description: str
    procedure_benefits: str
    procedure_risks: str

    