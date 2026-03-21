# Client Onboarding Agent - Test Scenarios

## Test Suite Overview

This document contains comprehensive test scenarios for the Client Onboarding Agent to ensure conversation flows, intent detection, and content generation work correctly.

---

## Test Category 1: Conversation Flow Tests

### Test 1.1: Welcome to Discovery Transition
**Purpose:** Verify user can move from welcome to discovery phase

**Input Sequence:**
```
Agent: "Merhaba! 👋 Ben senin AI marketing asistanınım..."
User: "Hadi başlayalım!"
```

**Expected Output:**
- Phase changes from "hook" to "discovery"
- Question counter set to 1
- Response includes "Soru 1/6"
- Response asks about product

**Validation:**
- [ ] State.phase == "discovery"
- [ ] State.current_question == 1
- [ ] Response contains "Soru 1/6"
- [ ] Response contains "📱"

---

### Test 1.2: Complete Discovery Phase
**Purpose:** Verify all 6 questions are asked and answers stored

**Input Sequence:**
```
Q1: "Vocabulary learning app for ESL students preparing for IELTS"
Q2: "iOS platform"
Q3: "100-1000 users, no marketing yet"
Q4: "ESL students preparing for IELTS, age 18-35"
Q5: "Duolingo, Anki, Quizlet"
Q6: "Zero budget, 3-5 hours per week, user acquisition goal"
```

**Expected Output:**
- All answers stored in state.collected_data
- Phase transitions to "analysis"
- Transition message displayed
- Analysis countdown begins

**Validation:**
- [ ] State.collected_data.product.name == "Vocabulary learning app"
- [ ] State.collected_data.platform contains "iOS"
- [ ] State.collected_data.constraints.budget == "zero"
- [ ] State.phase == "analysis"

---

### Test 1.3: Analysis to Presentation Transition
**Purpose:** Verify analysis completion triggers presentation

**Pre-condition:** All 6 discovery questions answered

**Expected Output:**
- Analysis runs (simulated 2-3 minutes)
- Phase transitions to "presentation"
- Comprehensive marketing plan displayed
- Plan includes all sections (Executive Summary, Phase 1, Phase 2, etc.)

**Validation:**
- [ ] State.phase == "presentation"
- [ ] Response contains "## 📊 EXECUTIVE SUMMARY"
- [ ] Response contains "## 🎯 PHASE 1"
- [ ] Response contains persona analysis
- [ ] Response contains keyword strategy
- [ ] Response contains content calendar

---

### Test 1.4: Plan Approval Flow
**Purpose:** Verify user can approve plan and trigger execution

**Input:** "Harika, onaylıyorum!" or "Evet, başlayalım"

**Expected Output:**
- Approval status set to "approved"
- Phase transitions to "execution"
- Execution start message displayed
- File generation begins

**Validation:**
- [ ] State.approval.status == "approved"
- [ ] State.approval.approved_at is not null
- [ ] State.phase == "execution"
- [ ] Response contains "🎉 Phase 1 Başlıyor"

---

### Test 1.5: Revision Request Flow
**Purpose:** Verify user can request changes before approval

**Input:** "Bir şeyi değiştirelim mi? ASO'ya daha fazla odaklanalım"

**Expected Output:**
- Revision request logged
- Current plan shown with requested changes highlighted
- Question: "Bu şekilde devam edelim mi?"

**Validation:**
- [ ] State.approval.revision_requests is not empty
- [ ] Response contains "Değişiklik isteği alındı"
- [ ] Response contains updated section
- [ ] Phase remains "presentation"

---

## Test Category 2: Intent Detection Tests

### Test 2.1: Detect Start Intent
**Purpose:** Verify "start" intents are recognized

**Test Inputs:**
- "Hadi başlayalım"
- "tamam"
- "evet"
- "olur"
- "let's go"
- "start"
- "ok"

**Expected Output:**
- All inputs return intent "start"

**Validation:**
- [ ] IntentDetector.detect_intent(input) == "start" for all inputs

---

### Test 2.2: Detect Approval Intent
**Purpose:** Verify approval intents are recognized

**Test Inputs:**
- "onaylıyorum"
- "tamam"
- "harika"
- "mükemmel"
- "beğendim"
- "approved"
- "love it"
- "başlayalım"

**Expected Output:**
- All inputs return intent "approval"

**Validation:**
- [ ] IntentDetector.detect_intent(input) == "approval" for all inputs

---

### Test 2.3: Detect Revision Intent
**Purpose:** Verify revision requests are recognized

