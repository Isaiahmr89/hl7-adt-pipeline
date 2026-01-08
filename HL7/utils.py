from datetime import datetime

# HL7 Helpers
FACILITY = "HOSPITAL"
SENDING_APP = "ADT"
VERSION = "2.5"

def hl7_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")

def msh(event_type, message_id):
    return (
        f"MSH|^~\\&|{SENDING_APP}|{FACILITY}|EHR|{FACILITY}"
        f"|{hl7_timestamp()}||ADT^{event_type}|{message_id}|P|{VERSION}"
    )

def evn(event_type):
    return (
        f"EVN|{event_type}|{hl7_timestamp()}"
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