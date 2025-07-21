---
layout: post
title: "No Smoke Without FHIR: Why Open Standard Data Stores Should Become Systems of Record"
date: 2025-07-10
categories: [healthcare, interoperability, digital-health]
tags: [FHIR, open-standard, EHR, clinical-data, NHS, HL7, data-infrastructure, healthtech, AI-in-healthcare, data-store, health-data]
author: Scott Marshall and Andrew Holway
excerpt: "Despite generating mountains of data, healthcare providers remain at the mercy of proprietary systems that limit access and innovation. Could open standards like FHIR offer a path to truly interoperable and intelligent health systems?"
---

<br>
The healthcare industry is one of the biggest producers of data in the world. But what level of control do healthcare providers really have over the zettabytes of information pumped out every year?

As Mark Twain (probably never) said, “data is like garbage, you better know what you’re going to do with it before you collect it.” On the surface it appears that hospitals and clinics are not heeding his advice, with estimates of [up to 97%](https://www.weforum.org/stories/2019/12/four-ways-data-is-improving-healthcare/) of healthcare data going untouched once it's been collected.

Compliance laws demand the collection of this information, but do clinicians and researchers really not know what to do with this deluge of data? Or is it that the industry’s current database management landscape precludes them easily accessing the information they require?  Data has to be stored somewhere, but are healthcare professionals being kept outside the perimeter of guarded silos, with access to information doled out like gruel to Twist?

Surely there must be an alternative, a world where patient data isn't held at the behest of tycoons, and a lingua franca can provide equity of access to organisations big and small. 

 <br>

### **A Captive Audience**
<br>
Everyone knows the frustration of having to explain the same symptoms again and again as they move from triage through treatment, with staff in different departments unable to adequately communicate with each other.

This scenario occurs in large part due to the clinical information systems that are tasked with storing medical data. Currently, the main culprits are the monolithic Electronic Health Records (EHRs) where patient records are usually held. The majority of EHR vendors insist on storing medical data in their own proprietary formats, which means that the information cannot easily be communicated across clinical systems. 

The data layers of these EHRs are decades old proprietary relational schemas, and because each vendor closely guards that schema, every integration requires the use of a paid-for interface engine. These system architectures don’t allow for the rapid development of new features, and adding a new clinical concept means a major release.

This lack of interoperability has traditionally been one of the biggest challenges in the digitisation of healthcare, to the point where legislation such as the 21st Century Cures Act was brought in to force vendors to use FHIR based APIs to allow clearer communication between systems.

Despite acknowledging the importance of digital health records, healthcare professionals are still highly sceptical about the practicalities of using them. Staff in the NHS report issues accessing notes and test results, and the recent [Digital Maturity Assessment](https://www.theregister.com/2025/04/10/nhs_electronic_records_face_skepticism) shows that although 90% of trusts have an EHR, only 10–30% of these EHRs have more advanced functions. Even more worryingly, a [2024 BBC FOI investigation](https://www.digitalhealth.net/2024/05/bbc-investigation-links-nhs-it-failures-to-patient-harm/) reported 89 trusts where EHR outages or data access issues directly put patients at risk, leading directly to three deaths.  

Moving between proprietary EHR providers is extremely prohibitive, and would likely require a multi year migration project. This often leaves healthcare providers locked in to expensive, burdensome contracts, unable to adopt innovations that don’t play by the proprietary rulebook.

There are over [25](https://6b.digital/insights/list-of-eprs-in-nhs-trusts-in-england) different EHR providers across the NHS, which has helped create such a  disjointed data landscape, but at least there is a competitive market. In the US, Epic has achieved such a monopoly in the EHR space that it is being accused of [breaking anti-trust laws](https://www.forbes.com/sites/sethjoseph/2025/05/14/trouble-at-the-top-epic-faces-mounting-antitrust-allegations-even-as-it-grows/).

<br>
### **We Didn’t Start the FHIR**
<br>
Fast Healthcare Interoperability Resources (FHIR) is a globally recognised standard designed to enable consistent data exchange between a range of disparate systems. Publicly released in 2014, FHIR was developed by Health Level 7 International, a not for profit organisation historically responsible for the implementations of clinical information standards.

The standard is built on core building blocks called resources. Each FHIR resource represents a distinct healthcare concept, such as a ‘patient’, ‘practitioner’, 'appointment’, or ‘procedure’, and defines a structured, standardised way to represent that piece of information across digital health systems.

EHR systems consist of databases, with a suite of API and UI tools on top which provide a range of different clinical and administrative data interaction functionalities. Proprietary EHR vendors build both the database and the tools themselves, meaning they mediate how and when data is accessed, and by who. 

However, it is also possible to use FHIR as a way to store medical data. A FHIR store is essentially just an API server that sits in front of a database, providing a much more open alternative to getting data in and out.

Many legacy providers trumpet their support of FHIR, and proudly boast of their suite of APIs designed to help out the little guy. But the options on offer are limited, and proprietary providers only really provide a curated selection of interoperability tools, giving third parties limited access to their data kingdoms. For anyone who wants to work with FHIR resources not currently served by existing APIs, there is a massive premium to pay.
<br>
<br>
### **Fighting Fire with FHIR**
<br>
One of the core benefits of utilising FHIR as the system of record is that it provides the potential ability for any number of software providers to operate on the data simultaneously. Hospitals are free to procure innovation from a much wider range of sources, with smaller vendors able to implement agile new tools without having to negotiate ‘interface fees’ with proprietary gatekeepers.  

Using FHIR stores decouples the processing of patient data from the storage of patient data, and storage becomes an easily manageable commodity resource. EHR vendors will be forced to shift from data controllers to data processors, and their products will be just another application interacting with the data. This forces them to compete purely on the quality of their user experiences, and makes the experience of moving between EHR vendors becomes a much simpler, cheaper process.

Open standards like FHIR are also inherently AI-friendly, and we’re entering the vibe coding era, where the technical cost of specialised programmers developing software is closing in on zero. This gives anyone utilising open standards to develop new applications a distinct advantage over those building proprietary tooling, as AI tools have fully ingested the widely available schemas and can produce repeatable outputs based on them. 
<br>
<br>
### **Keep a Little FHIR Burning**
<br>
As part of its recent 10 year plan, the UK government has [reiterated its commitment](https://www.gov.uk/government/publications/10-year-health-plan-for-england-fit-for-the-future/fit-for-the-future-10-year-health-plan-for-england-executive-summary) to developing a ‘single patient record’, and NHS England guidelines mandate that [FHIR UK Core](https://digital.nhs.uk/services/fhir-uk-core) should be the common language underpinning it. 

Perhaps in a perfect world, every clinical system would be built on top of FHIR, and interoperability would be a moot point. However, even with the industry pushing for the widespread adoption of FHIR, proprietary providers are currently too ingrained into workflows for this utopia to become reality in the short term.

However there are already technical solutions on the market which healthcare providers could leverage. Both open source solutions like [HAPI FHIR](https://hapifhir.io/) and commercially supported packages from the likes of [Microsoft](https://learn.microsoft.com/en-us/azure/healthcare-apis/fhir/overview) and [Smile Digital Health](https://www.smiledigitalhealth.com/) offer clinical FHIR repositories for storing medical data and the API tools for interacting with it. An organisation could self-host their own server on premise, or work with a third party cloud PaaS provider without compromise on compliance or safety.

Given their prominence across health journeys, could it be the case that GPs become primary data providers, operating FHIR stores as the core system of record for a patient? Perhaps the fragmented GP landscape and their reliance on outdated technology means they may not currently be able to implement the infrastructure required for such a task.  

Maybe a better option would be for the creation of a new organisation which is responsible for maintaining the FHIR store. As long as legal mandates support the necessity of all medical data being sent to this organisation, a centralised data controller could handle all the translation of proprietary data into FHIR, meaning trusts are not under pressure to implement and maintain additional FHIR layers. 
<br>
<br>
### **Conclusion**
<br>
There appears to be two paths forward for healthcare providers. They can continue to procure and deploy legacy systems with proprietary databases, or they can push for the adoption of new ways of storing and accessing data, where they have the freedom to integrate with a wide ecosphere of applications.  

FHIR offers the perfect platform for the future of medical data management. In reality, the move to FHIR is something of a foregone conclusion, given the governmental and institutional push. Perhaps by establishing a system where mandates push patient data to a national level data provider, the healthcare industry can speed up its journey to the medical data promised land. 