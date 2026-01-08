import random
from events import generate_a01, generate_a02, generate_a03, generate_a08

LOCATIONS = ["ER", "ICU", "MED", "SURG"]

def choose_new_location(current):
    return random.choice([loc for loc in LOCATIONS if loc != current])


def init_patient_state(patient):
    patient["state"] = "NEW"
    patient["location"] = None
    patient["encounter_id"] = None


def next_event(patient):
    if patient["state"] == "NEW":
        patient["state"] = "ADMITTED"
        patient["location"] = None
        return generate_a01(patient)

    if patient["state"] in ("ADMITTED", "TRANSFERRED"):
        roll = random.random()

        if roll < 0.6:
            new_location = choose_new_location(patient["location"])
            patient["location"] = new_location
            patient["state"] = "TRANSFERRED"
            return generate_a02(patient, f"{new_location}^05^B")

        elif roll < 0.8:
            return generate_a08(patient)

        else:
            patient["state"] = "DISCHARGED"
            patient["location"] = None
            return generate_a03(patient)

    return None

