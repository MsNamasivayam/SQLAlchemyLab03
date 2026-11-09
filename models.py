"""
The model classes. Each class maps to one table in vet.db,
and each attribute maps to one column.
"""

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone_number: Mapped[str]

    def __repr__(self):
        return f"{self.last_name}, {self.first_name} #{self.phone_number}"


class Vet(Base):
    __tablename__ = "vets"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    def __repr__(self):
        return f"Dr. {self.last_name}"


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    species: Mapped[str]
    owner_id: Mapped[Optional[int]] = mapped_column(ForeignKey("owners.id"))


class Appointment(Base):
    __tablename__ = "appts"

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pets.id"))
    vet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("vets.id"))
    date: Mapped[Optional[str]]
    time: Mapped[Optional[str]]
