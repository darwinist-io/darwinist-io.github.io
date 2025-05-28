---
layout: document
title: "NHS Image Exchange Portal (IEP): National Medical Imaging Infrastructure"
subtitle: "Critical Analysis of Sectra's Monopoly on UK Healthcare Image Exchange"
date: 2025-05-27
author: "Darwinist Team"
tags: ["NHS", "Medical Imaging", "Healthcare Infrastructure", "DICOM", "Market Analysis", "Healthcare Policy", "Radiology"]
category: "Healthcare Infrastructure"
featured: true
toc: true
excerpt: "Comprehensive analysis of the NHS Image Exchange Portal operated by Sectra, examining how this national platform enables secure transfer of 6+ million daily DICOM studies across 500+ healthcare organizations, supporting critical patient care workflows while exploring the market dynamics and access considerations for different provider types."
---

# Overview

The **Image Exchange Portal (IEP)** is the **national medical imaging exchange platform** commissioned by **NHS England** and operated exclusively by **Sectra Limited**. It enables secure, efficient transfer of **DICOM-format diagnostic imaging studies**—including CT, MRI, ultrasound, and X-rays—between NHS Trusts, private hospitals, and teleradiology providers across the UK. The portal is a critical component in the continuity of care, especially for urgent, multisite, or specialist clinical scenarios.

# Executive Summary

The **NHS Image Exchange Portal (IEP)** is a national platform operated exclusively by **Sectra Limited**, enabling the secure transfer of diagnostic imaging between NHS Trusts, private hospitals, and teleradiology providers. Commissioned and centrally funded by NHS England for public-sector institutions, the IEP facilitates the exchange of millions of DICOM-format radiology studies across more than 500 organisations. It serves as the critical backbone for image sharing in patient transfers, multidisciplinary team discussions, second opinions, and outsourced radiology reporting. The IEP operates over the NHS Health and Social Care Network (HSCN) and has no national-level alternative or equivalent competitor.

Sectra holds a **monopoly position** over national radiology image exchange in England, with all NHS Trusts relying on its infrastructure for cross-organisational interoperability. NHS organisations cannot currently procure or operate a competing national exchange platform, and all image transfers outside of local PACS peer-to-peer integrations must route through Sectra’s IEP. The platform supports standard DICOM protocols and integrates with major PACS and RIS systems, though manual steps are often required for study reconciliation and report imports. The IEP’s market exclusivity stems from its role as the centrally procured solution, creating a single point of dependency for imaging interoperability across the country.

Access to the IEP is **centrally funded for NHS Trusts** via a volume-based tiered model, where institutions pay annually based on their total number of image sends and receives. In contrast, **private diagnostic providers**, including teleradiology firms, are not covered by this national subsidy. These providers are typically billed **per study retrieved**, with reported rates of approximately **£8 per image transfer**, regardless of study complexity. This pricing model creates a substantial cost differential between public and private actors, with smaller private firms paying many times more per study than large NHS Trusts. As these costs are fixed per transaction, small firms operating at low volumes face disproportionately high financial barriers to participation in NHS diagnostic pathways.

The **pricing asymmetry** introduced by this model has tangible implications for **market access and competition**. Smaller and niche teleradiology providers—often those developing innovative reporting models, AI workflows, or flexible clinical services—find IEP access prohibitively expensive. This effectively limits their ability to participate in NHS contracts or deliver services at a competitive price point. While NHS Trusts benefit from economies of scale and subsidised infrastructure, private providers are burdened with costs that make scalable collaboration difficult. As a result, the current structure contributes to **market concentration**, restricts **operational diversity**, and may inadvertently **discourage technological innovation** within the diagnostic imaging ecosystem.

---

## **Access & Architecture**

* **Access Restricted to HSCN**: Only available via the **Health and Social Care Network (HSCN)**—formerly the N3 network.