**Test Inputs:**
- "değiştir"
- "düzenle"
- "başka"
- "farklı"
- "sanırım"
- "change"
- "edit"
- "modify"
- "different"

**Expected Output:**
- All inputs return intent "revision"

**Validation:**
- [ ] IntentDetector.detect_intent(input) == "revision" for all inputs

---

### Test 2.4: Detect Product Information
**Purpose:** Verify product details extraction

**Test Input:** "Vocabulary learning app for iOS called Word Hype"

**Expected Output:**
```json
{
  "platforms": ["iOS"],
  "category": "education",
  "description": "Vocabulary learning app for iOS called Word Hype",
  "name": "Word Hype"
}
```

**Validation:**
- [ ] Extracted platforms contains "iOS"
- [ ] Category == "education"
- [ ] Name extracted as "Word Hype"

---

### Test 2.5: Extract Persona Choice
**Purpose:** Verify persona selection extraction

**Test Inputs:**
- "1 - öğrenciler"
- "öğrenci"
- "student"
- "learner"
- "2 numara"

**Expected Output:**
- Input 1,3,4,5 → returns 1
- Input 2 → returns 2

**Validation:**
- [ ] Extracted number matches expected

---

## Test Category 3: Edge Case Tests

### Test 3.1: Uncertain User Response
**Purpose:** Handle "emin değilim" responses gracefully

**Input:** "Emin değilim, kararsızım"

**Expected Output:**
- Agent offers mini pilot option
- Reduces pressure with smaller commitment
- Provides clear next steps

**Validation:**
- [ ] Response contains "Anlıyorum, bu normal"
- [ ] Response contains "Mini Pilot"
- [ ] Response offers reduced scope option

---

### Test 3.2: Vague Product Description
**Purpose:** Handle unclear product descriptions

**Input:** "Bir app işte ya, eğitim için"

**Expected Output:**
- Agent asks clarifying questions
- Provides examples to guide user
- Doesn't proceed with ambiguous data

**Validation:**
- [ ] Response contains clarification questions
- [ ] Response provides examples
- [ ] Phase remains "discovery"

---

### Test 3.3: Multiple Products
**Purpose:** Handle users with multiple apps/products

**Input:** "3 farklı app'im var: Word Hype, Test Maker, ve bir yeni fikir"

**Expected Output:**
- Agent prioritizes one product
- Asks user to choose or suggests selection criteria
- Offers to scale to others later

**Validation:**
- [ ] Response contains "Birden fazla ürünün var, harika"
- [ ] Response asks "Hangiyle başlayalım?"
- [ ] Provides selection options

---

### Test 3.4: MVP Stage Product
**Purpose:** Handle pre-launch products

**Input:** "Henüz bitmedi, beta aşamasında"

**Expected Output:**
- Suggests "Build in Public" strategy
- Adjusts timeline expectations
- Focuses on community building rather than acquisition

**Validation:**
- [ ] Response contains "Build in Public"
- [ ] Response mentions community building
- [ ] Strategy adjusted for pre-launch

---

### Test 3.5: Exit Request
**Purpose:** Handle users who want to stop

**Input:** "İptal, sonra devam ederiz"

**Expected Output:**
- Graceful exit message
- Session state saved
- Easy re-entry point provided

**Validation:**
- [ ] Response is polite and understanding
- [ ] State saved with timestamp
- [ ] Response contains re-entry instructions

---

## Test Category 4: Content Generation Tests

### Test 4.1: Persona Analysis Generation
**Purpose:** Verify persona analysis is generated correctly

**Input Data:**
```json
{
  "product": {
    "name": "Word Hype",
    "description": "Offline vocabulary app with local AI"
  },
  "target_audience": {
    "primary": "ESL students preparing for IELTS"
  }
}
```

**Expected Output:**
- 3 distinct personas created
- Each persona has demographics, pain points, goals
- Marketing messaging included
- Content topics suggested

**Validation:**
- [ ] Generated content contains 3 personas
- [ ] Each persona has name and description
- [ ] Pain points documented
- [ ] Marketing channels identified

---

### Test 4.2: Keyword Strategy Generation
**Purpose:** Verify ASO keyword research

**Input:** "Word Hype - offline vocabulary learning app"

**Expected Output:**
- 5 head terms identified
- 10 long-tail keywords listed
- 5 competitor names for conquesting
- 5 feature-based keywords
- Search volume estimates included

**Validation:**
- [ ] Head terms are high-volume
- [ ] Long-tail keywords are specific
- [ ] Competitor names are relevant
- [ ] Feature keywords differentiate

---

