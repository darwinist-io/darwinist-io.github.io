---
layout: document
title: "Understanding The Use of Clinical AI Across England’s NHS Trusts"
subtitle: "A comprehensive analysis of clinical AI adoption across England’s NHS trusts, based on 120 FOI responses. Discusses adoption rates, leading vendors, governance, barriers to scale, and future directions for AI in UK healthcare."
date: 2025-06-10
author: "Darwinist Team"
tags: ["Clinical AI", "NHS", "Radiology AI", "Healthcare Technology", "FOI", "UK Health", "AI Adoption"]
category: "Medical AI Solutions"
featured: true
hidden: false
toc: true
excerpt: "A comprehensive analysis of clinical AI adoption across England’s NHS trusts, based on 120 FOI responses. Discusses adoption rates, leading vendors, governance, barriers to scale, and future directions for AI in UK healthcare."
---

## **Executive Summary** {#executive-summary}

This report examines the current state of adoption, procurement, and governance practices of clinical artificial intelligence in England’s NHS trusts as of late 2024, based on Freedom of Information (FOI) responses from 120 secondary care trusts.

There are broadly two types of AI in use clinically. Convolutional Neural Networks (CNNs) which power radiology and pathology imaging AI tools, and text based Large Language Models (LLMs). LLMs can be further subdivided into point-of-care ambient recording tools and summarisation tools. For this purpose of this report these three clinical AI use cases will be referred to as **Radiology AI**, **Ambient AI**, and **Summary AI**.

Radiology AI was by far the most prevalent type of AI reported, with only a handful of trusts reporting usage of Ambient AI, and no mention at all of Summary AI.

