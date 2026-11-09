"""
SQLAlchemy Lab 03
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, init_db
from models import Owner, Vet, Pet, Appointment


def update_appt(session):
    """
    This function assumes the user makes
    no mistakes and that there are no duplicates
    """
    name = input("What is your pet's name?\n")
    date = input("When is the appointment you would like to change? (YYYY-MM-DD)\n")

    # TODO: Get the appointment and its vet for the print statements below
    appt = None
    vet = None

    print("Great! I have the following appointment:")
    print(f"{appt.date} at {appt.time} with {vet}")

    response = input("Would you like to 'reschedule' or 'cancel' this appointment?\n")

    if response == "cancel":
        # TODO: Cancel the appointment. The time slot stays open for another pet.
        
        print("Your appointment has been cancelled. Thank you!")
    else:
        new_date = input("When would you like to change your appointment to? (YYYY-MM-DD)\n")
        # TODO: Change the appointment's date

        print("Great! You now have the following appointment:")
        print(f"{appt.date} at {appt.time} with {vet}")

        verify = input("Is that correct? (Y/N)\n")
        if verify == "N":
            # TODO: Undo the change

            print(f"Your appointment is still {appt.date} at {appt.time} with {vet}")
        else:
            # TODO: Save the change

            print("Your appointment has been updated")


# Create and fill vet.db if it doesn't exist yet
init_db()

with Session(engine) as session:
    update_appt(session)
