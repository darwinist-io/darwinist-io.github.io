---
layout: document
title: "Laurel Bridge: Integrated DICOM Routing and Radiology AI Orchestration"
subtitle: "Advanced Medical Imaging Workflow Platform for NHS Radiology Departments"
date: 2025-05-26
author: "Darwinist Team"
tags: ["DICOM", "Radiology AI", "Medical Imaging", "NHS", "Healthcare Technology", "PACS", "Workflow Orchestration"]
excerpt: "Advanced medical imaging orchestration platform that integrates DICOM routing with automated prior retrieval and AI workflow orchestration, purpose-built for NHS Trust Radiology Departments and seamless integration with AI algorithms."
---

# Laurel Bridge

Integrated DICOM Routing and Radiology AI Orchestration for NHS Radiology Departments

## **📌 Executive Summary**

Laurel Bridge is an advanced, next-generation medical imaging orchestration platform that integrates the robust routing capabilities of Compass with the automated prior retrieval and workflow orchestration of Navigator, purpose-built to meet the clinical, technical, and regulatory needs of NHS Trust Radiology Departments.

Designed for seamless integration with Radiology AI algorithms and NHS PACS/RIS infrastructure, Beagle serves as a central control plane for all DICOM-based data movement, ensuring secure, intelligent, and automated imaging workflows across legacy and modern systems.

---

## **🧠 Key Capabilities**

### **1\. Unified DICOM Routing and AI Workflow Management**

* Consolidates Compass' DICOM routing engine and Navigator's prior-fetch logic into a single platform.  
* Enables AI-ready workflows, directing exams to AI inference engines, RIS/PACS, and storage archives in parallel or sequentially.  
* Flexible support for Store and Forward and Direct routing logic with multi-destination orchestration.

### **2\. Radiology AI Integration Framework**

* Routes studies to AI analysis platforms based on modality, body part, patient demographics, or referring physician.  
  Supports round-trip workflows: ingestion → AI analysis → results returned as DICOM SR, PDF, or HL7 messages.  
* Advanced filtering and matching rules to ensure only clinically relevant cases are routed to AI endpoints.  
* Customizable Job Actions to handle AI result re-ingestion, HL7 alerts, or smart routing to consultants.

### **3\. Smart Prior Retrieval**

* Automatically retrieves prior studies based on MWL, HL7, or RESTful triggers, optimized for NHS PACS configurations.  
* Context-aware retrieval: filters priors by body part, modality, adjacency, and age of exam.  
* Retention policies ensure transient caching to align with NHS data governance guidelines.

### **4\. NHS IT and Security Compliance**

* Native support for TLS 1.2/1.3, encrypted HL7, Active Directory/LDAP, and auditable role-based access control.  
* End-to-end audit logging for every action, message, and routing event, aligned with DICOM PS3.15 security standards.  
* Designed for high-availability and failover-ready installations, including support for Windows Server clusters.

---

## **🛠️ Technical Features**

