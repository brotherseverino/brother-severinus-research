# Visual Mockups Gallery: Epistemic Glyphs in Action

**Date:** April 24, 2026  
**Version:** 1.0  
**Purpose:** Concrete visual examples of glyphs integrated with AI systems

---

## Table of Contents

1. [ChatGPT Thinking Mode](#chatgpt-thinking-mode)
2. [Healthcare Clinical Decision Support](#healthcare-clinical-decision-support)
3. [Research Paper Analysis](#research-paper-analysis)
4. [Code Generation with Verification](#code-generation-with-verification)
5. [Multi-Source News Synthesis](#multi-source-news-synthesis)

---

## ChatGPT Thinking Mode

### Use Case: Calendar Query with Mixed Epistemic Status

**User query:** "What's my schedule tomorrow and when should I leave for the 2pm meeting?"

**AI Response (with glyphs):**

```
[Thinking Mode]

🔷◐⊕ Accessing user calendar for 2026-04-25...
🔷✓⊕ Retrieved 3 confirmed meetings:
     - 09:00 AM: Team standup (Conference Room A)
     - 02:00 PM: Client presentation (Downtown Office)
     - 05:00 PM: Project review (Remote)

⬡▶⊙ Calculating travel time to downtown office...
⬡✓⊙ Estimated commute: 35-45 minutes (based on historical traffic)
⬡→⊙ Current traffic conditions: Unknown (API unavailable)
○⊚ Weather forecast suggests no delays (speculative)

🔷⤴⊕ Recommendation: Leave by 1:15 PM
         (Allows 45min travel + 15min buffer)

[Final Answer]

Your schedule for April 25:

🔷⊕ 09:00 AM - Team standup (Conference Room A)
🔷⊕ 02:00 PM - Client presentation (Downtown Office)  
🔷⊕ 05:00 PM - Project review (Remote)

⬡⊙ Recommended departure for 2pm meeting: 1:15 PM
    (35-45min commute + 15min buffer based on historical traffic)

○⊚ Note: Real-time traffic check unavailable - allow extra time if rush hour
```

**Visual scan result:**
- User immediately sees **3 solid diamonds** (verified meetings)
- Sees **hexagons** (inferred travel time) - not as certain
- Sees **hollow circle** (speculative weather note) - lowest confidence

**Click-through example (2pm meeting):**

```
User clicks: 🔷⊕

┌─────────────────────────────────────────────────────┐
│ Verification Details                                │
├─────────────────────────────────────────────────────┤
│ Meeting: Client presentation                        │
│ Time: 2026-04-25 14:00-15:30                        │
│ Location: Downtown Office                           │
│                                                     │
│ Source: Google Calendar API                         │
│ Query timestamp: 2026-04-24 19:30:15 UTC            │
│ Event ID: cal_evt_2Hx9kP                            │
│                                                     │
│ Status: Confirmed                                   │
│ Attendees: 4 (all accepted)                         │
│ Organizer: john@company.com                         │
│                                                     │
│ Confidence: 100% (direct calendar query)            │
│                                                     │
│ [View in Google Calendar]                           │
│ [Refresh verification]                              │
└─────────────────────────────────────────────────────┘
```

---

## Healthcare Clinical Decision Support

### Use Case: Emergency Department Triage

**Patient:** 62yo female, chest pain, SOB (shortness of breath)

**AI-Assisted Triage (with glyphs):**

```
EMERGENCY TRIAGE ASSESSMENT

Patient vitals (last 5 minutes):
🔷⊕ BP: 165/95 mmHg (elevated)
🔷⊕ HR: 110 bpm (tachycardia)
🔷⊕ SpO2: 92% on room air (low)
🔷⊕ Temp: 37.2°C (normal)

CRITICAL FINDINGS ⚡
╔════════════════════════════════════════════════════╗
║ 🔷🔄⊕⚡ ACUTE CORONARY SYNDROME (ACS) suspected    ║
║                                                    ║
║ Evidence:                                          ║
║ 🔷⊕ ECG: ST elevation in leads II, III, aVF        ║
║ 🔷⊕ Troponin-I: 4.8 ng/mL (critical: >0.04)       ║
║ 🔷⊕ Risk factors: Age, HTN, chest pain            ║
║                                                    ║
║ ACTION REQUIRED: Activate cath lab immediately     ║
║ Protocol: STEMI (ST-elevation MI) pathway          ║
║ Time-sensitive: Door-to-balloon <90 minutes        ║
╚════════════════════════════════════════════════════╝

Differential diagnosis (other possibilities):

🔷⤴⊕ Pulmonary Embolism
      Evidence:
      - D-dimer elevated (2.1 mg/L FEU, normal <0.5)
      - Tachycardia + hypoxia pattern
      - Wells score: 6 (high probability)
      Recommendation: CT-PE scan if ACS ruled out

⬡⊙ Pneumonia
   Evidence:
   - No fever currently
   - CXR: Pending interpretation
   - Possible but less likely
   Status: Monitor, await CXR results

○⊚ Anxiety/Panic attack
   Very unlikely given vital signs & troponin
   Consider only if all cardiac/pulmonary workup negative
```

**Physician workflow:**
1. **Sees ⚡ immediately** → critical finding
2. **Reads boxed section** → ACS protocol
3. **Clicks 🔷🔄⊕⚡** → verifies against guidelines

**Click-through (ACS finding):**

```
┌────────────────────────────────────────────────────────┐
│ TIER 4: CLINICAL EVIDENCE (CRITICAL)                   │
├────────────────────────────────────────────────────────┤
│ Finding: Acute Coronary Syndrome (STEMI)               │
│ Confidence: 95% (diagnostic criteria met)              │
│                                                        │
│ Verification process:                                  │
│ ✓ ECG reviewed by cardiology (Dr. Patel, 19:32)       │
│ ✓ Troponin trend: Rising (4.2→4.8 in 30min)           │
│ ✓ Clinical presentation matches ACC/AHA criteria       │
│ ✓ Cath lab notified & activated (19:35)               │
│                                                        │
│ Guidelines matched:                                    │
│ - ACC/AHA STEMI Guidelines (2023)                      │
│ - ESC Acute Coronary Syndromes (2025)                 │
│ - Hospital STEMI Protocol v4.2                         │
│                                                        │
│ Time-critical actions:                                 │
│ [✓] Aspirin 325mg given (19:28)                       │
│ [✓] Clopidogrel 600mg given (19:29)                   │
│ [✓] Heparin bolus given (19:31)                       │
│ [✓] Cath lab activated (19:35)                        │
│ [⏳] Door-to-balloon timer: 12 minutes elapsed         │
│                                                        │
│ Audit trail: 4 verification steps completed           │
│ Last updated: 2026-04-24 19:36:22 UTC                 │
│                                                        │
│ [View full ECG]                                        │
│ [View troponin trend graph]                            │
│ [View guideline references]                            │
│ [Download audit trail PDF]                             │
└────────────────────────────────────────────────────────┘
```

**Outcome:**
- Physician makes rapid, informed decision
- All verification steps documented
- Time-critical protocol executed correctly
- Full audit trail for legal/quality review

---

## Research Paper Analysis

### Use Case: Literature Review for Grant Proposal

**User query:** "Summarize recent findings on CRISPR gene editing safety concerns"

**AI Response (with glyphs):**

```
LITERATURE SYNTHESIS: CRISPR Safety Concerns

Recent peer-reviewed findings (2024-2026):

🔷⊕ Off-target effects reduced but not eliminated
    Source: Zhang et al., Nature 2025, Vol 618, p.123-130
    Finding: New base editors show 0.02% off-target rate
    (down from 2-5% in 2020 systems)
    N=450 edits across 12 cell lines
    [VERIFIED: Direct access to Nature publication]

🔷⊕ Chromosomal rearrangements remain concern
    Source: Kim et al., Science 2024, Vol 382, p.891-897
    Finding: 3-8% of edits resulted in large deletions
    (>1kb) in embryonic stem cells
    Clinical relevance: Unknown for adult somatic cells
    [VERIFIED: Direct access to Science publication]

⬡⤴⊕ Immune response variability emerging as issue
     Source: Meta-analysis, Chen et al., Cell 2026
     Synthesis: 15 studies, N=2,340 patients
     Finding: 12-18% develop anti-Cas9 antibodies
     Effect on re-dosing: Reduced efficacy
     [VERIFIED: Meta-analysis methodology sound]

⬡⊙ Long-term follow-up data still limited
   Source: Review article, Doudna & Charpentier, NEJM 2025
   Assessment: Most trials <5 years follow-up
   Recommendation: 10-15 year studies needed
   [INFERRED: Expert opinion, not primary data]

○⊚ Germline editing regulatory consensus unclear
   Current status: Varies by jurisdiction
   International summit (2025): No consensus reached
   [SPECULATED: Based on news reports, not official statement]
```

**Click-through example (Zhang et al. finding):**

```
┌───────────────────────────────────────────────────────┐
│ Source Verification                                   │
├───────────────────────────────────────────────────────┤
│ Citation: Zhang et al., Nature 2025                   │
│ Title: "Improved base editors with minimal off-target"│
│ DOI: 10.1038/s41586-025-07234-x                       │
│ Pub date: 2025-03-15                                  │
│                                                       │
│ Verification method:                                  │
│ ✓ Direct API access to Nature                        │
│ ✓ Full text retrieved & parsed                       │
│ ✓ Key finding extracted from results section         │
│ ✓ Sample size (N=450) confirmed in methods           │
│ ✓ Cross-referenced with supplementary data           │
│                                                       │
│ Credibility indicators:                               │
│ - Journal: Nature (IF: 64.8, Q1)                     │
│ - Citations: 142 (as of 2026-04-24)                  │
│ - Peer review: Yes (3 reviewers)                     │
│ - Data availability: Yes (GEO: GSE198234)            │
│                                                       │
│ Confidence in extraction: 98%                         │
│ (Direct quote match confirmed)                        │
│                                                       │
│ [View full paper on Nature.com]                       │
│ [View citation context]                               │
│ [Download BibTeX]                                     │
└───────────────────────────────────────────────────────┘
```

**User benefit:**
- Immediately distinguishes **peer-reviewed data** (🔷) from **expert opinion** (⬡) from **speculation** (○)
- Can click through to verify sources for grant proposal citations
- Epistemic transparency supports rigorous scholarship

---

## Code Generation with Verification

### Use Case: Security-Critical Function

**User query:** "Generate a function to validate user passwords securely"

**AI Response (with glyphs):**

```
PASSWORD VALIDATION FUNCTION

🔷⊕ Security best practices applied:
    - OWASP Password Guidelines (2024)
    - NIST SP 800-63B requirements
    - Industry standard bcrypt hashing

⬡⊙ Implementation notes:
    - Assumes bcrypt library available
    - Cost factor: 12 (recommended for 2026)
    - No custom crypto (uses vetted library)

```python
import bcrypt
import re

def validate_password(password: str) -> tuple[bool, str]:
    """
    🔷⊕ Validate password strength per OWASP 2024 guidelines
    
    Returns:
        (is_valid, message)
    """
    
    # 🔷⊕ Length check (NIST minimum: 8 chars)
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    # 🔷⊕ Maximum length (prevent DoS via bcrypt)
    if len(password) > 64:
        return False, "Password too long (max 64 characters)"
    
    # ⬡⊙ Complexity check (recommended but not required by NIST)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    
    complexity_score = sum([has_upper, has_lower, has_digit])
    if complexity_score < 2:
        return False, "Password should contain uppercase, lowercase, and digits"
    
    return True, "Password meets security requirements"

def hash_password(password: str) -> str:
    """
    🔷⊕ Hash password using bcrypt with cost factor 12
    
    Security note: Cost factor 12 = ~250ms on modern hardware
    (Recommended by OWASP as of 2024)
    """
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """
    🔷⊕ Verify password against bcrypt hash (constant-time)
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
```

⚠️ SECURITY NOTES:

🔷⊕ Verified against OWASP guidelines:
    - Minimum 8 characters (NIST requirement)
    - Maximum 64 characters (bcrypt limitation)
    - Uses bcrypt (industry standard, not MD5/SHA1)
    - Constant-time comparison (prevents timing attacks)

⬡⊙ Additional recommendations (not implemented):
    - Password breach check (HaveIBeenPwned API)
    - Rate limiting on login attempts
    - Multi-factor authentication

○⊚ Do NOT use for:
    - Passwords >64 characters (will truncate)
    - High-throughput scenarios (bcrypt is intentionally slow)
    - Legacy system integration (may need MD5/SHA1 for compat)

**Click-through (OWASP verification):**

```
┌────────────────────────────────────────────────────────┐
│ Security Standard Verification                         │
├────────────────────────────────────────────────────────┤
│ Standard: OWASP Password Storage Cheat Sheet           │
│ Version: 2024 (updated 2024-08-15)                     │
│ URL: owasp.org/www-project-cheat-sheets/cheatsheets/...│
│                                                        │
│ Requirements checked:                                  │
│ ✓ Minimum length: 8 characters (implemented)           │
│ ✓ Maximum length: 64 characters (bcrypt limit)         │
│ ✓ Hashing algorithm: bcrypt (recommended)              │
│ ✓ Cost factor: 12 (appropriate for 2026 hardware)     │
│ ✓ No custom crypto (uses vetted library)              │
│ ✓ Constant-time comparison (timing attack resistant)   │
│                                                        │
│ NIST SP 800-63B compliance:                            │
│ ✓ Minimum 8 characters                                 │
│ ✓ No composition rules enforced (NIST discourages)     │
│ ⚠ Complexity check included (optional, not required)   │
│                                                        │
│ Verification timestamp: 2026-04-24 19:45:03 UTC        │
│ Guidelines last updated: 2024-08-15                    │
│                                                        │
│ [View OWASP guidelines]                                │
│ [View NIST SP 800-63B]                                 │
│ [Run security test suite]                              │
└────────────────────────────────────────────────────────┘
```

**Developer benefit:**
- Knows which parts are **verified against standards** (🔷)
- Sees **recommendations** that aren't implemented (⬡)
- Understands **limitations** explicitly (○)
- Can audit security compliance via click-through

---

## Multi-Source News Synthesis

### Use Case: Understanding Complex News Event

**User query:** "What happened with the AI safety summit last week?"

**AI Response (with glyphs):**

```
AI SAFETY SUMMIT (April 17-19, 2026)

🔷⊕ Confirmed facts (multiple primary sources):
    - Location: Singapore
    - Attendees: 42 countries represented
    - Duration: 3 days (April 17-19, 2026)
    - Host: Singapore Ministry of Communications
    
    Sources: Official summit website, Reuters, AP

🔷⤴⊕ Major announcements:
    1. "Singapore Framework" for AI governance
       - 7 participating nations signed (US, UK, EU, Japan, Singapore, Canada, Australia)
       - Focus: Cross-border AI safety standards
       - Implementation timeline: 12-18 months
       
    2. AI Incident Reporting System (AIRS)
       - Voluntary reporting for AI failures/harms
       - Managed by UN-affiliated body
       - Launches Q3 2026 (pilot)
       
    Sources: Official press releases (verified), major news agencies

⬡⊙ Interpretations/Analysis:
    - Framework seen as "modest but meaningful" (MIT Tech Review)
    - Some critics call it "too voluntary" (Nature editorial)
    - Industry largely supportive but cautious (OpenAI, Anthropic statements)
    
    Note: These are expert opinions, not factual claims

⬡▶⊚ Political context (inferred):
    - US-China tensions: China did not sign framework
    - Timing: 6 months before UN AI Summit
    - Possible relationship to upcoming EU AI Act revisions
    
    Caveat: Political analysis, not confirmed by officials

○⊚ Speculation/Future predictions:
    - Some observers predict "enforcement mechanisms" will be added within 2 years
    - Possible expansion to include AI model liability frameworks
    - May influence national legislation in signatory countries
    
    Warning: These are predictions, not commitments

SOURCES BREAKDOWN:

Primary (official):
🔷⊕ Singapore AI Summit official website (accessed 2026-04-24)
🔷⊕ Ministry of Communications press release (April 19, 2026)
🔷⊕ UN statement on AIRS (April 19, 2026)

Secondary (news):
🔷⊕ Reuters: "42 nations gather for AI safety talks" (April 17)
🔷⊕ AP: "Singapore Framework signed by 7 countries" (April 19)
⬡⊙ MIT Tech Review: "A modest step forward" (April 20)
⬡⊙ Nature Editorial: "AI governance needs teeth" (April 22)

Tertiary (analysis):
⬡⊚ Political analyst commentary (The Economist, April 23)
○⊚ Future predictions (AI policy researcher blog, April 24)
```

**Click-through example (Singapore Framework announcement):**

```
┌──────────────────────────────────────────────────────────┐
│ Multi-Source Verification                                │
├──────────────────────────────────────────────────────────┤
│ Claim: "Singapore Framework signed by 7 nations"         │
│ Status: Verified (3 independent primary sources)         │
│                                                          │
│ Source 1: Official press release                         │
│   Publisher: Singapore Ministry of Communications       │
│   Date: 2026-04-19 14:30 UTC                            │
│   URL: mci.gov.sg/press-releases/ai-summit-2026         │
│   Quote: "Seven nations today signed the Singapore..."   │
│   Credibility: Official government source (primary)      │
│                                                          │
│ Source 2: Reuters wire                                   │
│   Byline: Jane Smith, Tech Policy Correspondent          │
│   Date: 2026-04-19 14:45 UTC                            │
│   Fact-check: Independently verified (Reuters standard)  │
│   Corroboration: Matches official announcement           │
│                                                          │
│ Source 3: Associated Press                               │
│   Date: 2026-04-19 15:02 UTC                            │
│   AP style note: "AP confirmed with US State Dept"       │
│   Additional detail: Text of framework released          │
│                                                          │
│ Cross-validation:                                        │
│ ✓ All 3 sources agree on: date, location, signatories   │
│ ✓ No contradictions found                                │
│ ✓ Official document available for public review          │
│                                                          │
│ Confidence: 99% (multiple primary sources confirm)       │
│                                                          │
│ [View official press release]                            │
│ [View Reuters article]                                   │
│ [View AP wire]                                           │
│ [Download framework PDF]                                 │
└──────────────────────────────────────────────────────────┘
```

**User benefit:**
- Clearly separates **facts** from **analysis** from **speculation**
- Can click through to verify sources for each claim
- Understands epistemic status of different parts of story
- Makes informed decisions about what to trust

---

## Summary: Visual Language Benefits

### Speed
- **Pre-attentive processing:** Glyphs recognized in <200ms
- **Faster triage:** Critical findings (⚡) immediately visible
- **Reduced reading:** Scan glyphs → decide whether to read details

### Accuracy
- **Clear differentiation:** Verified vs inferred vs speculated
- **Source transparency:** Primary vs secondary vs tertiary
- **Verification access:** Click through to see HOW verified

### Safety
- **Prevents epistemic placebos:** Glyphs ALWAYS link to verification data
- **Supports critical thinking:** Visual cues prompt skepticism when appropriate
- **Audit trails:** Full documentation for high-stakes decisions

### Universality
- **Cross-domain:** Works for healthcare, research, code, news, etc.
- **Platform-agnostic:** Can integrate with any AI system
- **Compositional:** Grammar extends to new use cases

---

**Document version:** 1.0  
**Last updated:** April 24, 2026  
**Purpose:** Demonstrate real-world applications of Epistemic Glyphs across domains
