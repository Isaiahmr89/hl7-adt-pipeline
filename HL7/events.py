from utils import msh, pid, pv1, evn
import random

# Event generators
# Event ADT^A01 Admission
def generate_a01(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A01", msg_id),
        evn("A01"),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        pv1("ER^12^A")
    ])

# Event ADT^A02 Transfer
def generate_a02(patient, location):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A02", msg_id),
        evn("A02"),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        pv1(location)
    ])

# Event ADT^A03 Discharge
def generate_a03(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A03", msg_id),
        evn("A03"),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
        "PV1|1|I|||||||||||||||||202512271030"
    ])

# Event ADT^A08 Update
def generate_a08(patient):
    msg_id = random.randint(100000, 999999)

    return "\n".join([
        msh("A08", msg_id),
        evn("A08"),
        pid(patient["patient_id"], patient["last_name"], patient["first_name"], "19800101", patient["sex"]),
    ])

events = [generate_a01, generate_a08, generate_a02, generate_a03]