---
layout: post
title: "Bare Metal, Hyperscalers and HPCaaS: Discovering the HPC Deployment Capability Gap"
date: 2024-09-04
categories: [HPC, Cloud, Technology]
tags: [bare-metal, BMaaS, hyperscaler, HPCaaS, IaaS, cloud-infrastructure, site-reliability-engineering, SRE, devops, cloud-computing, AWS, Azure]
author: Scott Marshall and Andrew Holway
excerpt: "Choosing the right HPC deployment model isn't just about cost or performance—it's about the capabilities you need in-house to make it work. This article explores the trade-offs between Bare Metal, IaaS, and HPCaaS, and what they mean for your engineering team."
---
<br>
*In this article we discuss how High Performance Computing (HPC) can be deployed on different types of service provider. We believe that the most important factor when choosing the right service provider is the technical capability that has to be maintained within the purchasers organisation. Technical capabilities are difficult and very expensive to build and maintain, and the costs of this capability are often overlooked. This article is intended to expose the required capabilities for each service provider and to provide a guide to help navigate this tricky space.* 
<br>
<br>
<br>
There are generally considered to be three different types of service provider operating in the HPC space, bare metal as a Service (BMaaS), infrastructure as a service (IaaS), and high performance computing as a service (HPCaaS). All of these providers offer access to the physical infrastructure required for HPC, but they differ significantly in the capabilities a customer must possess in order to efficiently consume their service and receive genuine value from their offerings.

Choosing the correct service provider for a HPC project is a key strategic decision that potential consumers must make, and they will need to have a deep understanding of the capital and operating expenses associated with each service. They will also need to weigh up factors such as the requisite skill requirements, timescales and flexibility the different methods require in order to make an informed decision.

A useful metric that can help us compare and contrast these different vendors is Time To First Value (TTFV). This tracks how long it takes from when a customer first interacts with a company’s product or service to when they actually create or receive something of value from it.   
An example of this is a drug discovery company, whose first moment of real value from a HPC service provider would be when their research team is unblocked and able to actually begin conducting their computational research.

Whilst they are capable of generating immense amounts of computing power and handling incredibly complex problems, ultimately, HPC systems or supercomputers are built from off the shelf commodity components. They may be specced to maximum memory and be packed with the fastest processors available, but they all start as standard servers.

