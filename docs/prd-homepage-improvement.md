---
permalink: false
eleventyExcludeFromCollections: true
---

# PRD: Homepage Content and UI/UX Improvement

## Document Status

- Status: Draft
- Owner: Product / Design / Frontend
- Target surface: Homepage only
- Pages in scope: `/en/`, `/uz/`
- Redirect note: `/` must continue redirecting to `/en/`

## Assumption

This PRD assumes "this page" refers to the bilingual homepage experience rendered through [`_includes/landing.njk`](/Users/yakhyo/Workspace/python-lessons/_includes/landing.njk) and wrapped by [`_layouts/base.njk`](/Users/yakhyo/Workspace/python-lessons/_layouts/base.njk). If the intended target is a different page, this PRD should be adapted before implementation.

## Summary

The current homepage is functional but structurally thin. It exposes tutorial lists and DSA links, yet it does not explain the product clearly in the first viewport, does not guide different learner types effectively, and leaves important content, trust, and SEO value in metadata rather than on-page content.

The goal is to redesign the homepage so new visitors can immediately understand:

1. What the site offers.
2. Who it is for.
3. Where to start.
4. What to do next.

The implementation must be non-breaking: no URL changes, no collection changes, no disruption to localization, and no regressions to existing tutorial/tool access.

## Background

The site is an Eleventy + Tailwind content platform for Python learning in English and Uzbek. The homepage is the primary entry point for discovery but currently behaves more like a content index than a guided landing experience.

Current homepage characteristics:

- Navigation includes Tutorial, DSA, Online IDE, language switch, and GitHub CTA.
- Main body begins with a tutorial content list, level tabs, and long lesson lists.
- DSA content appears as a second section with two dense cards.
- Footer is comprehensive and functional.
- Root `/` redirects to `/en/`.

## Current-State Findings

### Content

- There is no visible homepage `h1`; the page starts at `h2`, which weakens accessibility and SEO.
- The strongest value proposition exists in metadata, not in the page body.
- The page does not explain learner outcomes, estimated effort, or recommended starting points.
- Level descriptions are generic and do not help users self-select quickly.
- Tutorial titles are useful as an index, but the page relies too heavily on raw lists without summary, context, or prioritization.
- The site claims credibility in meta description ("Trusted by 100+ campuses & companies since 2015") but that proof is not visible on-page.

### UI/UX

- The first viewport lacks a clear hero, primary CTA, or structured path selection.
- The initial experience is list-heavy and scanning-intensive.
- DSA content competes with the main Python tutorial path instead of being clearly secondary or optional.
- There is no "start here" path for beginners, returning users, or DSA-focused learners.
- The page offers little progressive disclosure; users see long lists before they understand the structure.

### Accessibility

- No visible `h1` on the homepage.
- The level switcher is implemented as buttons with JavaScript display toggling, but it does not appear to use full tab semantics (`tablist`, `tab`, `tabpanel`, `aria-selected`, keyboard behavior).
- Important content depends on client-side enhancement to filter correctly.
- Dense list presentation increases cognitive load, especially on mobile.

### SEO / Information Architecture

- Title tag is serviceable but repetitive: "Python Programming Tutorial | Python Tutorial".
- On-page content does not fully support the keywords and intent implied in metadata.
- Homepage schema is present, but the on-page structure does not strongly reinforce course discovery or entry-point selection.

### Data / Quality

- English and Uzbek tutorial inventories are symmetrical: 21 basic, 11 intermediate, 12 advanced.
- Data structures list shows an ordering inconsistency in the rendered output (`06` appears twice), which reduces perceived polish.

## Problem Statement

New users land on the homepage and see a content index before they see a clear promise, path, or recommended next action. This slows comprehension, weakens conversion into learning starts, and makes the product feel less deliberate than the underlying content quality warrants.

## Goals

1. Clarify the homepage value proposition within the first viewport.
2. Help first-time users choose a learning path in under 5 seconds.
3. Increase clicks into the correct first lesson, DSA roadmap, or Online IDE.
4. Improve homepage accessibility, SEO, and perceived quality.
5. Preserve all existing routes, content collections, and localization behavior.

## Non-Goals

1. Rewriting all tutorial content in this phase.
2. Redesigning tutorial detail pages, tool pages, or DSA detail pages.
3. Changing existing URLs, slugs, or collection shapes.
4. Adding accounts, progress tracking, or a forum backend.
5. Replatforming away from Eleventy or Tailwind.

## Primary Users

### Beginner Learner

Needs a clear starting point, reassurance that the content is free and structured, and low-friction entry into lesson 1.

### Returning Learner

