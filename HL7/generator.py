from lifecycle import init_patient_state, next_event
from datetime import datetime
from pathlib import Path
import random

OUT_DIR = Path("HL7/flows")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def write_hl7(message, patient_id, trigger):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = OUT_DIR / f"{patient_id}_{trigger}_{ts}.hl7"
    with open(filename, "w") as f:
        f.write(message)

PATIENTS = [
    {"patient_id": "00001", "first_name": "John", "last_name": "Doe", "sex": "M"},
    {"patient_id": "00002", "first_name": "Jane", "last_name": "Smith", "sex": "F"},
    {"patient_id": "00003", "first_name": "Chris", "last_name": "Brown", "sex": "M"},
]

for p in PATIENTS:
        init_patient_state(p)

if __name__ == "__main__":
    for _ in range(15):
        patient = random.choice(PATIENTS)
        msg = next_event(patient)

        if msg:
            trigger = msg.split("|")[8].split("^")[1]
            write_hl7(msg, patient["patient_id"], trigger)

            print(msg)
            print("-" * 10)








    # for _ in range(10):
    #     patient = random.choice(PATIENTS)
    #     msg = generate_a02(patient)
    #     print(msg)
    #     print("-" * 50)





