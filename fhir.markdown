---
layout: fhir
fhir:
  fhir_text: "Each FHIR resource serves a specific purpose in healthcare data management, enabling interoperability and standardization across systems. These resources are widely used in electronic health records (EHRs), clinical decision support systems, and healthcare applications."
  fhir_resources:
    group_1:
      - fhir_resource: "Patient"
        fhir_icon: "fas fa-user"
        fhir_description: "Represents demographic and administrative information about an individual receiving care. Used for identifying and managing patient records."
        bootstrap_colour: "primary"
        fhir_long_form: |
            A Patient resource is the anchor for every NHS record, holding demographic and administrative details such as name, date of birth, NHS number and preferred language. It establishes identity, ensures the right notes follow the right person across settings, and underpins statutory reporting (e.g. 18-week RTT and cancer-waiting-time clocks).

            Because almost every other FHIR resource references a Patient, the Patient resource acts as a hub. Observations, Conditions, MedicationRequests and Encounters all carry a subject link back to the Patient, while Allergies, Immunisations and CarePlans use it to guarantee safe continuity of care when data flows between GP systems, shared-care records and acute EPRs.

      - fhir_resource: "Observation"
        fhir_icon: "fas fa-chart-line"
        fhir_description: "Captures measurements and clinical assessments, such as lab results, vital signs, or imaging findings. Essential for tracking patient health data."
        bootstrap_colour: "success"
        fhir_long_form: |
            An Observation records a single clinical measurement or assessment—NEWS2 score in ED, HbA1c from pathology, or a chest-X-ray impression typed at a PACS workstation. Each entry stores the value, unit, coded term (typically SNOMED CT or LOINC in England), the timestamp and the performer.

            Every Observation links back to its Patient (`subject`) and the Encounter (`context`) in which it was made, and may be grouped under a DiagnosticReport. Decision-support tools query recent Observations to trigger alerts—e-Sepsis rules, for example—while CarePlans track progress by monitoring trends in key observations such as weight or blood pressure.

      - fhir_resource: "Condition"
        fhir_icon: "fas fa-diagnoses"
        fhir_description: "Represents a clinical condition, problem, or diagnosis. Used for documenting patient health issues and managing care plans."
        bootstrap_colour: "danger"
        fhir_long_form: |
            A Condition captures any diagnosed or suspected health problem, from lifelong diabetes to an episode of community-acquired pneumonia. It records onset date, clinical status, certainty and severity, supporting QOF registers, GIRFT analytics and secondary-uses data submissions.

            Conditions reference the Patient and, when relevant, the Encounter or EpisodeOfCare in which they were identified. CarePlans list active Conditions as targets, while MedicationRequests and Procedures cite them in `reasonReference`, providing the clinical justification for treatment or intervention.

    group_2:
      - fhir_resource: "MedicationRequest"
        fhir_icon: "fas fa-prescription-bottle-alt"
        fhir_description: "Represents a request for medication for a patient. Used for prescribing, dispensing, and tracking medication orders."
        bootstrap_colour: "warning"
        fhir_long_form: |
            A MedicationRequest documents an order for medicines—repeat inhalers from primary care, warfarin on an inpatient chart, or TTO antibiotics at discharge. It records the drug, dose, route, timing, authorising prescriber and whether it is destined for EPS, ward stock or homecare.

            The resource references the Patient and the authoring Practitioner, and is usually tied to the Encounter in which it was created. Linked Conditions or Observations (e.g. INR) explain clinical intent, while downstream Dispense and Administration resources update status so pharmacists and ward staff can reconcile therapy in real time.

      - fhir_resource: "Procedure"
        fhir_icon: "fas fa-syringe"
        fhir_description: "Documents actions taken on a patient, such as surgeries, therapies, or diagnostic tests. Used for tracking interventions and outcomes."
        bootstrap_colour: "info"
        fhir_long_form: |
            A Procedure records an action performed on the patient—from venepuncture to robotic prostatectomy. It captures performer, date/time, body-site, technique, outcome and any follow-up requirements, fulfilling NHS theatre coding and interventional radiology reporting.

            Procedures reference the Patient and Encounter, while Observations or DiagnosticReports generated during the event (histology, post-op haemoglobin) point back using `partOf`. They can also satisfy goals in a CarePlan and appear as `reasonReference` for future Appointments or follow-up investigations.

      - fhir_resource: "Encounter"
        fhir_icon: "fas fa-hospital"
        fhir_description: "Represents an interaction between a patient and healthcare provider, such as a visit, admission, or consultation. Used for managing episodes of care."
        bootstrap_colour: "secondary"
        fhir_long_form: |
            An Encounter marks a clinical interaction—ED attendance, outpatient clinic, domiciliary visit or virtual ward round. It defines status (arrived, admitted, discharged), location, participants and care setting, feeding PAS activity reporting and real-time bed-management dashboards.

            Observations, MedicationRequests, Procedures and DiagnosticReports created during that contact all carry the Encounter ID in their `encounter`/`context` element. Linking Encounters into Episodes supports datasets such as the SUS admitted-patient-care collection and enables analysts to reconstruct a full spell of care.

    group_3:
      - fhir_resource: "AllergyIntolerance"
        fhir_icon: "fas fa-exclamation-triangle"
        fhir_description: "Captures information about allergies or intolerances a patient has. Used for ensuring safe treatment and avoiding adverse reactions."
        bootstrap_colour: "danger"
        fhir_long_form: |
            An AllergyIntolerance stores confirmed or suspected hypersensitivities—penicillin anaphylaxis, nut allergy, or contrast-medium intolerance. It records reaction manifestation, severity, certainty and evidence, driving e-Prescribing safety checks and DSCR alerts.

            The resource references the Patient and optionally the Encounter in which it was documented. CDS engines consult AllergyIntolerance before authorising MedicationRequests, while Procedure records (e.g. contrast CT) check for iodine allergies, ensuring contraindications are flagged across care settings.

      - fhir_resource: "Immunization"
        fhir_icon: "fas fa-syringe"
        fhir_description: "Documents vaccines administered to a patient. Used for tracking immunization history and compliance."
        bootstrap_colour: "success"
        fhir_long_form: |
            An Immunization captures each vaccine event—MMR in infancy, seasonal influenza, or a COVID-19 booster—recording lot number, site, route and programme eligibility. It underpins the national IIS, supports cohort recalls and provides evidence for travel clinics and occupational-health clearance.

            Immunizations reference the Patient and, if delivered during a visit, the Encounter. They fulfil CarePlan goals (e.g. "fully vaccinated"), inform public-health surveillance and allow decision-support tools to detect gaps—triggering alerts when an Observation (positive PCR) appears without a corresponding COVID immunization.

      - fhir_resource: "DiagnosticReport"
        fhir_icon: "fas fa-file-medical"
        fhir_description: "Represents the findings and interpretations of diagnostic tests, such as lab results or imaging studies. Used for clinical decision-making."
        bootstrap_colour: "primary"
        fhir_long_form: |
            A DiagnosticReport bundles the narrative conclusion of a test episode—biochemistry panel, CT head or spirometry—together with links to its Observations, images or PDFs. It includes status, performer, specimen details and issue date, ensuring safe sign-off and clear provenance.

            The report ties to the Patient and Encounter, references any specimen or ImagingStudy resources, and lists individual Observations in `result`. Portals surface the DiagnosticReport headline while allowing drill-down into component readings, supporting multidisciplinary team review and discharge summarisation.

    group_4:
      - fhir_resource: "CarePlan"
        fhir_icon: "fas fa-notes-medical"
        fhir_description: "Represents a plan for managing a patient's health, including goals, interventions, and outcomes. Used for coordinating care across providers."
        bootstrap_colour: "info"
        fhir_long_form: |
            A CarePlan articulates coordinated goals, activities and responsible teams for complex cases—frailty management, cancer follow-up or anticipatory care. It records personalised outcomes, scheduled interventions and review dates, supporting the NHS's personalised-care agenda and ICB-wide shared-decision-making.

            The plan references the Patient, authoring Practitioner and custodial Organisation. Activities point to future Appointments, MedicationRequests or Procedures, while linked Observations and Encounters update progress notes that automatically adjust goal status—keeping community, primary and secondary-care teams aligned.

      - fhir_resource: "Device"
        fhir_icon: "fas fa-microchip"
        fhir_description: "Represents medical devices used in patient care, such as implants, monitors, or diagnostic tools. Used for tracking device usage and maintenance."
        bootstrap_colour: "dark"
        fhir_long_form: |
            A Device resource captures any kit applied to or used by the patient—hip prosthesis, cardiac monitor, or home BP cuff—with identifiers, model, serial number and UDI, meeting MHRA traceability standards and facilitating field-safety recalls.

            Other resources reference the Device: a Procedure records implantation, DeviceUsage logs home readings, Observations store values originating from the device, and AdverseEvent cites the Device if a fault occurs, enabling end-to-end vigilance across the patient journey.

      - fhir_resource: "Appointment"
        fhir_icon: "fas fa-calendar-check"
        fhir_description: "Represents a scheduled meeting between a patient and healthcare provider. Used for managing bookings and availability."
        bootstrap_colour: "warning"
        fhir_long_form: |
            An Appointment captures future bookings—clinic slots, imaging sessions or domiciliary visits—storing planned time, participants, service type and Did-Not-Attend flags. It powers clinic templates, 2-week-wait trackers and patient self-service via the NHS App.

            Once fulfilled, the Appointment spawns an Encounter; CarePlans reference it within scheduled activities; and Practitioner or HealthcareService availability updates accordingly, ensuring capacity planning and real-time patient communication stay synchronised.

    group_5:
      - fhir_resource: "HealthcareService"
        fhir_icon: "fas fa-concierge-bell"
        fhir_description: "Represents services offered by a healthcare provider, such as specialties or facilities. Used for managing service directories."
        bootstrap_colour: "secondary"
        fhir_long_form: |
            A HealthcareService describes an Organisation's offerings—physiotherapy, MRI, GP extended hours—with contact details, eligibility criteria and capacity. It underpins the NHS Directory of Services and e-Referral triage by allowing systems to match referrals to the most appropriate provider.

            Appointments reference HealthcareService to indicate the type of slot booked, while CarePlans pull in services needed to achieve goals. At organisation-level, ICS dashboards use HealthcareService data to map supply and demand across regions.

      - fhir_resource: "Practitioner"
        fhir_icon: "fas fa-user-md"
        fhir_description: "Represents information about healthcare professionals. Used for identifying and managing provider roles and responsibilities."
        bootstrap_colour: "primary"
        fhir_long_form: |
            A Practitioner resource profiles clinicians—consultants, GPs, nurses—recording GMC or NMC identifiers, specialities and contact preferences. It feeds authentication (smartcards), rosters and clinical-note attribution, ensuring the right professional is credited for each action.

            Practitioners act as authors or performers in Encounters, Procedures, Observations, DiagnosticReports and MedicationRequests. They link to Organisations and HealthcareServices to show their affiliations, supporting on-call lookup, e-rostering and revalidation audits.

      - fhir_resource: "Organization"
        fhir_icon: "fas fa-building"
        fhir_description: "Represents details about healthcare organizations, such as hospitals or clinics. Used for managing administrative and operational data."
        bootstrap_colour: "info"
        fhir_long_form: |
            An Organization captures administrative entities—NHS trusts, ICBs, GP practices or diagnostic providers—storing ODS codes, sites and operational roles. It supports commissioning flows, data-sharing agreements and onboarding with national services like the DSPT and MESH.

            Organization resources own Locations, HealthcareServices and Practitioners, and populate `serviceProvider` in Encounters or `custodian` in CarePlans. They provide provenance when data moves across the Spine, ensuring clinicians can see where and by whom information was generated.
---