| Feature Category | Capability |
| :---- | :---- |
| Routing Engine | Store & Forward, Direct Routing, Multi-destination, Load Balancing |
| Trigger Sources | DICOM MWL, HL7 ADT/ORM, REST API, CSV Polling |
| Destination Types | DICOM SCU/SCP, AI Engines, PACS, VNA, RIS, Cloud (AWS S3, GCP, Azure) |
| Workflow Automation | Job Actions, Retry Logic, Custom Scripting (C\#/.NET), Event Hooks |
| Security | FIPS-compliant TLS, Certificate-based Auth, Logging Suppression for PHI |
| Web Interface | Secure browser access to job queues, logs, sources/destinations, cache |
| Cache Management | Transient DICOM cache with purging policies, searchable via C-FIND |
| HL7 Integration | Bidirectional messaging with hospitals' RIS, support for ACK/NAK, HL7 v2.x |
| AI-Specific Tools | Inference tracking, SR/PDF mapping, Confidence score filtering, delay logic |

---

## **🧩 Interoperability & NHS Alignment**

* Fully supports IHE profiles (e.g., SWF, PIR, XDS-I) used in NHS systems.  
* Compatible with PACS vendors like Sectra, GE, Agfa, and RIS systems commonly used across Trusts.  
* Designed to function behind NHS N3/HSCN firewalls, supporting proxy configurations and network zoning.  
* Adapts to Trust-specific governance, including Information Governance (IG) Toolkits, and DSCN compliance.

---

## **🚀 Deployment & Scalability**

* Modular architecture: scale from a single-site hospital to multi-site Trust environments.  
* Deployable on virtualized Windows environments or cloud-hosted infrastructures (with NHS Digital guidance).  
* Silent install options and remote license management ease Trust-wide deployment.  
* Integration-ready via Compass APIs, HL7 messaging, and RESTful endpoints.

---

## **📊 Use Cases in NHS Context**

* Automated AI Integration: Automatically route chest X-rays to a triage AI for suspected COVID findings.  
* Efficient Prior Study Retrieval: Pull 2-year priors for oncology follow-up imaging automatically before reporting.  
* Teleradiology Routing: Direct night-time trauma scans to outsourced radiology providers based on rule conditions.  
* Disaster Recovery Prep: Redirect studies to offsite VNA if PACS heartbeat fails.

---

## 

## **🧩 Differentiators**

| Laurel Bridge | Other Solutions |
| :---- | :---- |
| Combines routing \+ prior \+ AI logic | Typically siloed across multiple platforms |
| Workflow-aware DICOM/HL7/REST orchestration | Rudimentary DICOM routing only |
| Built-in compliance tooling for NHS | Requires third-party add-ons |
| Supports local \+ cloud-based AI engines | Limited cloud support or rigid integrations |

---

## **📦 Packaging & Licensing**

* Available in Base, Enterprise, and AI-Enhanced editions.  
* Perpetual or annual license models available for NHS procurement.  
* Site-based pricing to fit within NHS Trust budget structures.

---

## **📞 Support & Services**

* Backed by Laurel Bridge’s Tier-3 support team with NHS project experience.  
* Optional onboarding packages, site assessments, and custom HL7/DICOM mapping services.  
* Regular software updates with support for NHS LTS (Long-Term Support) Windows platforms.

**Use Cases**

## **1\. AI Triage for Emergency Radiology Cases**

### ***Use Case: AI-Driven Prioritisation of Chest X-rays in A\&E***

**Scenario:**  
An NHS Trust A\&E department receives a high volume of chest X-rays, many of which require urgent attention (e.g., suspected pneumothorax or pulmonary embolism).

**How Laurel Bridge Helps:**

* Automatically routes CXR exams from A\&E to an AI inference engine upon acquisition.  
* Applies DICOM filters (modality \= CR/DR, body part \= Chest, source \= A\&E).  
* AI-generated structured reports are ingested, and critical findings (e.g., high confidence pneumothorax) trigger escalation workflows.  
* HL7 messages or SMS/email alerts are sent to on-call radiologists or consultants.

**Outcome:**  
Faster triage of critical cases improves clinical response time, patient safety, and supports 24/7 diagnostic services.

---

## **2\. Smart Prior Retrieval for Oncology Follow-Up**

### ***Use Case: Automatically Fetch Relevant Priors for MDT Reviews***

**Scenario:**  
Patients undergoing cancer treatment require regular imaging reviews. Radiologists need historical scans to evaluate disease progression.

**How Laurel Bridge Helps:**

* On receiving a new oncology CT exam (via MWL or HL7 trigger), Laurel Bridge retrieves relevant priors (e.g., last 12 months, same body part).  
* Filters priors based on anatomy, modality, or referrer.  
* Delivers the new study and selected priors to the reporting workstation or PACS in one unified job.

**Outcome:**  
Saves radiologists time, reduces manual search errors, and ensures better diagnostic accuracy for MDT meetings and follow-up reviews.

---

## **3\. AI Result Integration and Data Governance**

### ***Use Case: Structured AI Outputs as DICOM SR into PACS***

**Scenario:**  
Trusts deploying AI (e.g., stroke detection or mammography CAD) often receive results in PDFs or external formats.

**How Laurel Bridge Helps:**

* Intercepts AI results and maps them to DICOM SR or PDF Encapsulated objects.  
* Inserts these into the correct patient/study folder in PACS using HL7 mapping and accession number reconciliation.  
* Supports anonymisation or tagging for research, audit, or QA initiatives.

**Outcome:**  
Enables clean and standards-compliant integration of AI results into the existing NHS infrastructure and audit trail, essential for governance and clinical documentation.

---

## **4\. Disaster Recovery and Business Continuity**

### ***Use Case: Seamless Routing to Offsite VNA During PACS Downtime***

**Scenario:**  
A Trust’s PACS is undergoing planned maintenance or experiences unplanned downtime.

**How Laurel Bridge Helps:**

* Monitors PACS availability using heartbeat sensing.  
* On failure, Laurel Bridge automatically reroutes incoming DICOM exams to an offsite VNA or backup PACS.  
* Sends HL7 notifications to RIS or staff indicating temporary redirection.

**Outcome:**  
Ensures zero-interruption diagnostic services, data integrity, and reduces manual intervention during outages.

---

## **5\. Outsourced and Night Hawk Reporting**

### ***Use Case: Conditional Routing for After-Hours Radiology Services***

**Scenario:**  
During overnight shifts or weekends, NHS Trusts often rely on teleradiology providers for out-of-hours coverage.

**How Laurel Bridge Helps:**

* Based on schedule and trigger conditions (e.g., 6 PM–8 AM, modality \= CT Head, location \= ED), Laurel Bridge routes exams to an external teleradiology service.  
* Ensures return of reports or structured data into the Trust’s RIS/PACS automatically.  
* Supports secure DICOM transmission over TLS and patient data logging for IG compliance.

Outcome:  
 Facilitates safe, efficient outsourcing without sacrificing control, compliance, or traceability.

