from lifecycle import init_patient_state, next_event
import random

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
            print(msg)
            print("-" * 10)








    # for _ in range(10):
    #     patient = random.choice(PATIENTS)
    #     msg = generate_a02(patient)
    #     print(msg)
    #     print("-" * 50)