Needs quick access to the next level, topic, or tool without re-reading the entire page.

### DSA-Oriented Learner

Needs a clear path into data structures and algorithms without confusing that track with the core beginner Python track.

## User Stories

1. As a beginner, I want to know where to start immediately so I can begin learning without comparing dozens of links.
2. As an intermediate learner, I want to jump to the right level quickly so I do not have to scan beginner content.
3. As a DSA learner, I want to understand whether DSA is part of the Python curriculum or a separate track.
4. As a bilingual user, I want the English and Uzbek homepages to feel equivalent in structure and intent.
5. As a mobile user, I want the homepage to feel manageable and readable without long scrolling through dense lists.

## Success Metrics

Primary metrics:

1. Increase homepage click-through rate to the first tutorial lesson.
2. Increase click-through rate to level-specific entry points.
3. Increase click-through rate to DSA roadmap and Online IDE from relevant sections.

Secondary metrics:

1. Reduce bounce rate from homepage sessions.
2. Improve average time to first outbound educational click.
3. Improve accessibility audit scores for heading structure, focus, and semantic controls.

## Experience Principles

1. Explain before listing.
2. Guide before overwhelming.
3. Keep the primary path obvious.
4. Make every section answer "why should I click this?"
5. Default to server-rendered clarity; use JavaScript only for enhancement.
6. Preserve familiarity while increasing polish.

## Proposed Information Architecture

### 1. Hero Section

Purpose: Establish the value proposition and primary next actions.

Requirements:

- Add a visible homepage `h1`.
- Add a concise subheading describing free, structured Python learning in English and Uzbek.
- Add a primary CTA: start the core tutorial path.
- Add a secondary CTA: explore DSA or open the Online IDE.
- Add lightweight trust or scale indicators only if they can be substantiated.

Recommended content:

- H1: outcome-focused and beginner-friendly.
- Supporting copy: structured curriculum, free access, bilingual support, practical progression.
- Utility points: number of lessons, levels, DSA track, browser IDE.

### 2. Path Selection Section

Purpose: Help users self-select instead of reading a long list first.

Requirements:

- Replace or reframe the current tab-first experience with level cards or a semantically correct tab/accordion pattern.
- Each path must include:
  - audience
  - prerequisites
  - lesson count
  - sample topics
  - direct CTA
- Keep "Basic", "Intermediate", and "Advanced" or rename consistently across both languages, but do not mix naming patterns.

Preferred approach:

- Three path cards above the full lesson list.
- Each card expands into a curated preview.
- Full list remains available below for index-style browsing.

### 3. Start-Here / Recommended Next Step Block

Purpose: reduce decision friction.

Requirements:

- Add a compact guided starter flow for first-time users.
- Include a "Start here" recommendation for beginners.
- Include a "Skip to intermediate" route for users with prior experience.
- Include a "Practice in browser" route to the IDE.

### 4. Curriculum Overview Section

Purpose: keep the strong content inventory, but make it easier to scan.

Requirements:

- Preserve current lesson links and ordering.
- Introduce clearer grouping and spacing.
- Show counts per level.
- Consider previewing the first 5-7 lessons with a "View all lessons in this level" expansion pattern if needed.
- Standardize visible labels for readability and consistency.

### 5. DSA Section

Purpose: preserve discoverability without competing with the main tutorial funnel.

Requirements:

- Position DSA as a parallel or next-step learning track, not the default starting point for beginners.
- Add a short explanation of who the DSA content is for.
- Keep roadmap links intact.
- Fix ordering and display inconsistencies so the track feels curated.

### 6. Bilingual Support Section or Inline Proof

Purpose: make the bilingual value explicit.

Requirements:

- Surface language support in visible content, not only in the navbar switcher.
- Clarify that the site supports English and Uzbek learning paths.

### 7. Footer / Contribution Framing

Purpose: retain community and open-source value without distracting from the learning journey.

Requirements:

- Keep GitHub and contribution links.
- Reduce the likelihood that GitHub is interpreted as the primary CTA for learners.

## Content Requirements

### Messaging

- Replace generic instructional copy with outcome-based copy.
- Avoid vague adjectives like "complete" unless backed by specifics.
- Explain what users will be able to do after each path.
- Keep copy concise, plain-language, and action-oriented.

### Trust

- Any claim such as "Trusted by 100+ campuses & companies since 2015" must either:
  - be supported with evidence and shown on-page appropriately, or
  - be removed/reworded until it can be validated.

### Localization

- English and Uzbek versions must remain structurally parallel.
- Copy should be localized intentionally, not mechanically translated.
- Shared content structures should come from data-driven templates where possible to avoid divergence.

