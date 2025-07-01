---
layout: usability
title: "Usability-Driven Product"
hero_image: /assets/usability-hero.jpg
description: >
  "Darwinist combines usability engineering and WCAG-ready design to deliver safe, accessible, and clinician-friendly software for healthcare providers."
hero_title: "Usability"
hero_subtitle: >
  
hero_tagline: >
  "Designed for clinicians, built by patients."
hero_subtext: >
  "Darwinist integrates usability standards like IEC 62366-1 and WCAG 2.1 AA to reduce cognitive load, improve workflows, and enhance patient care."
client_brief:
  title: "Darwinist UI & UX Brief"
  version: "June 2025"

  standards:
    - name: "IEC 62366-1:2015 + Amd 1:2020"
      fa_icon: "fas fa-users-cog"          # human-factors engineering
      bootstrap_colour: "warning"
      description: >
        Usability-engineering process for medical devices; demands documented task
        analysis, iterative formative testing and summative validation to prove that
        UI-related risks are controlled in line with ISO 14971.
    - name: "WCAG 2.1 AA"
      fa_icon: "fas fa-universal-access"   # accessibility
      bootstrap_colour: "info"
      description: >
        Web Content Accessibility Guidelines baseline adopted by the NHS; requires
        ≥ 4.5 : 1 text contrast, keyboard operability, meaningful focus states and
        ARIA semantics for assistive technologies.

  palette_semantics:
    primary:
      description: "Neutral-anchor entities (Patient, DiagnosticReport, Practitioner)"
      fa_icon: "fas fa-link"
      bootstrap_colour: "primary"
    success:
      description: "Positive or completed states (Observation trends, Immunization records)"
      fa_icon: "fas fa-check-circle"
      bootstrap_colour: "success"
    danger:
      description: "High-risk data (Condition, AllergyIntolerance)"
      fa_icon: "fas fa-exclamation-triangle"
      bootstrap_colour: "danger"
    warning:
      description: "Time-critical or pending tasks (MedicationRequest, Appointment)"
      fa_icon: "fas fa-bell"
      bootstrap_colour: "warning"
    info:
      description: "Reference / context items (Procedure, CarePlan, Organization)"
      fa_icon: "fas fa-info-circle"
      bootstrap_colour: "info"
    secondary_dark_light:
      description: "Supportive context, devices, backgrounds, secondary actions"
      fa_icon: "fas fa-layer-group"
      bootstrap_colour: "secondary"

  rationale:
    bootstrap_choice:
      - "Bootstrap’s components and colour utilities satisfy WCAG 2.1 AA out-of-the-box, eliminating costly retrofits."
      - "Eight semantic colour tokens map cleanly to clinical meaning, letting clinicians read state at a glance."
      - "Built-in focus rings, ARIA labels and the `color-contrast()` helper let developers concentrate on clinical logic."

    iec62366_alignment:
      - number: "5.1"
        name: "Use Specification"
        fa_icon: "fas fa-user-tag"
        bootstrap_colour: "primary"
        response: >
          Rapid Bootstrap prototypes accelerate contextual-inquiry sessions with
          representative clinicians, helping us document intended users, environments
          and operating principles early.

      - number: "5.2"
        name: "Identify UI characteristics & potential use errors"
        fa_icon: "fas fa-search-minus"
        bootstrap_colour: "primary"
        response: >
          Semantic colours and predictable components make it easier to spot steps
          where a user could mis-select or overlook critical information.

      - number: "5.3"
        name: "Identify hazards & hazardous situations"
        fa_icon: "fas fa-radiation-alt"
        bootstrap_colour: "primary"
        response: >
          Colour-coded risk levels and clear affordances help map which hazards tie
          to each UI element during ISO 14971 analysis.

      - number: "5.4"
        name: "Describe hazard-related use scenarios"
        fa_icon: "fas fa-scroll"
        bootstrap_colour: "primary"
        response: >
          Low-code prototypes enable walk-throughs that surface realistic,
          hazard-related scenarios before code solidifies.

      - number: "5.5"
        name: "Select scenarios for summative evaluation"
        fa_icon: "fas fa-list-check"
        bootstrap_colour: "primary"
        response: >
          Distinctive danger and warning styling highlights which scenarios demand
          summative validation, simplifying selection rationale.

      - number: "5.6"
        name: "User-interface specification"
        fa_icon: "fas fa-file-code"
        bootstrap_colour: "primary"
        response: >
          A single Sass map of theme colours and utility classes becomes a
          traceable, auditable UI specification.

      - number: "5.7"
        name: "User-interface evaluation plan"
        fa_icon: "fas fa-clipboard-list"
        bootstrap_colour: "primary"
        response: >
          Bootstrap-based layouts ensure consistent, reproducible test setups across
          devices when drafting the evaluation plan.

      - number: "5.8"
        name: "Formative evaluation (design & implementation)"
        fa_icon: "fas fa-pen"
        bootstrap_colour: "primary"
        response: >
          Variable overrides let designers tweak contrast overnight once formative
          sessions expose readability issues.

      - number: "5.9"
        name: "Summative (validation) evaluation"
        fa_icon: "fas fa-vial"
        bootstrap_colour: "primary"
        response: >
          Built-in keyboard, focus and ARIA compliance mean summative testing can
          focus on workflow safety, not basic accessibility defects.

      - number: "5.10"
        name: "User Interface of Unknown Provenance (UOUP)"
        fa_icon: "fas fa-recycle"
        bootstrap_colour: "primary"
        response: >
          When reusing legacy Bootstrap components we document them under Annex C as
          UOUP and run targeted gap testing to confirm safety.


  usability_benefits:
    - fa_icon: "fas fa-smile-beam"
      bootstrap_colour: "success"
      text: >
        Consistent, familiar UI reduces training time and cognitive load, addressing
        the proven link between poor EHR usability and clinician burnout.
    - fa_icon: "fas fa-tablet-alt"
      bootstrap_colour: "primary"
      text: >
        Responsive grid keeps layouts orderly from mobile crash-trolley tablets to
        27-inch radiology monitors.

  clinician_wellbeing:
    fa_icon: "fas fa-heartbeat"
    bootstrap_colour: "success"
    evidence: >
      A 2024 JAMA Network Open survey of 2 067 family physicians showed that higher
      EHR usability scores correlated with an 18.8 % drop in reported burnout.
    takeaway: >
      By adopting Bootstrap’s clear visual hierarchy and predictable interactions,
      Darwinist helps clinicians spend less effort deciphering software and more
      time on patient care.

  cost_of_getting_usability_wrong:
    fa_icon: "fas fa-skull-crossbones"
    bootstrap_colour: "danger"
    headline: "Poor UI can harm patients, staff and the bottom line."
    consequences:
      - "Patient harm: dose mis-entry, delay in recognising deteriorating vitals."
      - "Regulatory risk: non-conformance with IEC 62366-1 / ISO 14971 triggers findings."
      - "Staff burnout: frustration fuels turnover and locum costs."
      - "Litigation & reputation damage: high-profile errors erode public trust."
    case_study:
      name: "UCSF Septra 38× overdose (2013)"
      fa_icon: "fas fa-pills"
      bootstrap_colour: "danger"
      summary: >
        Look-alike alerts and ambiguous units let a resident order 6 160 mg instead of
        160 mg; clear units, distinctive danger colours and tiered alerts—the very
        guardrails Bootstrap helps implement—would have prevented the error.

  balancing_form_and_function:
    - fa_icon: "fas fa-bolt"
      bootstrap_colour: "info"
      text: "Core CSS < 20 kB gzipped keeps pages snappy on patchy hospital Wi-Fi."
    - fa_icon: "fas fa-shield-alt"
      bootstrap_colour: "secondary"
      text: "Open-source ecosystem delivers continuous security and accessibility patches."
    - fa_icon: "fas fa-paint-brush"
      bootstrap_colour: "primary"
      text: "NHS branding achieved by overriding a handful of Sass variables—no template rewrites."
    - fa_icon: "fas fa-eye"
      bootstrap_colour: "light"
      text: "Modern, restrained visual style avoids clutter while preserving high contrast."

  bottom_line_for_clients:
    fa_icon: "fas fa-handshake"
    bootstrap_colour: "success"
    text: >
      By combining Bootstrap’s WCAG-ready toolkit with the IEC 62366-1 usability-engineering
      process, Darwinist delivers clinical software that is safe, accessible,
      maintainable and clinician-friendly—helping doctors focus on patients, not on
      fighting the UI.
---