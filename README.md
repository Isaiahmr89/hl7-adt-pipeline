**Project Overview**

This project demonstrates an end-to-end healthcare data integration pipeline using HL7 v2 ADT messages. 
It generates realistic, stateful ADT event flows (admit, transfer, update, discharge), validates message structure 
and required fields, and transforms validated HL7 messages into FHIR-compliant JSON resources for downstream storage 
and analytics.

Synthetic patient data is used to simulate real hospital workflows while preserving realistic message structure and 
event sequencing. The pipeline is designed to support auditing, replay, and future analytics use cases such as ADT 
dashboards.

**Current Capabilities**

Stateful HL7 ADT message generation (A01, A02, A03, A08)
Multi-patient, realistic hospital event flows
HL7 envelope, structural, and field-level validation (QA pipeline)
HL7 → FHIR transformation (Patient and Encounter resources)
Replayable HL7 message datasets for testing and analysis

**Tech Stack**

Python – HL7 message generation, validation, and transformation
Flask – API layer for HL7 ingestion (in progress)
PostgreSQL – Structured storage for raw HL7 and FHIR JSON (planned)
Power BI – Analytics and dashboarding (planned)
AWS S3 – Cloud storage for raw message archival (planned)

**Roadmap**

API-based HL7 ingestion with validation and transformation
PostgreSQL persistence (raw HL7, validation results, FHIR JSON)
Containerization with Docker Compose
CI with automated validation tests
Analytics dashboards based on ADT event data