The art of turning these standard servers into beastly machines pumping out results at unheralded speeds is one of the key challenges of the HPC setup process, and, depending on the route a company has chosen, may require a number of key competencies to be present in the organisation.
<br>
<br>
## SRE vs. DevOps
<br>
Despite the intricacies inherent in setting up and deploying HPC clusters, there is a scarcity of software options on the market seeking to make the process easier. Previously, Bright Cluster Manager played a pivotal role in helping companies streamline the HPC setup process, but after being [acquired](https://blogs.nvidia.com/blog/bright-computing-hpc/) by NVIDIA in 2022, the platform is no longer a readily available, cost efficient solution.

This software gap has amplified the importance of Site Reliability Engineering (SRE) and DevOps(Developer Operations), complex capabilities which are often difficult to define, build and maintain.

Created by Google, [Site Reliability Engineering](https://sre.google/) is an engineering practice focused on building and maintaining reliable cloud services. SRE engineers must be proficient in software development and possess a deep understanding of network, storage, and compute systems. They create the infrastructure and operational frameworks that enable Infrastructure as a Service (IaaS) cloud services to function. This makes SRE an alternative to traditional infrastructure operations, emphasizing automation, scalability, and proactive problem-solving.

DevOps, on the other hand, involves the consumption and configuration of cloud services, often through scripting and automation. DevOps teams use third-party tools to deploy and manage applications in the cloud, focusing on delivering quicker value, and leveraging the foundational infrastructure provided by SRE teams to ensure their services run efficiently and reliably. In essence, SRE creates the platform, while DevOps consumes it.

A DevOps engineer will not be able to fully realise the job of a trained SRE engineer, as the skill set required is an order of magnitude more complex, and this is reflected in their comparative salaries.
<br>
<br>
## Bare Metal as a Service (BMaaS) 
<br>
Some providers, such as [Hetzner](https://www.hetzner.com/) and [Teraswitch](https://teraswitch.com/), offer only bare metal. They provide their customers with access to the physical infrastructure, but they don’t provision the software and services required to deliver a full end to end solution.

Due to the lack of turnkey HPC operating systems on the market today, organisations using BMaaS will require a highly skilled SRE team in place to ensure they can design and create a HPC system that brings them value. Purchasers assume responsibility for ensuring they have the correct physical infrastructure, potentially handling the design and management of servers, storage and networking.

Whilst they offer the cheapest prices for the raw compute resources, the total cost of ownership for customers can be very high unless a careful consideration of how the economies of scale will be unlocked is in place. Highly skilled SRE engineers will be required and the system must be carefully architected to ensure appropriate performance is squeezed from every component. 

The strategic decisions that need to be made when considering BMaaS mean that the consumer has a greater amount of control in how they set up their systems. However, the complexities that need to be addressed before an end user can begin their work means that BMaaS has the longest TTFV out of the three main types of provider
<br>
<br>
## Infrastructure as a Service (IaaS)
<br>
[Hyperscalers](https://www.redhat.com/en/topics/cloud-computing/what-is-a-hyperscaler) like [Amazon Web Services](https://aws.amazon.com/), [Google Cloud](https://cloud.google.com/), and [Microsoft Azure](https://azure.microsoft.com/en-gb) offer IaaS, providing their customers with flexible, on-demand access to resources, and a suite of tools designed to help streamline setting up computing environments.

These providers help administrators with mid range skill sets set up projects in a reasonable timeframe, but they are not necessarily best geared towards running HPC workloads. It is certainly possible to create HPC clusters using IaaS services, but they are more explicitly designed for web applications. A high DevOps skill level is needed to successfully deploy HPC workloads, and internal teams are still responsible for making their own architectural decisions.

Building and maintaining HPC resources on IaaS will require strong DevOps practices to be in place, but deploying HPC using hyperscalers is comparatively easy when compared to BMaaS. The majority of SRE work has already been completed, and whilst there is still a high necessity for DevOps engineers, they are ultimately configuring reliable third party services rather than being tasked with working directly on top of bare metal.

IaaS providers will often offer generous free credit packages on signup, but running HPC workloads can burn through these credits very quickly. It can be easy for a company to have spent so much time setting up resources and learning the platform, that they tend to just continue using the service, even when the premium pricing kicks in. 

There is a high potential for vendor lock-in once these credits run out. DevOps engineers who have poured a lot of time and effort into configuring HPC on a platform may not want to have to reconfigure an entirely new system elsewhere, or may lack the knowledge to be able to do so. Each hyperscaler uses a unique user interface, so switching providers will require time and effort for staff to learn how to use the new platform. The big IaaS providers leverage this resistance to change to help ensure that they keep customers using their services.

Hyperscalers can be very expensive, sometimes 10x more costly than BMaaS providers. Their pricing can reflect the fact that companies like Amazon and Google are household names, which gives them some leeway to charge consumers premium fees. Discounts for longer term commitments are available however, and negotiations with account managers can yield better pricing for yearly spends over $1Million.

They also offer customers a cheaper alternative via their spot pricing model, offering unused computing resources for a heavy discount. This can dramatically increase ROI, but these spot instances are always at high risk of being reclaimed, with the jobs paused and the resource moved to a higher paying customer. This can cause delays to a project, especially if the monitoring systems are not optimised properly. 

Consumers must also consider the location of a service provider’s data centres. Hyperscalers will generally have access to data centres all across the globe, and have the infrastructure to offer customers more localised resources, which can help decrease latency and negate potential data transfer compliance issues. Bare metal and HPCaaS providers generally have a much narrower range of locations on offer, and can struggle to match hyperscalers’ near global coverage.
<br>
<br>
##  High Performance Computing as a Service (HPCaaS)
<br>
An increasingly common third option on the market is HPCaaS such as [Dug](https://dug.com/hpcaas/) and [Rescale](https://rescale.com/platform/hpc-as-a-service/). Alongside providing customers with physical infrastructure, this business model also offers direct support for the end user’s applications. HPCaaS companies deliver an end to HPC service, typically tailored to a specific application or field. Dug, for example, focuses on providing solutions for the geoscience industry. Leveraging their knowledge of a specific sector allows them to provide customers with an off the rack solution that enables the end user to start working almost immediately, creating a TTFV of essentially zero.

HPCaaS providers offer the consumer a ‘[white glove](https://www.mckinsey.com/capabilities/operations/our-insights/the-future-of-customer-experience-personalized-white-glove-service-for-all)’ service, providing them with a highly personalised experience that guides them seamlessly through the onboarding and HPC environment setup process. This type of service completely mitigates the need for the purchasers to maintain SRE and DevOps capabilities.

This increased speed of receiving value does not necessarily result in a more expensive service. Whilst They may not be able to match BMaaS on the price of raw resources, the fact they remove a large chunk of the HPC admin burden present with the other types of vendor makes them a very cost effective option, especially if a company chooses a provider whose area of expertise aligns with their own. They also offer the added benefit of providing customers with a single monthly invoice, ensuring customers know exactly what they’re paying for without any hidden costs.

HPCaaS also has the benefit of a fairly low risk of vendor lock-in. Even if providers are not necessarily keen to help users migrate their data off the platform, the low investment level from the consumer means that the cost of changing providers is minimal. Unlike with IaaS where DevOps staff will need to learn and configure new interfaces for each platform, the uniformity of industry specific research software means that a company can easily switch to a different HPCaaS provider and seamlessly continue their work.
<br>
<br>
## On Premises 
<br>
Alternatively, depending on the size of the organisation, and the amount of computationally complex tasks they are undertaking, a company may also consider installing their own HPC solution on premises. Whilst for some companies this may be a viable path, this route requires a very large upfront investment, and realistically needs top tier SRE capabilities. It will likely necessitate hiring HPC experts to organise and maintain the systems, and these are extremely expensive and notoriously difficult to retain.
<br>
<br>
## Conclusion
<br>
Each of the three main service providers carry with them significant differences in the capability required to reach the point of receiving value. Bare Metal as a Service gives consumers access to the cheapest base resources and the greatest control over their system architecture, but requires a very high engineering skill level and carries with it the longest timescale for achieving value. Companies need to be confident of the economies of scale when choosing the BMaaS route.

Infrastructure as a Service providers are an order of magnitude less complex to use than bare metal providers, and have a time to first value around 1/10th of that of BMaaS. They also require a much lower engineering complexity, and the necessary DevOps skills are much easier to build and maintain than the SRE capabilities required for BMaaS. Whilst they can be much more expensive, spending money on IaaS is much easier and less risky than building a complex engineering capability to take advantage of low prices on bare metal. 

High Performance Computing as a Service offers a time to first value of essentially zero, and handles the complexities of SRE and DevOps for their clients. If an organisation can find a provider whose core area of expertise aligns with their own, then HPCaaS offers a cost effective, easy to manage solution that allows consumers to start seeing real results straight out the box.