# Prospect: Aims Education Nigeria

**Phase:** 0  
**Sector:** Education / international student recruitment  
**Location:** Lekki, Lagos, Nigeria  
**Status:** INVESTIGATING  
**Research date:** 2026-10-02  
**Primary website:** https://aimseducation.com/nigeria

## Identity

Aims Education is an international education/student-recruitment organization with a Nigerian operation in Lekki and another Nigerian office in Ogudu/Ojota. Public university-agent directories independently list Aims Education as an education agent in Nigeria.

### Sources
- https://aimseducation.com/nigeria
- https://aimseducation.com/global-offices/nigeria
- https://www.bradford.ac.uk/international/country/nigeria/
- https://www.ulster.ac.uk/global/apply/agent-quality-framework/agents
- https://www.dmu.ac.uk/international/en/agents.aspx

## Business Understanding

Aims operates a multi-stage student recruitment and application workflow. Public service material describes counselling, university/course selection, document preparation, application submission, offer/application follow-up, visa/compliance support, and pre-departure/post-arrival support.

### Current public workflow reconstruction

Lead / enquiry
→ counselling
→ profile assessment
→ university/course selection
→ document collection/preparation
→ application
→ offer / conditions
→ compliance / visa
→ pre-departure
→ post-arrival support

This is a reconstruction from public service descriptions, not a claim about Aims' internal software state model.

### Sources
- https://aimseducation.com/nigeria
- https://aimseducation.com/nigeria/services/university-application
- https://aimseducation.com/nigeria/consultation

## Digital Footprint

### CRM

**Observation:** Aims job descriptions explicitly require staff to maintain student/application records in a CRM or management system.

**Evidence:**
- Student Counsellor role: CRM used for student details and applications.
- Canada Recruitment Officer role: CRM used while coordinating applications with universities and other offices.
- Compliance Officer role: CRM used for accurate records and reporting.

**Sources:**
- https://ng.linkedin.com/jobs/view/student-counselor-at-aims-education-3417896893
- https://ng.linkedin.com/jobs/view/international-student-recruitment-officer-canada-destination-at-aims-education-nigeria-3899305539
- https://ng.linkedin.com/jobs/view/compliance-officer-at-aims-education-nigeria-4022325960

### Structured lead capture

**Observation:** The current consultation flow collects structured prospective-student information including name, phone, email, residence, intake, destination, study level, subject and message.

**Source:** https://aimseducation.com/nigeria/consultation

**Unknown:** The current public evidence does not establish exactly how these submissions enter the CRM, how assignment occurs, or whether staff intervention is required.

### Existing automation / MIS project

**Observation:** Aims previously commissioned an operational software project from Adroit Infosystem.

A verified Clutch case study/review attributed to AIMS Education describes requirements including:
- internal operations automation
- Analytics/MIS
- website + Facebook + WhatsApp integration
- lead tracking from inquiry to enrollment
- follow-ups, reminders and document-submission workflows
- invoicing/accounts-receivable automation

**Reported results:** Aims reported a 20% reduction in processing time for key operations and a 25% reduction in data-entry/processing errors, alongside reported cash-flow/operational benefits from accounts-receivable automation.

**Important temporal limitation:** The project is listed as beginning in 2021 and the review was published in 2024. It is evidence of a historical/current-at-the-time system requirement, not proof that the same gaps remain in 2026.

**Source:** https://clutch.co/profile/adroit-infosystem

### Technology hiring

**Observation:** Aims has recruited web-development talent. A published Web Developer role listed WordPress customization, Figma, HTML, CSS, JavaScript and PHP responsibilities.

**Source:** https://www.myjobmag.com/jobs/latest-jobs-at-aims-education

**Inference:** Some website technology work is/was handled as an internal capability rather than being entirely outsourced.

**Unknown:** The role description does not establish the relationship between the public website, internal CRM, MIS, integrations, or other operational systems.

## Operational Complexity Signals

### Multi-party workflow

Aims' published service model involves coordination among students, counsellors, compliance staff, universities and other offices. This creates a potentially complex information flow.

**Inference:** Cross-system synchronization, reporting, notifications, document state, deadline management and ownership of records are reasonable investigation targets.

**Confidence:** Medium for complexity; no claim that a problem exists.

### Growth / multi-office operation

Aims currently lists multiple Nigerian offices and has recruited for branch, counselling, compliance and related roles.

**Inference:** Scaling across offices may increase the importance of shared records, reporting, workflow consistency and system integration.

**Confidence:** Medium.

## Opportunity Hypotheses

These are hypotheses only and are NOT established business problems.

### H1 — Post-implementation integration / modernization
The historical automation system may have evolved unevenly as the business, website, offices and service scope changed.

**Potential capabilities:** Integration, backend/API engineering, internal software, digital transformation.

**Confidence:** Low–Medium.

### H2 — End-to-end student lifecycle visibility
The original automation project strongly emphasized lead-to-enrollment. Aims' current public service scope extends beyond enrollment into applications, compliance, visa and post-arrival support.

**Question:** Does the current system provide a unified lifecycle view from lead through post-arrival outcome?

**Potential capabilities:** Internal software, dashboards, APIs, automation.

**Confidence:** Low–Medium.

### H3 — Website/CRM lead synchronization
The current website collects structured leads while Aims still relies on CRM-based student/application management.

**Question:** Are web leads automatically normalized, deduplicated, assigned and tracked in the CRM?

**Potential capabilities:** APIs, integrations, workflow automation.

**Confidence:** Low.

### H4 — Deadline/document workflow automation
Aims publicly describes handling application deadlines, payment deadlines, interview dates and document workflows.

**Question:** Are reminders, escalations and document-state transitions fully automated across all active applicants?

**Potential capabilities:** Automation, notifications, internal dashboards.

**Confidence:** Low–Medium.

## What Is NOT Established

- The current CRM vendor/platform.
- Whether the Adroit-built system is still the active system in 2026.
- Whether Adroit still maintains it.
- Current backend/database/hosting architecture.
- Current website-to-CRM integration architecture.
- Current WhatsApp/Facebook integrations.
- Whether duplicate leads or manual data transfer occur.
- Whether deadline/document workflows are manual.
- Whether Aims currently has a technology problem requiring an external vendor.

## Highest-Value Research Questions

1. What CRM/platform does Aims currently use?
2. Is the 2021+ Adroit system still active, and what parts does it cover?
3. Is Adroit still a technology partner?
4. How does the current website consultation form feed the CRM?
5. How are WhatsApp enquiries attached to student records?
6. How are leads assigned to counsellors?
7. How are duplicate leads handled?
8. How are documents stored, versioned and verified?
9. How are application/payment/interview deadlines tracked and escalated?
10. Does one record contain the complete student journey?
11. How are the Lekki and Ogudu offices synchronized?
12. Who owns technology decisions and vendor relationships?
13. What does the internal Web Developer actually maintain?
14. What technology work is currently being hired or outsourced?

## Current Assessment

Aims Education is a **qualified Phase 0 investigation candidate** because there is unusually strong public evidence of an existing technology-dependent operating model and a documented history of purchasing operational automation.

However, **no current 2026 business problem has been proven yet**.

The next investigation should focus on the current architecture and post-implementation gaps rather than pitching generic software development.

**Core Issachar question:** What changed in Aims' operating system between the documented automation project and its current multi-office, multi-service operation—and is there evidence of a new unresolved constraint?