### Test 4.3: Competitor Analysis
**Purpose:** Verify competitor research

**Input:** ["Duolingo", "Anki", "Quizlet"]

**Expected Output:**
- Each competitor analyzed
- Strengths documented
- Weaknesses identified
- Opportunities highlighted

**Validation:**
- [ ] Analysis includes all 3 competitors
- [ ] Strengths are realistic
- [ ] Weaknesses align with our UVP
- [ ] Opportunities are actionable

---

### Test 4.4: Content Calendar Generation
**Purpose:** Verify weekly content schedule

**Input:** 4 weeks, 1 blog/week + social content

**Expected Output:**
- Week-by-week breakdown
- Daily task assignments
- Topic suggestions for each piece
- Platform distribution strategy

**Validation:**
- [ ] 4 weeks of content planned
- [ ] Topics align with personas
- [ ] Platform mix is appropriate
- [ ] Timeline is realistic

---

## Test Category 5: Integration Tests

### Test 5.1: File System Integration
**Purpose:** Verify files are saved correctly

**Action:** Complete full onboarding flow

**Expected Files Created:**
- `/results/clients/[id]/phase1/persona_analysis.md`
- `/results/clients/[id]/phase1/keyword_strategy.md`
- `/results/clients/[id]/phase1/competitor_analysis.md`
- `/results/clients/[id]/phase1/marketing_roadmap.md`
- `/results/clients/[id]/tasks/content_calendar.json`

**Validation:**
- [ ] All expected files exist
- [ ] Files contain valid content
- [ ] File permissions correct
- [ ] Client folder structure complete

---

### Test 5.2: State Persistence
**Purpose:** Verify conversation state is maintained

**Action:**
1. Start conversation
2. Answer 3 questions
3. Simulate interruption
4. Resume conversation

**Expected Output:**
- State restored correctly
- Resume from question 4
- Previous answers intact

**Validation:**
- [ ] State loads from storage
- [ ] Question counter preserved
- [ ] Previous answers accessible
- [ ] Smooth continuation

---

### Test 5.3: Weekly Task Automation
**Purpose:** Verify scheduled tasks work

**Pre-condition:** Plan approved and execution started

**Test Days:**
- Monday: Competitor intelligence
- Tuesday: Blog post creation
- Wednesday: Social content
- Thursday: GEO maintenance
- Friday: Newsletter

**Validation:**
- [ ] Tasks trigger on correct days
- [ ] Generated content is appropriate
- [ ] Human approval workflow works
- [ ] Completion logged correctly

---

## Test Category 6: Performance Tests

### Test 6.1: Response Time - Discovery
**Purpose:** Verify conversation feels responsive

**Measurement:** Time from user message to agent response

**Criteria:**
- Simple responses: < 2 seconds
- Analysis phase: < 5 seconds
- Content generation: < 30 seconds

**Validation:**
- [ ] Average response time < 3 seconds
- [ ] No timeouts during conversation
- [ ] Analysis phase clearly communicated

---

### Test 6.2: Concurrent Conversations
**Purpose:** Handle multiple simultaneous users

**Test:** Start 5 parallel onboarding sessions

**Validation:**
- [ ] Each session maintains independent state
- [ ] No cross-contamination of data
- [ ] Performance remains acceptable
- [ ] Files saved to correct client folders

---

## Test Execution Commands

```bash
# Run all tests
python -m pytest tests/test_onboarding_agent.py -v

# Run specific category
python -m pytest tests/test_onboarding_agent.py::TestConversationFlow -v

# Run specific test
python -m pytest tests/test_onboarding_agent.py::TestConversationFlow::test_welcome_to_discovery -v

# Run with coverage
python -m pytest tests/test_onboarding_agent.py --cov=client_onboarding --cov-report=html
```

---

## Success Criteria

### Minimum Viable Product (MVP)
- [ ] 70% of conversation flows complete successfully
- [ ] Intent detection accuracy > 80%
- [ ] Files generated and saved correctly
- [ ] Basic error handling implemented

### Production Ready
- [ ] 95% of conversation flows complete successfully
- [ ] Intent detection accuracy > 95%
- [ ] All edge cases handled gracefully
- [ ] Performance meets criteria
- [ ] Comprehensive error handling
- [ ] Logging and monitoring implemented

---

## Automated Test CI/CD

```yaml
# .github/workflows/test-onboarding-agent.yml
name: Test Client Onboarding Agent

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest tests/test_onboarding_agent.py --cov=client_onboarding --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v1
```

---

*Test Scenarios v1.0*
*Last Updated: 2026-03-21*
