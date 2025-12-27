from datetime import datetime
import random

FACILITY = "HOSPITAL"
SENDING_APP = "ADT"
VERSION = "2.5"

PATIENTS = [
    {"patient_id": "00001", "first_name": "John", "last_name": "Doe", "sex": "M"},
    {"patient_id": "00002", "first_name": "Jane", "last_name": "Smith", "sex": "F"},
    {"patient_id": "00003", "first_name": "Chris", "last_name": "Brown", "sex": "M"},
]


# HL7 Helpers
def hl7_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def msh(event_type, message_id):
    return (
        f"MSH|^~\\&|{SENDING_APP}|{FACILITY}|EHR|{FACILITY}"
        f"{hl7_timestamp()}|ADT^{event_type}|{message_id}|P|{VERSION}"
    )

def pid(patient_id, last_name, first_name, dob, sex):
    return (
        f"PID|1||{patient_id}^^^{FACILITY}||"
        f"{last_name}^{first_name}||{dob}|{sex}"
    )

def pv1(location, provider_id="1234", provider_last="Smith", provider_first="Alice"):
    return (
        f"PV1|1|I|{location}||||"
        f"{provider_id}^{provider_last}^{provider_first}"
    )

# Event generators
# Event ADT^A01 Admission
def generate_a01(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A01", msg_id),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        pv1("ER^12^A")
    ])

# Event ADT^A02 Transfer
def generate_a02(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A02", msg_id),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        pv1("ICU^05^B")
    ])

# Event ADT^A03 Discharge
def generate_a03(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A03", msg_id),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        "PV1|1|I|||||||||||||||||202512271030"
    ])

# Event ADT^A08 Update
def generate_a08(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A08", msg_id),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
    ])

events = [generate_a01, generate_a08, generate_a02, generate_a03]

if __name__ == "__main__":
    for _ in range(10):
        patient = random.choice(PATIENTS)
        msg = generate_a01(patient)
        print(msg)
        print("-" * 50)