## UX Requirements

1. The first screen must answer:
   - what this site is
   - who it is for
   - where to start
2. The default next step for beginners must be obvious.
3. The page must remain easy to scan on mobile.
4. Dense link lists must be visually grouped and chunked.
5. Major actions must appear above the fold on common laptop and mobile widths.
6. Visual hierarchy must separate primary learning actions from secondary project/community actions.

## Accessibility Requirements

1. Add exactly one visible `h1` per homepage.
2. Use semantic section headings in descending order.
3. If tabs are used, implement full accessible tab semantics and keyboard behavior.
4. If tabs are not necessary, prefer simpler progressive disclosure such as cards plus anchored sections.
5. Ensure visible focus states for all links and buttons.
6. Meet WCAG AA contrast for text and interactive elements.
7. Ensure touch targets are at least 44x44 CSS pixels.
8. Avoid conveying state by color alone.
9. Preserve usability with JavaScript disabled where feasible; core links must remain visible and functional.

## SEO Requirements

1. Improve homepage title tag to remove redundancy and better match user intent.
2. Ensure on-page copy supports major search intents:
   - learn python
   - python tutorial
   - python for beginners
   - python lessons
3. Add a visible introductory paragraph aligned with metadata.
4. Preserve canonical URLs and current locale behavior.
5. Keep structured data valid; expand only if it maps to real on-page content.

## Technical Requirements

1. Do not change:
   - tutorial permalinks
   - DSA permalinks
   - root redirect behavior
   - English/Uzbek path conventions
2. Keep the homepage implementation compatible with existing Eleventy collection logic.
3. Prefer additive refactoring:
   - extract reusable content config
   - keep markup modular
   - avoid mixing large inline strings with complex interactive logic
4. JavaScript should enhance, not gate, the core experience.
5. New UI should not require heavyweight client frameworks.
6. Preserve current navbar, footer, and tool links unless a specific improvement is justified in implementation review.

## Recommended Implementation Approach

### Phase 1: Content and Structure

- Add hero section with `h1`, subhead, and primary CTAs.
- Add path-selection cards or improved level navigation.
- Reframe DSA as a secondary track.
- Add visible bilingual and trust messaging where valid.

### Phase 2: Semantics and Interaction

- Replace ad hoc tab behavior with accessible interaction patterns.
- Improve mobile spacing, chunking, and focus treatment.
- Keep content usable without JavaScript.

### Phase 3: Polish and Measurement

- Refine copy, spacing, iconography, and micro-interactions.
- Add analytics events if GA is enabled.
- Validate SEO, accessibility, and content parity.

## Acceptance Criteria

1. Homepage has a visible `h1` in both English and Uzbek.
2. First viewport contains a clear value proposition and at least one primary learning CTA.
3. Users can identify beginner, intermediate, advanced, and DSA paths without reading long lists first.
4. All current tutorial and roadmap links continue to work unchanged.
5. Homepage remains functional and understandable even if homepage enhancement JavaScript fails.
6. Keyboard navigation is complete and predictable.
7. Lighthouse/accessibility checks show no regressions on homepage-critical semantics.
8. Content claims visible on-page are accurate and reviewable.
9. English and Uzbek homepages ship with matching structure and equivalent intent.

## Validation Checklist

- Run `npm run build`
- Run `npm run check`
- Manually verify:
  - `/`
  - `/en/`
  - `/uz/`
  - mobile navbar behavior
  - language switch behavior
  - CTA links
  - DSA links
  - no-JS fallback behavior for homepage navigation

## Risks

1. Over-designing the homepage could hide the site's strongest asset: direct access to lessons.
2. Copy changes may create English/Uzbek parity drift if not centralized.
3. Adding interaction without semantic rigor could worsen accessibility.
4. Unverified trust claims could create credibility risk if made more prominent.
5. Excessive visual complexity could conflict with the site's current lightweight performance profile.

## Open Questions

1. Should the primary CTA go to lesson 1, the tutorial index, or a new curated "start here" anchor on the homepage?
2. Is the trust claim about campuses/companies validated and ready for on-page use?
3. Should DSA remain on the homepage, or should it be visually reduced and positioned as a next-step track?
4. Does the team want a simple homepage search/jump feature, or is guided navigation enough for this phase?
5. Should visible lesson labels be normalized for readability on the homepage even if source page titles stay unchanged?

## Suggested Deliverables

1. Updated homepage wireframe for desktop and mobile.
2. Finalized bilingual homepage copy.
3. Implementation ticket set:
   - content strategy
   - homepage template refactor
   - accessibility pass
   - analytics hooks
   - QA and regression verification