* **Portal URL**: Accessible internally at [https://nww.iepservice.nhs.uk/IEP/External/Login](https://nww.iepservice.nhs.uk/IEP/External/Login).

* **Zero-footprint viewer**: Integrated web-based viewer (UniView) requires no client software and operates within standard NHS browser environments.

* **No public access**: Not usable from outside NHS networks (e.g., home or public internet).

* **Secure**: Encrypts all data in **transit and at rest**, ISO 27001 certified, compliant with the **NHS Data Security and Protection Toolkit**.

* **Audit Logs**: Stores transaction logs for **seven years**; the past **12 months** are visible in the portal.

* **Authentication**: NHS smartcard or equivalent secure credentials are required for login.

---

## **Functionality and Workflows**

* **DICOM Transfers**: Supports manual and automated **bidirectional image transfers**.

* **Clinical Contexts**: Used in emergency care, second opinions, teleradiology, MDTs, and referrals.

* **Backdating Support**: Manual workflows support **RIS backdating** to align with image acquisition dates.

* **Clinical Urgency Flags**: Users can flag transfers as "clinical emergency" for prioritisation.

* **Study Bundling**: Multiple studies for one patient can be bundled in a single transfer.

* **Temporary Storage**: Imported studies are stored temporarily—**typically deleted after 30 days** unless archived locally.

* **Manual Reconciliation**: Required for RIS/PACS alignment, especially in cases of **DICOM metadata mismatches** (e.g., patient ID discrepancies).

* **Attached Reports**: Some studies include radiology reports, though these often need to be **manually copied** into RIS (e.g., CRIS), flagged by UI icons.

---

## **Governance & Legal**

* **Data Controller**: NHS Trust.

* **Data Processor**: Sectra Limited.

* **Consent**: No enforced consent mechanism; the **sending organisation is responsible** for governance.

* **Fallback Mechanism**: In case of IEP outages, image sharing can revert to encrypted DVDs.

---

## **Pricing Model**

### **NHS Trusts:**

* **Tiered Pricing (Annual, volume-based)**:

  * Tier 1: £3,045 (\<500 studies)

  * Tier 2: £5,075 (up to 10,000 studies)

  * Tier 3: £8,120 (up to 25,000 studies)

  * Tier 4: £12,180 (up to 50,000 studies)

  * Tier 5: £18,000 (up to 100,000 studies)

* **Extras**:

  * Additional IEP node: £400 each

  * Auto Report Retrieval: £1,500/year

### **Private Providers:**

* Not funded by NHS England.

* Charged **per study**, up to **£8 per access**.

* Subject to **separate contracts with Sectra**.

**Example**: Gateshead Health NHS FT paid £13,812 in 2025-26 for Tier 3 service \+ viewer \+ node licence.

---

## **National Role and Strategic Importance**

* Used by over **500 healthcare organisations**.

* **More than 6 million images** processed daily.

* Originally for radiology, now extended to **cardiology**, **pathology**, and other imaging domains.

* Supports national strategies:

  * **ICS integration**

  * **Diagnostic transformation**

  * **Imaging network consolidation**

---

## **System Limitations and Issues**

* **No real-time streaming**, only DICOM study transfer.

* **Not a PACS replacement**: Functions as an exchange/routing layer.

* **Vendor Lock-in**: Sectra holds a **de facto monopoly**; no competing platform exists at national level.

* **Innovation Impact**: High access costs hinder **startups and small teleradiology providers**.

* **No open procurement route** for alternative platforms.

---

## **Examples of Usage and Integration**

* **CRIS Integration**:

  * Standard referral code: `"RNZ02EXT"`.

  * Consultant code: `"EXT"`.

* **Use Cases**:

  * Used for **SAR (Subject Access Requests)**.

  * Critical for transfers from **district hospitals to tertiary centers**.

  * Employed in research, trauma, and overflow services.

---

## **Support and Reliability**

* **98% service availability goal** (24/7/365).

* **Severity-based support model**:

  * Severity 1 outages: 4-hour resolution target.

* **Disaster Recovery**: Full DR and failover infrastructure in place.

---

## **Stakeholders & Users**

* **NHS Clinicians**: Radiologists, referrers, MDT participants.

* **PACS Administrators & Support Teams**

* **Teleradiology & Research Organisations**

* **Patients**: Indirectly through SARs and shared care.

---

## **Conclusion**

The **IEP is a foundational component** of national diagnostic services in the UK, enabling cross-organisational imaging exchange while complying with NHS security and governance standards. Despite its widespread use and importance, challenges such as **pricing asymmetries**, **vendor lock-in**, and **limited interoperability alternatives** have implications for innovation and competition, particularly affecting private providers and smaller players.

