---
layout: document
title: "Document Format Guide for AI Content Generation"
subtitle: "Template and Guidelines for Creating Healthcare Technology Documentation"
date: 2025-06-01
author: "Darwinist Team"
tags: ["Documentation", "Template", "AI Guidelines", "Healthcare Technology"]
category: "Documentation Guidelines"
featured: false
hidden: true
toc: true
excerpt: "Comprehensive guide for AI systems on how to format healthcare technology documents using Jekyll markdown, including YAML front matter, heading structure, content organization, and style conventions used in the Darwinist documentation collection."
---

# Document Format Guide for AI Content Generation

## YAML Front Matter Structure

Every document must begin with YAML front matter enclosed in triple dashes (`---`). This metadata controls how Jekyll processes and displays the document:

```yaml
---
layout: document                    # Always use "document" layout
title: "Primary Document Title"     # Clear, descriptive title
subtitle: "Explanatory subtitle"    # Additional context (optional)
date: 2025-06-01                   # Publication date (YYYY-MM-DD format)
author: "Darwinist Team"           # Always "Darwinist Team"
tags: ["Tag1", "Tag2", "Tag3"]     # Relevant keywords as array
category: "Category Name"          # Groups related documents
featured: true                     # Boolean: highlights important docs
toc: true                         # Boolean: enables table of contents
hidden: false                     # Boolean: hides from document listing
excerpt: "Brief summary..."       # 1-2 sentence document description
---
```

### YAML Field Guidelines:

- **title**: Use title case, be specific and descriptive
- **subtitle**: Explain the document's purpose or scope
- **tags**: Include 3-7 relevant keywords (healthcare tech, product names, standards)
- **category**: Use consistent categories like "Healthcare Technology", "Medical AI Solutions", "Healthcare Infrastructure"
- **excerpt**: Write a compelling 1-2 sentence summary highlighting key benefits, metrics, or unique value

## Markdown Heading Structure

Use ATX-style headings with proper hierarchy:

```markdown
# Main Title (H1) - Use sparingly, mainly for document title
## Major Section (H2) - Primary content divisions
### Subsection (H3) - Secondary topics
#### Details (H4) - Specific points
##### Minor Points (H5) - Rarely used
###### Smallest (H6) - Avoid if possible
```

### Heading Best Practices:
- Start with H2 for main content sections (H1 reserved for document title)
- Maintain logical hierarchy (don't skip levels)
- Use descriptive, scannable headings
- Include keywords relevant to healthcare/technology context

## Content Formatting

### Emphasis and Strong Text
```markdown
*Italics for emphasis*
**Bold for strong importance**
***Bold and italic for critical points***
```

### Lists
```markdown
# Unordered lists for features, benefits, capabilities
* Primary point
* Secondary point
  * Nested sub-point
  * Another sub-point

# Ordered lists for processes, steps, phases
1. First step
2. Second step
3. Third step
```

### Code and Technical Elements
```markdown
`Inline code` for technical terms, file names, commands

```
Code blocks for longer technical content, configurations, or examples
```

### Links
```markdown
[External link text](https://example.com)
[This AI Spec Document]({% link _docs/AI spec.md %})
```

### Tables
```markdown
| Feature | Benefit | Use Case |
|---------|---------|----------|
| Row 1 data | Row 1 data | Row 1 data |
| Row 2 data | Row 2 data | Row 2 data |
```

### Blockquotes
```markdown
> Use for important quotes, key statistics, or highlighted information
```

## Document Structure Pattern

Most healthcare technology documents follow this structure:

```markdown
# Executive Summary or Overview
Brief introduction explaining what the technology/solution does and its primary value proposition.

## Key Features/Capabilities
Detailed breakdown of main functionalities, often using:
- Bullet points for feature lists
- Numbered lists for processes
- Tables for comparisons

## Technical Specifications
- System requirements
- Integration capabilities
- Standards compliance
- Architecture details

## Use Cases/Applications
Real-world scenarios where the solution provides value, often organized by:
- Healthcare setting (NHS Trusts, private practices, etc.)
- Clinical specialty (radiology, cardiology, etc.)
- Workflow type (diagnostic, therapeutic, administrative)

## Benefits/Outcomes
Quantified results, metrics, and qualitative improvements:
- Clinical outcomes
- Operational efficiency
- Cost savings
- User satisfaction

## Implementation/Deployment
- Setup requirements
- Integration process
- Training needs
- Support available

## Compliance/Security
- Regulatory certifications
- Data protection measures
- Healthcare standards compliance
- Audit capabilities

## Conclusion
Summary of key value propositions and call to action
```

## Writing Style Guidelines

### Tone and Voice
- **Professional but accessible**: Avoid overly technical jargon without explanation
- **Confident and authoritative**: Present information as factual and well-researched
- **Solution-focused**: Emphasize benefits and outcomes for healthcare organizations
- **UK healthcare context**: Reference NHS, NICE, CQC, and UK regulations where relevant

### Technical Writing Best Practices
- Define acronyms on first use: "Electronic Health Record (EHR)"
- Use active voice when possible
- Include specific metrics and quantified benefits
- Provide context for technical capabilities (why they matter clinically)
- Use consistent terminology throughout

### Healthcare-Specific Considerations
- Reference relevant UK healthcare standards (HL7 FHIR, DICOM, etc.)
- Include regulatory compliance information (CE marking, MHRA approval, etc.)
- Mention integration with common NHS systems
- Address clinical workflow implications
- Consider different user types (clinicians, IT staff, administrators)

## Special Formatting Elements

### Callout Boxes (using blockquotes with formatting)
```markdown
> **Key Benefit**: This solution reduces diagnostic time by 70% while improving accuracy.
```

### Feature Lists with Icons
```markdown
✅ **FHIR Compliant**: Native support for healthcare interoperability standards
❌ **Legacy Compatible**: Works with existing PACS and HIS systems
🔒 **Secure**: End-to-end encryption and GDPR compliance
```

### Comparison Tables
```markdown
| Capability | Our Solution | Traditional Approach |
|------------|--------------|---------------------|
| Setup Time | Minutes | Weeks |
| Standards | FHIR/DICOM | Proprietary |
| Access | Cloud/On-Premise | On-Premise Only |
```

## Common Document Categories

- **"Healthcare Technology"**: General health IT solutions
- **"Medical AI Solutions"**: AI-powered diagnostic and clinical tools
- **"Healthcare Infrastructure"**: Core systems like PACS, imaging networks
- **"Healthcare Standards"**: Documentation about FHIR, DICOM, HL7
- **"Healthcare Policy"**: Analysis of regulations, procurement, strategy
- **"Medical Imaging Solutions"**: Radiology and imaging-specific tools
- **"Healthcare Education"**: Training and certification frameworks

## SEO and Discoverability

- Include relevant keywords naturally in headings and content
- Use descriptive link text
- Structure content for scanning (headings, lists, tables)
- Include quantified benefits and outcomes
- Reference popular healthcare technology terms and standards

## File Naming Convention

Files should use descriptive names with spaces and proper capitalization:
- `Product Name Technical Brief.md`
- `Healthcare Standard Implementation Guide.md`
- `Clinical AI Solution Overview.md`

This format ensures consistency, readability, and proper Jekyll processing while serving the needs of healthcare technology professionals seeking detailed, actionable information.