The responses reveal a 50% adoption rate. 36 different AI providers were cited, with neuroradiology and stroke support AI vendor [Brainomix](https://www.brainomix.com/) seeing the greatest penetration. Since the data was collected, some trusts have clarified their responses, and [Annalise](https://annalise.ai/) appears to have become the most widely adopted provider.

However, higher penetration does not equate to high usage, with adoption mostly limited to small scale pilot projects. Only around 1% of England’s medical images in 2024 were touched by AI tools. Higher usage volumes were observed in MSK support tools, and these represent a potential high growth use case, with AI’s ability to produce richer reporting being particularly important.  

Procurement and governance practices were at an early stage, but clearly of importance to trusts keen to build decision making frameworks. Some trusts have established internal steering groups, while others relied on Integrated Care Boards (ICBs) or regional networks for decision-making.

It appears clear that AI will increasingly impact care over the coming years, but human oversight will remain essential. The role of radiologists will likely have to shift towards a more holistic understanding of the deployment of AI across healthcare settings.

---

## **Response Results** {#response-results}

On the 18th September 2024, Darwinist sent out FOI requests to 149 NHS trusts. Trusts were asked for details regarding any AI tools that were currently being used for diagnosis or treatment of patients within the trust. Additionally, details on the usage frequency, and copies of any policies, procedures or committee notes regarding selection and implementation were requested. 

Trusts were chosen because of the presence of radiology capabilities, as this was Darwinist’s focus at the time. Ambulance and mental health trusts were not contacted. 120 trusts responded to the FOI request, and 29 either did not respond at all, or declined to respond citing the Section 31 (1) FOI exemption regarding cyber security concerns. 

Perhaps as was to be expected given the independent nature of trusts, there was significant variation in adoption across the country. Responses were split exactly down the middle, with 60 trusts reporting AI use, and 60 trusts saying they were not. Each of the 12 community trusts that were contacted confirmed that they had not implemented any form of clinical AI. 

The responses present a clear picture of the main providers of radiology AI products to trusts and their levels of penetration. There were a total of 36 different vendors reported, with the vast majority being Radiology AI solutions for diagnostic imaging. In general, usage numbers for the applications were relatively low, even for those with greater numbers of installations. 

* Stroke Detection \- [Brainomix](https://www.brainomix.com/) (16 trusts) and [RapidAI](https://www.rapidai.com/) (12 trusts) are widely used for acute stroke diagnosis and care.

* Chest Imaging \- [Annalise](https://annalise.ai/) (11 trusts), [Aidence Veye](https://www.aidence.com/veye-lung-nodules/) (8 trusts) [Behold AI Red Dot](https://www.behold.ai/our-solutions/red-dot-ct-head/)**\*** (5 trusts) are used for triaging chest CTs and x-rays. 

  ***\***In January 2025, Behold AI went into [administration](https://www.digitalhealth.net/2025/01/digital-health-startup-behold-ai-enters-administration/).*

* Cardiovascular Imaging \- [HeartFlow](https://www.heartflow.com/) (10 trusts) and [Circle CVI](https://www.circlecvi.com/) (2 trusts) are used for cardiac image analysis.

* Fracture Detection and Bone Age \- Systems such as [Gleamer BoneView](https://www.gleamer.ai/solutions/boneview) (4 trusts), [Radiobotics RBfracture](https://radiobotics.com/solutions/rbfracture/) (2 trusts), and [BoneXpert](https://bonexpert.com/) (2 trusts) appear in orthopaedic workflows. 

* Dermatology \- [Skin Analytics DERM](https://skin-analytics.com/) (8 trusts) is being used in teledermatology triage.. 

* Radiotherapy \- Tools like [RaySearch Laboratories’ RayStation](https://www.raysearchlabs.com/raystation/) (2 trusts) and [Limbus AI](https://limbus.ai/) (1 trust) are being used in radiotherapy for contouring and treatment planning. 

* Image Reconstruction \- Scanner-specific tools such as [Siemens Deep Resolve](https://www.siemens-healthineers.com/en-uk/magnetic-resonance-imaging/technologies-and-innovations/deep-resolve) (3 trusts) and [Canon AICE](https://uk.medical.canon/aice/) (1 trust) are being used to reconstruct MRI images and check scan quality. 

Neurology, and especially stroke, provides a strong use case for radiology AI. Because of the critical time savings they provide, stroke AI tools present the largest impact on patient outcomes. As of late 2024, it appears that all [107 stroke units](https://www.digitalhealth.net/2024/12/all-107-stroke-centres-in-england-using-ai-technology-says-nhse/) across England had implemented AI. Despite this widespread adoption though, stroke imaging only accounts for around 0.2% of the total annual medical images taken across the NHS.

In contrast, musculoskeletal (MSK) imaging constitutes a significantly larger share of annual scans, and vendors like Gleamer and Radiobotics saw some of the highest usage volumes reported by trusts. However, these volumes only represented a tiny fraction of the NHS’s total MSK scans, presenting a key potential high growth area. 

Mammography is also a discipline where radiology AI shows great potential. Vendors such as [Lunit](https://www.lunit.io/en) and [Kheiron Medical Technologies](https://www.kheironmed.com/) were reported by trusts, and in February 2025, the NHS [announced plans](https://www.theguardian.com/society/2025/feb/04/nhs-to-launch-worlds-biggest-trial-of-ai-breast-cancer-diagnosis) for the world’s largest AI breast cancer diagnosis trials.

Additionally there was some sporadic reporting of Ambient AI tools, such as [Nuance Speechmagic](https://www.nuance.com/en-gb/index.html) for medical transcription, and the creation of patient information videos via [Synthesia](https://www.synthesia.io/). It is possible that Ambient AI usage was underreported by trusts, as they may have felt they fell outside the scope of clinical AI as defined in our request.

It is worth noting that the majority of these responses likely came from the radiology team, so tools being used in cardiology and pathology, for example, may be under-reported. Annalise, BoneXpert and Brainomix responded to this study noting significant under-reporting of their products, but Darwinist was unable to validate the exact extent of their deployment in the NHS.

Some AI vendors reported additional contracts signed outside of the scope of the study. Given the speed of deploying new radiology AI into trusts is slow, Darwinist believes that, despite this, there has been no significant changes in how radiology AI tools are impacting care since the study was conducted. 

---

## **Governance and Guidance** {#governance-and-guidance}

Some trusts did not have any AI policies, guidelines and frameworks in place, but a significant portion of responders said they were in the process of drafting them. A small number of trusts indicate that they have AI steering groups or AI governance boards set up.

A number of responses note that pilot trials are underway and implemented in trusts through region wide initiatives orchestrated by integrated care boards (ICBs) or imaging networks.

AI approval processes often overlap with general digital governance committees and policies. Trusts referred to guidelines and frameworks such as DTAC (Digital Technology Assessment Criteria) and “A Buyer’s Guide to AI in Health and Care” as part of their embryonic assessment protocols.

---

## **What's Stopping Adoption - Radiology AI** {#adoption-at-scale}

From the overall usage statistics provided, it can be estimated that AI tools are only used on around 1% of medical images produced in England. Darwinist spoke to a number of NHS staff, AI vendors, Health Innovation Networks and representatives of industry bodies such as the ABHI to try to uncover the factors which appear to be blocking adoption at scale.

### **Business Cases** {#business-cases}

Radiology AIs are packages of single task computer vision tools, which cannot be used for diagnosis without the oversight of a radiologist. They are certified medical devices, and can only operate within the confines of that regulatory framework. Each radiology AI tool comes with a set of technical integration requirements that the IT department has to manage, both in the initial installation and across the entire product lifecycle.

Some filter out scans with no significant findings, prioritising patients, but all scans still require signoff by a human radiologist. Our data suggests that, depending on volume, radiology AI products can cost up to £30 per scan, however they often do not significantly reduce reporting time. As the hospital is already paying the radiologist, it appears that at their current price point and under current regulations, radiology AI does not necessarily represent good value for money for NHS trusts.

### **Sustainability** {#sustainability}

There are also serious concerns regarding vendor longevity. The majority of radiology AI vendors are still early stage companies, and there is a deep market consolidation under way. Whilst many vendors are moving towards becoming sustainable, it is inevitable that many more will go under. Venture capitalists backing clinical AI vendors are beginning to demand financial results, and companies who are unable to deliver these may find themselves in a perilous situation. The recent case of Behold AI, who went into administration despite being deployed in a number of trusts, provides a warning for procurement departments.

### **Reporting** {#reporting}

Radiology AI does have the potential to deliver much more comprehensive and accessible radiology reporting quality. Current radiology reporting standards often provide short, text based results, but AI can generate much richer and more visually comprehensive outputs, making them easier for patients and consulting clinicians to interpret and act on. This is especially powerful in MSK, where a more thorough report has the potential to improve the level of care across both NHS and private treatment. 

Radiologists report on a specific query, and do not review every frame of every image. Radiology AI tools have a significant advantage over their human counterparts in this way, as they can assess every pixel and easily highlight areas of interest a human may have missed. 

Radiology AI’s analytical vigilance may though lead to a rise in incidentalomas, unexpected findings of uncertain clinical significance. Like full body scanning, this can pose complex ethical challenges and may ultimately prove detrimental to the delivery of care. Whilst early detection could be potentially life saving, additional findings are often benign, and their over-reporting could lead to unnecessary investigations, distressing patients and wasting valuable hospital resources.

### **Resistance to Change** {#resistance-to-change}

Institutional inertia, decision paralysis and clinical resistance may be proving to be bottlenecks for adoption. There is understandable reticence amongst some radiologists to adopt tools which are perceived to be a threat to their relevance. Whilst in the short to medium term, radiology AI tools simply augment a clinician’s existing workflows, there is potential for a future in which AI diagnoses patients without human supervision, creating an existential threat to the practice.

However, radiology, as a practice, may be best placed to control all forms of AI in clinical environments. Radiologists are capable physicists and mathematicians, meaning they are the best placed of any medical discipline to understand the probabilistic risk profiles and other mathematical concepts that need to be addressed in the application of radiology and summary AI tools.

It is also worth noting that some of the perceived resistance is down to a lack of resources. There is a disparity in digital maturity levels across trusts, and some simply do not have the requisite IT staff numbers and experience to be able to dedicate time to implementing new AI tools.

---

## **What's Stopping Adoption - Summary AI** {#summary-ai}


### **Access to Data** {#access-to-data}

Compared to radiology AI tools, which have limited scope, summary AI solutions have the potential to touch every branch of medicine, and there is already [evidence](https://hai.stanford.edu/news/ai-can-outperform-humans-writing-medical-summaries) showing clinicians prefer summaries generated by AI tools. There are a wide range of different use cases for summary AI including point of care, discharge notes, letters to GPs and patients, forensic reporting, care plan generation and quality assurance assessments.

Whilst radiology AIs have relatively simple DICOM in/DICOM out workflows, summary AIs are an order of magnitude harder to implement. They require integrations with a wide range of disparate and usually antiquated clinical information systems.

The quality of clinical record keeping in the UK is generally very strong, especially when compared to health systems around the globe. However, NHS trusts currently have to use a number of different proprietary clinical information systems to store this data. The vendors of these systems often have opaque access methods, and exert a level of control over the data which makes it difficult for trusts to innovate.

### **Transparency** {#transparency}

Currently available LLM models already have the capability to generate good quality patient summaries, but their use must be tightly controlled. For example, it is not appropriate for a doctor to simply copy and paste a summary from ChatGPT, as it does not provide the necessary transparency. Similarly, black box LLM models hosted inside hospital IT departments do not provide outputs which can safely be used clinically. Human-in-the-loop systems will enable clinicians to use AI to extract, examine, transform patient data within a safe and controlled environment.

Much like radiology AI tools, summary AI tools still require a trained clinician to make the final call on its results. The ultimate responsibility must still reside with the clinicians.

---

## **What's Stopping Adoption - Ambient AI** {#ambient-ai}

While ambient AI solutions, such as voice-driven transcription and documentation assistants, are present in the wider clinical landscape, there was very little usage of them reported by the trusts in our sample. As such, Darwinist does not currently have sufficient evidence to comment meaningfully on their implementation. 

Whilst further investigation would be required before drawing conclusions about the role they play at NHS trusts, it does appear that pinning a microphone to a patient somewhat changes the environment under which care is delivered. Beyond the practicalities of setting up recording equipment in clinical scenarios, ambient AI’s presence could have a detrimental impact on a patient’s levels of honesty and anxiety, especially in sensitive or embarrassing cases. 

The BMA has also [raised concerns](https://www.digitalhealth.net/2025/06/bma-warns-gps-on-the-substantial-risks-of-ai-scribing-tools/) that ambient AI tools are being adopted into clinical workflows without the necessary clinical safety and data protection checks being in place. 

---

## **The Future of Clinical AI** {#the-future-of-clinical-ai}

Radiology AI has presented humanity with an excellent new tool in its diagnostic arsenal, but its development and delivery sits mostly in the hands of VC backed firms whose commercial necessities mean that it may not be able to reach a price point that makes it feasible for mass adoption. 

Some radiology AI vendors have argued that implementation costs are trending slowly downwards, but the realities of meeting regulatory requirements may be the true obstacle in achieving such a price point. Regardless of commercial motivations, radiology AI tools will generally need to reach £1 to enable ubiquity.

Whilst there will undoubtedly be high intensity pathways where vendors are essential, it may be the case that development of radiology AI tools must transition into the hands of healthcare providers. Hospitals are sitting on vast quantities of imaging data, and given the right platform, could begin training their own CNN models on their own patient data.

If a self-trained clinical AI tool is being used exclusively within the healthcare provider that built it, medical device clearances can be avoided, removing a key resource drain from the process. There is even scope for the sharing of AI models between trusts. Imaging networks and integrated care boards could assume the responsibilities needed to coordinate the sharing of data and quality management systems required for the creation of AI tools by NHS trusts.

Similarly, Darwinist can see trusts leveraging the contents of their clinical information systems to fine-tune their own LLM models. By ingesting their entire catalogue of clinical guidelines, alongside medical records they can create highly localised AI which allow a much deeper analysis of trust operations and patient cohorts. However, to fully realise this scenario, there needs to be a shift away from the proprietary and antiquated clinical information systems currently in place at most trusts. 

The NHS is keen to push towards the open data sharing standard [FHIR](https://digital.nhs.uk/services/fhir-apis). Services such as [Microsoft’s Azure FHIR Store](https://learn.microsoft.com/en-us/azure/healthcare-apis/fhir/overview) and open source alternative [HAPI FHIR](https://hapifhir.io/) provide the functionalities and performance for clinical data storage which can allow trusts to fine tune AI models.

Darwinist believes that summary AI tools present the most compelling use of AI in healthcare. At the point of care, clinicians could have clear, concise information about the presenting patient, allowing them to make quicker, more informed decisions. The potential for summary AIs to standardise discharge notes, letters to patients, and communications with other organisations is immense.

Darwinist believes that the clinical use of summary AIs should follow a similar pattern to radiology AI, with oversight from a trained clinician being essential. The reporting physician will order a report from a summary AI in much the same way as they would order a medical image.  
A specially trained clinical professional then validates that the quality of the data is suitable for safe and accurate use in generating a report.

New clinical roles will likely have to be created in order to facilitate the clinical assessment of content for summary generation. To support clinicians in their journey to becoming experts in the deployment and use of AI in medical practice, Continual Personal Development programmes will need to be designed and delivered in collaboration with leading universities and the Royal Colleges of Medicine.

Darwinist also believes that Quality Improvement Projects (QIPs) are a highly important process in the development and deployment of AI. If junior doctors are given the correct tools and training in how to safely deploy AI, QIPs can create an iterative, evidence based route to adoption. 

---

## **Conclusion** {#conclusion}

In recent years, AI has been held up by the tech community as an unstoppable force which will dramatically change the delivery of care. In reality, AI is not a silver bullet. To have this heralded transformational effect on healthcare, standards and practices of medicine may have to be torn up, and the responsibility of clinicians reduced.

Despite this, the responses in this study shows that the use of AI in clinical environments, and in particular radiology AI, is rising across England’s NHS trusts. It is clear though, that both the field of medicine, and society as a whole, is still very early in the AI journey. 

Society must be careful not to place unrealistic expectations on new AI technologies. It would be a fallacy to suggest that AI adoption should be blocked because it cannot achieve perfection. It is much more reasonable to measure the performance of AI in clinical settings against current clinician error rates, rather than insisting that it be held to an impossible standard.

The NHS today is facing a 30% shortfall of radiologists, which is compounding a potential [six week](https://www.rcr.ac.uk/news-policy/policy-reports-initiatives/state-of-the-wait/) waiting time for radiology reporting. Many of today’s radiology AI solutions are already mature enough to show significant efficiency gains and improvements in the quality of care.

But as radiology AI tools begin to handle more and more of the heavy lifting, will the position of radiologists in the diagnostic chain need to change? Is there a future in which AI renders radiologists redundant? It may be the case that radiologists need to shift from a focus on imaging to a broader engagement with a range of AI workflows.

Darwinist believes the only safe, clinically reliable way for AI to be adopted is by maintaining human supervision. This clinician-in-the-loop principle does pose a unique challenge for the business case of radiology AI tools though. If the route to mass adoption relies on utilising existing human resources, can radiology AI provide enough additional value to justify its use? 

There is a common maxim that argues that for a new product to displace an existing solution, it must be ten times better than what it seeks to replace. Perhaps, apart from time critical niche use cases such as stroke, radiology AI does not currently provide a radical enough improvement to the status quo to justify the technical, political and financial switching costs.

Maybe the true value of radiology AI sits outside of diagnosis. Perhaps the radiology workflow continues as it is, with radiologists still in place. AI could expand out their reports to offer much richer, more easily digestible information, understood by a broader spectrum of people involved in diagnosis and recovery. 

The future of clinical AI application development and deployment may well need to be in the hands of Trusts, rather than commercial entities. By bringing AI training and inference in-house, trusts, imaging networks and ICBs could leverage their existing data and guidelines to create clinically potent, cost effective AI tools. 

---

## **Response Breakdown by Trust** {#response-breakdown-by-trust}

Below is a list of the responses provided by the NHS Trusts. The level of detail provided reflects that of the trust’s response.  


## **Trusts Stating The Use of Clinical AI** {#trusts-stating-the-use-of-clinical-ai}

* **Barking, Havering and Redbridge University Hospitals NHS Trust**  
  Uses Aidoc AI (Radiology), Brainomix (Stroke CT), Combinostics cNeuro (Brain MRI).

* **Buckinghamshire Healthcare NHS Trust**  
  Uses Aidence (CT Chest) and Skin Analytics DERM. Aidence had 1177 uses between March and August 2024\. DERM saw 863 uses between January and October 2024\.

* **Calderdale and Huddersfield NHS Foundation Trust**  
  Uses BeHold AI Red Dot (Chest X-ray prioritisation).

* **Chesterfield Royal Hospital NHS Foundation Trust**  
  Setting up Annalise Chest X-Ray Reporting (not yet used on patients); uses IschemaView RapidAI software on 2 CT scanners, but the data is handled at Sheffield Teaching Hospitals.

* **Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust**  
  Piloting Annalise AI (Radiology), live for only 4 weeks as of October 2024\.

* **Dorset County Hospital NHS Foundation Trust**  
  Uses Aidence/DeepHealth Veye Lung Nodules (Chest CT), iSchemaView RapidAI (Neuro), Skin Analytics DERM.

* **East & North Hertfordshire NHS Trust**  
  Uses Behold AI Red Dot, Brainomix, and a targeted lung health check AI service.

* **East Suffolk and North Essex NHS Foundation Trust**  
  Uses Neu Health, Gleamer Boneview, Brainomix, and HeartFlow. Brainomix saw 1745 uses between August 2023 and August 2024\. Boneview had 17,174 uses between June and September 2024\.

* **East Sussex Healthcare NHS Trust**  
  Uses Brainomix to process all patients referred by stroke team (887 in 23/24), HeartFlow (used 57 times in 23/24).

* **Epsom and St Helier University Hospitals NHS Trust**  
  Uses Annalise for chest x-ray and iSchemaView Rapid AI for brain CT scans. Annalise is being used on a trial basis, but has been used on 68,000 scans in the past year. Rapid AI was procured by Surrey Stroke Network.  

* **Frimley Health NHS Foundation Trust**  
  Uses Annalise AI and Ufonia.

* **Gateshead Health NHS Foundation Trust**  
  Uses Annalise for GP X-ray diagnosis support only.

* **Gloucestershire Hospitals NHS Foundation Trust**  
  Uses Brainomix eStroke in thrombectomy assessment before transfer.

* **Great Ormond Street Hospital for Children NHS Foundation Trust**  
  Uses BoneXpert to detect pediatric bone age (1277 uses in previous 12 months).

* **Great Western Hospitals NHS Foundation Trust**  
  Uses Ultromics EchoGo (Radiology) and Brainomix (Stroke) recommended by the Thrombectomy Innovation and Transformation Network (TITAN) regional stroke network.

* **Guy’s and St Thomas’ NHS Foundation Trust**  
  Uses AI currently for background tasks such as treatment planning and bone age assessment, is also trialling additional AIs and developing AI evaluation policy.

* **Hampshire Hospitals NHS Foundation Trust**  
  Uses HeartFlow (Cardiac CT), iSchemaView RapidAI (Stroke), Lucida Medical (Prostate), Aidence, Cascination CAS 1, MModal (transcription).

* **Harrogate and District NHS Foundation Trust**  
  Uses Radiobotics RBfracture, and Annalise in clinical decision support capacities, and Nuance Speechmagic/Dragon Medical for transcriptions.

* **Hull University Teaching Hospitals NHS Trust**  
  Uses iSchemaView RapidAI (stroke), Aidence (2777 lung checks in 12 months), Synthesia AI (patient information videos).

* **James Paget University Hospitals NHS Foundation Trust**  
  Uses Medtronic GI Genius within colonoscopy only as part of a national research project.

* **Kettering General Hospital NHS Foundation Trust**  
  Uses Radiobotics RBfracture in A\&E (approximately 25,000 exams in 12 months).

* **King’s College Hospital NHS Foundation Trust**  
  Uses IschemaView RapidAI (stroke), Medtronic GI Genius (endoscopy), Elaitra ViewFinder (breast imaging), and has built an in-house NLP product.

* **Kingston Hospital NHS Foundation Trust**  
  Piloting Skin Analytics DERM for teledermatology triage.

* **Lancashire Teaching Hospitals NHS Foundation Trust**  
  Uses Body Vision LungVision for exploratory bronchoscopy procedures. 26 Lung Navigation procedures were performed between August 2023 and September 2024\.

* **Leeds Teaching Hospitals NHS Trust**  
  Uses RaySearch Laboratories RayStation segmentation tool for radiotherapy treatment planning, Lunit INSIGHT MMG for mammography, and Siemens Deep Resolve for MRI image reconstruction. RayStation processed approximately 1000 treatment plans per annum. Lunit was used on around 90,000 mammograms.

* **Liverpool Heart and Chest Hospital NHS Foundation Trust**  
  Early adopters in 2015/16 of Aidence Veye Analysis and HeartFlow. Uses Aidence for approximately 100 analyses per day and HeartFlow 10–15 times a month.

* **Manchester University NHS Foundation Trust**  
  Uses Skin Analytics DERM for dermatology triage. Used on 1166 patients between May and October 2024

* **Mid and South Essex NHS Foundation Trust**  
  Uses Behold AI Red Dot (chest x-ray), Brainomix (stroke detection support), Deep Medical (outpatient data analysis).

* **Mid Cheshire Hospitals NHS Foundation Trust**  
  Conducting Pilot study of Skin Analytics DERM in dermatology.

* **Mid Yorkshire Hospitals NHS Trust**  
  Uses iSchemaView RapidAI to assist in secondary capture and radiology reporting. Used for 1025 studies in the previous year.

* **Milton Keynes Hospital NHS Foundation Trust**  
  Uses Canon AICE and Siemens MRI Deep Resolve for image reconstruction, Gleamer Boneview (MSK X-Ray), AIDOC iPE (chest CT); trialing Brainomix e-Stroke suite.

* **Norfolk and Norwich University Hospitals NHS Foundation Trust**  
  Uses Brainomix.

* **North West Anglia NHS Foundation Trust**  
  Confirmed that they are using clinical AI, but refused to list providers, invoking a Section 31 FOI exemption. 

* **Northern Care Alliance NHS Foundation Trust**  
  Uses iSchemaView RapidAI for category 1 stroke detection and Motilent (in selected sites); implementing Annalise. RapidAI saw 1763 uses in the previous year.

* **Northern Lincolnshire and Goole NHS Foundation Trust**  
  Uses iSchemaView RapidAI (stroke), Aidence (lung screenings), Synthesia AI (patient information videos), iRefer (clinical decision support). Also exploring additional AI products and use cases.

* **Northumbria Healthcare NHS Foundation Trust**  
  Uses Brainomix and HeartFlow.

* **Royal Cornwall Hospitals NHS Trust**  
  Uses Brainomix eCTA in stroke/decision-making. 288 usages between September 2023 and September 2024\.

* **Royal Papworth Hospital NHS Foundation Trust**  
  Uses Brainomix 4-5 times monthly, HeartFlow 20 times monthly, and Circle CVI 250-300 times monthly.

* **Royal Surrey NHS Foundation Trust**  
  Evaluating the use of Annalise AI for chest x-rays.

* **Salisbury NHS Foundation Trust**  
  Uses Biotronics 3D, Circle, Aidence, Brainomix, and Heartflow.

* **Sheffield Teaching Hospitals NHS Foundation Trust**  
  Confirms it uses AI systems but is unable to provide specific details.

* **Somerset NHS Foundation Trust**  
  Uses Behold AI, Lucida Medical AI (prostate), Brainomix and Skin Analytics DERM.

* **South Tees Hospitals NHS Foundation Trust**  
  Uses Annalise for Chest X-rays, a prostate AI recommended by NPIC, and the Mvision radiotherapy segmentation suite.

* **Tameside and Glossop Integrated Care NHS Foundation Trust**  
  Trialling Annalise for triaging chest x-rays as part of a wider Greater Manchester initiative.

* **The Christie NHS Foundation Trust**  
  Uses AI tools daily for Chest X-Ray decision support and radiotherapy auto-segmentation, but did not specify which products.

* **The Clatterbridge Cancer Centre NHS Foundation Trust**  
  Uses Limbus for auto-contouring of vital organs in radiotherapy planning.

* **The Princess Alexandra Hospital NHS Trust**  
  Uses Riverain ClearRead for chest CT, Lunit for mammography, and Behold AI for high confidence normal scan reporting for chest x-ray.

* **The Rotherham NHS Foundation Trust**  
  Trialling Gleamer BoneView for emergency department X-ray imaging as part of ICB initiative. 25-30k uses across the previous year.

* **The Royal Marsden NHS Foundation Trust**  
  Uses Siemens Deep Resolve for MRI image reconstruction and RaySearch Laboratories RayStation for radiotherapy planning.

* **University Hospitals Dorset NHS Foundation Trust**  
  Uses iSchemaView RapidAI in the stroke department, Heartflow in cardiology, Skin Analytics in dermatology, and Aidence Targeted Lung Health Check.  

* **University Hospitals of Morecambe Bay NHS Foundation Trust**  
  Uses BoneXpert for bone age assessments, Annalise for chest X-ray, Brainomix for CT based stroke decision support.

* **University Hospitals Of Leicester NHS Trust**  
  Confirmed that they are using clinical AI, but refused to list providers, invoking a Section 31 FOI exemption.

* **University Hospitals Sussex NHS Foundation Trust**  
  Uses Brainomix, Kheiron MIA, HeartFlow, and also indicated an AI enhanced patch for arrhythmias.

* **West Hertfordshire Teaching Hospitals NHS Trust**  
  Uses HeartFlow.

* **West Suffolk NHS Foundation Trust**  
  Uses Skin Analytics on a daily basis.

* **Whittington Health NHS Trust**  
  Uses Gleamer BoneView.

* **Worcestershire Acute Hospitals NHS Trust**  
  Uses iSchemaView RapidAI for stroke/thrombectomy decisions in close association with University Hospitals Birmingham NHS Foundation Trust.

* **Wrightington, Wigan and Leigh Teaching Hospitals NHS Foundation Trust**  
  Uses AZmed Rayvolve for fracture detection in MSK X-rays. 64,356 uses between January and October 2024\. 

* **Wye Valley NHS Trust**  
  Uses AI in stroke thrombectomy triage in partnership with University Hospitals Birmingham NHS Foundation Trust.

* **York and Scarborough Teaching Hospitals NHS Foundation Trust**  
  Uses iSchemaView RapidAI for CT stroke perfusion imaging, and is trialling Kheiron MIA for mammography.

---

## **Trusts Stating They Do Not Use Clinical AI** {#trusts-stating-they-do-not-use-clinical-ai}

* **Airedale NHS Foundation Trust**  
* **Alder Hey Children’s NHS Foundation Trust** (BoneXpert stated they are a customer)  
* **Barnsley Hospital NHS Foundation Trust**  
* **Bedfordshire Hospitals NHS Foundation Trust**  
* **Birmingham Community NHS Foundation Trust**  
* **Birmingham Women’s and Children’s NHS Foundation Trust**  
* **Blackpool Teaching Hospitals NHS Foundation Trust**  
* **Bolton NHS Foundation Trust**  
* **Bradford Teaching Hospitals NHS Foundation Trust**  
* **Bridgewater Community Healthcare NHS Foundation Trust**  
* **Cambridgeshire Community Services NHS Trust**  
* **Central London Community Healthcare NHS Trust**  
* **Croydon Health Services NHS Trust**  
* **Derbyshire Community Health Services NHS Foundation Trust**  
* **George Eliot Hospital NHS Trust**  
* **Gloucestershire Health and Care NHS Foundation Trust**  
* **Hertfordshire Community NHS Trust**  
* **Homerton Healthcare Foundation Trust**  
* **Hounslow and Richmond Community Healthcare NHS Trust**  
* **Isle Of Wight NHS Trust**  
* **Kent Community Health NHS Trust**  
* **Leeds Community Healthcare NHS Trust**  
* **Lewisham and Greenwich NHS Trust** (no AI in use yet, although they are setting up governance. Deepc platform is deployed in the trust, but is not actually in use)  
* **Lincolnshire Community Health Services NHS Trust**  
* **Liverpool Women's NHS Foundation Trust**  
* **London North West University Healthcare NHS Trust**  
* **Medway NHS Foundation Trust**  
* **Mersey and West Lancashire Teaching Hospitals NHS Trust**  
* **Moorfields Eye Hospital NHS Foundation Trust**  
* **North Bristol NHS Trust**  
* **North Cumbria Integrated Care NHS Foundation Trust**  
* **North Middlesex University Hospital NHS Trust**  
* **North Tees and Hartlepool NHS Foundation Trust**  
* **Northampton General Hospital NHS Trust**  
* **Queen Victoria Hospital NHS Foundation Trust**  
* **Royal Berkshire NHS Foundation Trust**  
* **Royal Free London NHS Foundation Trust**  
* **Royal National Orthopaedic Hospital NHS Trust** (BoneXpert stated they are a customer)  
* **Royal Wolverhampton NHS Trust** (developing a policy, no AI in use yet)  
* **Sherwood Forest Hospitals NHS Foundation Trust**  
* **Shrewsbury & Telford Hospital NHS Trust**  
* **Solent NHS Trust**  
* **South Warwickshire NHS Foundation Trust**  
* **Stockport NHS Foundation Trust**  
* **Surrey and Sussex Healthcare NHS Trust**  
* **Sussex Community NHS Foundation Trust**  
* **The Dudley Group NHS Foundation Trust**  
* **The Hillingdon Hospitals NHS Foundation Trust**  
* **The Newcastle upon Tyne Hospitals NHS Foundation Trust**  
* **The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust**  
* **The Royal Orthopaedic Hospital NHS Foundation Trust**  
* **The Walton Centre NHS Foundation Trust**  
* **University Hospitals Bristol and Weston NHS Foundation Trust**  
* **University Hospitals Coventry & Warwickshire NHS Trust**  
* **University Hospitals of Derby and Burton NHS Foundation Trust**  
* **University Hospitals Plymouth NHS Trust**  
* **Walsall Healthcare NHS Trust**  
* **Warrington and Halton Teaching Hospitals NHS Foundation Trust**  
* **Wirral Community Health and Care NHS Foundation Trust**  
* **Wirral University Teaching Hospital NHS Foundation Trust** (reviewing regional AI, not currently in use)

---

## **Non-Responsive Trusts** {#non-responsive-trusts}

* **Ashford and St Peter's Hospitals NHS Foundation Trust**  
* **Barts Health NHS Trust**  
* **Cambridge University Hospitals NHS Foundation Trust**  
* **Chelsea and Westminster Hospital NHS Foundation Trust**  
* **Countess of Chester Hospital NHS Foundation Trust**  
* **County Durham and Darlington NHS Foundation Trust**  
* **Dartford and Gravesham NHS Trust**  
* **East Cheshire NHS Trust**  
* **East Kent Hospitals University NHS Foundation Trust**  
* **East Lancashire Hospitals NHS Trust**  
* **Imperial College Healthcare NHS Trust**  
* **Maidstone and Tunbridge Wells NHS Trust**  
* **Liverpool University Hospitals NHS Foundation Trust**  
* **Nottingham University Hospitals NHS Trust**  
* **Oxford University Hospitals NHS Foundation Trust**  
* **Portsmouth Hospitals University NHS Trust**  
* **Royal Devon University Healthcare NHS Foundation Trust**  
* **Royal United Hospitals Bath NHS Foundation Trust**  
* **Sandwell and West Birmingham Hospitals NHS Trust**  
* **Sheffield Children's NHS Foundation Trust**  
* **South Tyneside and Sunderland NHS Foundation Trust**  
* **St George's University Hospitals NHS Foundation Trust**  
* **The Queen Elizabeth Hospital, King's Lynn, NHS Foundation Trust**  
* **Torbay and South Devon NHS Foundation Trust**  
* **United Lincolnshire Hospitals NHS Trust**  
* **University College London Hospitals NHS Foundation Trust**  
* **University Hospitals Birmingham NHS Foundation Trust**  
* **University Hospitals of North Midlands NHS Trust**  
* **University Hospital Southampton NHS Foundation Trust**

---

## **Additional Responses** {#additional-responses}

On May 9th, 2025, we sent a copy of our compiled report to all of the trusts initially contacted, offering them the chance to correct or comment. The following trusts provided additional information.

* **Alder Hey Children’s NHS Foundation Trust**  
  *“We have now progressed rapidly, and we are piloting Ambient AI Scribe across Outpatients and AI Coding across Inpatients and Outpatients. We have a Board approved AI strategy and are in the process of mobilising this through 25/26.”*

* **Bradford Teaching Hospitals NHS Foundation Trust**  
  *“Since you sent your FOI request I can confirm we have started using Annalise AI in Radiology for chest x-rays.”*

* **East Cheshire NHS Trust**  
  *“Annalise Container. We also have DART for use in MSK community services. System only went operational 04/04/25. Annalise and DART are both ICB wide pilots that have been selected and implemented regionally. All the clinical safety case reports etc have been done at regional level.”* 

* **The Princess Alexandra Hospital NHS Trust**  
  *“Behold.AI no longer in use as the company went under.”*

* **University Hospital Southampton NHS Foundation Trust**  
  *“We would like to point out that we received your FOI request, and pointed you in the direction of our new FOI portal for requesting of FOIs.  We do not have any record of a resubmission on your part, and therefore it is not that we did not reply to your FOI, but we did not register a request through the portal.”*

* **Wrightington, Wigan and Leigh Teaching Hospitals NHS Foundation Trust**  
  *“Since this request was responded to on 8th October 2024, WWL have since gone live with Chest AI and Dermatology AI.”*

---

## **Appendix** {#appendix}

## **The FOI Request** {#the-foi-request}

Dear FOI Team,

I am writing to request information concerning the use and evaluation of clinical artificial intelligence systems within your trust. For the purposes of this request, 'clinical AI' refers to artificial intelligence models used in patient diagnosis or treatment.

**Context for the Request:**

The integration of AI technologies into healthcare is rapidly advancing and has the potential to significantly impact patient care, diagnostics, and treatment outcomes. Understanding how NHS trusts are adopting and utilizing clinical AI systems is crucial for assessing the current landscape, identifying best practices, and informing future developments in this field.

**Information Requested:**

**Current Use of Clinical AI Systems:**

**Question 1:** Does the trust currently use any clinical AI systems in diagnosing or treating patients?

**Details of Clinical AI Systems in Use:**

**Question 2:** Please provide a list of clinical AI systems currently used by the trust.

**Question 3:** If available, please provide any existing reports or summaries detailing the usage frequency of these clinical AI systems within the trust over the past 12 months.

**Decision Making for Clinical AI**

**Question 4:** If available, please provide copies of any policies, procedures, or committee meeting minutes from the past two years that outline how the trust selects and approves clinical AI systems for use.


