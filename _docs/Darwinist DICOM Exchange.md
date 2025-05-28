---
layout: document
title: "Darwinist DICOM Exchange: National Level Medical Imaging Platform"
subtitle: "Cloud-native medical imaging exchange platform built on Azure DICOM/FHIR services, Laurel Bridge routing engines, and MedDream viewer, offering secure federated image sharing, AI-ready infrastructure, and browser-based diagnostics as a modern alternative to traditional HSCN-restricted imaging networks."
date: 2025-05-27
author: "Darwinist Team"
tags: ["DICOM", "Medical Imaging", "NHS", "Cloud Technology", "FHIR", "Healthcare Infrastructure", "AI Integration"]
category: "Healthcare Technology"
featured: true
toc: true
hidden: true
excerpt: "Cloud-native medical imaging exchange platform built on Azure DICOM/FHIR services, Laurel Bridge routing engines, and MedDream viewer, offering secure federated image sharing, AI-ready infrastructure, and browser-based diagnostics as a modern alternative to traditional HSCN-restricted imaging networks."
---

# Executive Summary

The **[NHS Image Exchange Portal]({{ site.baseurl }}/docs/nhs-image-exchange-portal-iep/) (IEP)**, operated by **Sectra**, has long served as the national standard for medical imaging transfer across UK healthcare organisations. While it enables vital cross-Trust image sharing, it remains constrained by outdated architecture, limited accessibility, and poor alignment with modern NHS priorities.

IEP is:

* **Dependent on manual workflows** for report ingestion and consent  
* **Closed to FHIR, AI, or cloud-native integration**  
* **Expensive and non-extensible**, especially for private or research use  
* **Unsuitable for Imaging Network consolidation**

As NHS England transitions toward **cloud-first policies**, **AI augmentation**, and **open standards**, it is imperative to modernise how imaging is accessed, exchanged, and governed.

### **Darwinist DICOM Exchange is the solution: a modular, cloud-native imaging exchange platform designed to supersede the limitations of the IEP.**

Built with:

* **Azure DICOM and FHIR Services**  
* **Laurel Bridge Compass and Navigator**  
* **MedDream zero-footprint viewer**  
* **Python Flask for orchestration and consent UI**

It offers a secure, scalable, and open alternative to IEP—enabling **federated image sharing**, **AI-ready infrastructure**, and **workflow automation** tailored to the evolving needs of NHS Trusts, Imaging Networks, and diagnostic innovators.

---

## **1\. Product Overview**

**Darwinist DICOM Exchange** is a federated, standards-based radiology platform enabling **secure image exchange, metadata integration, and browser-based viewing** across institutions. It supports both clinical and research use cases and is designed to modernise diagnostic workflows while maintaining compliance, scalability, and cost-efficiency.

---

## **2\. Technology Stack**

| Component | Functionality |
| :---- | :---- |
| **Azure DICOM Service** | Secure image archive and API-based DICOMweb access |
| **Azure FHIR Service** | Imaging metadata mapped to FHIR for EPR integration and governance |
| **Laurel Bridge Compass** | Rules-based DICOM/HL7 routing engine |
| **Laurel Bridge Navigator** | Automated priors fetching and workflow execution |
| **MedDream Viewer** | CE-certified HTML5 diagnostic viewer |
| **Python Flask \+ Bootstrap** | UI for workflow control, consent dashboards, and logs |

---

## **3\. Key Features**

### **✅ Modern Image Exchange**

* DICOMweb-based routing via HTTPS, no VPN or node installs  
* Secure access beyond HSCN—supports remote reading and cloud workflows  
* Cross-Trust federation and metadata alignment

### **✅ AI-Ready and FHIR-Native**

* Study metadata streamed into **FHIR resources**  
* Enables downstream integration with EPR, AI, registries, and analytics  
* Supports real-time triggers for AI and reporting engines

### **✅ Zero-Footprint Viewing**

* **MedDream HTML5 viewer** supports full diagnostic capabilities, MPR, overlays, annotations  
* Seamless access from NHS desktops, mobile, and home environments  
* Compatible with structured reporting and collaborative MDT use

### **✅ Automated Routing and Priors Retrieval**

* **HL7/MWL/REST triggers** initiate prior fetching and DICOM routing  
* Rule-based filtering by modality, date, or clinical need  
* Retry logic and failure audit trails included

### **✅ Consent and Compliance UI**

* Flask UI allows:  
  * Patient-specific consent flagging  
  * Audit logs of study access  
  * Role-based views and data request workflows  
* FHIR-linked consent tracking possible via Azure Health APIs

---

## **4\. NHS Use Case Alignment**

| Scenario | Capability |
| :---- | :---- |
| **Cross-Site Image Sharing** | Federated DICOM access via Azure |
| **AI Deployment & Validation** | Routing to/from AI tools with built-in de-ID |
| **Community Diagnostics** | Browser-based access with no local infrastructure |
| **Virtual Clinics & MDTs** | Real-time collaboration in the MedDream viewer |
| **Clinical Trials & Research** | Consent-governed data ingestion, export, anonymisation |
| **Subject Access Requests** | Secure, auditable study release workflow |

---

## **5\. Security & Compliance**

* **TLS encryption**, **OAuth2**, **Azure Private Endpoints**  
* Compliant with:  
  * **NHS Data Security and Protection Toolkit**  
  * **ISO/IEC 27001**  
  * **GDPR & HIPAA**  
* **RBAC** and **Active Directory integration**  
* Full audit trail for DICOM, FHIR, and user access

---

## **6\. Competitive Advantages vs. NHS IEP**

| Feature | Darwinist DICOM Exchange | NHS IEP |
| ----- | ----- | ----- |
| Network Access | Secure internet access | HSCN only |
| Standards | DICOMweb \+ HL7 \+ FHIR | DICOM \+ HL7 |
| Viewer | CE-certified HTML5 viewer | Limited web viewer |
| AI Integration | Native routing \+ metadata | Not supported |
| Consent UI | Built-in tracking \+ audit | Manual or external |
| Speed to Deploy | Cloud setup in hours | Node installs in weeks |
| Extensibility | Python/REST APIs and plugins | Closed architecture |
| Pricing | SaaS \+ Azure consumption | Tiered fixed fees |

---

## **7\. Deployment Options**

* **Azure-native**  

---

## **8\. Roadmap**

* NHS-native **consent registry API integration**  
* **FHIR Subscriptions** for live alerting  
* **LLM compatibility** for auto-reporting and natural language queries  
* Optional **patient portal** for imaging access

---

## **9\. Conclusion**

**Darwinist DICOM Exchange** provides a next-generation alternative to the IEP—offering **cloud-native access**, **AI readiness**, **FHIR compatibility**, and **browser-based diagnostics** in one unified platform. It empowers NHS Trusts to modernise imaging workflows, reduce reliance on proprietary systems, and embrace secure, scalable radiology infrastructure aligned with national strategy.

