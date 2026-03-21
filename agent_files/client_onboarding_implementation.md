# Client Onboarding Agent - Implementation Guide

## Overview

This document provides technical implementation details for the interactive Client Onboarding Agent.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TELEGRAM INTERFACE                       │
│                   (User Messages)                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              CONVERSATION STATE MANAGER                      │
│         (Track phase, questions, collected data)            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              DIALOGUE ENGINE                                 │
│  • Phase router                                              │
│  • Question selector                                         │
│  • Response parser                                           │
│  • Context manager                                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              CONTENT GENERATOR                               │
│  • Persona analyzer                                          │
│  • Keyword researcher                                        │
│  • Competitor researcher                                     │
│  • Roadmap builder                                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              FILE SYSTEM                                      │
│  • Save generated content                                    │
│  • Create client folder                                       │
│  • Update tracking files                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## State Management

### Session State JSON Structure

```json
{
  "session_id": "uuid-v4-string",
  "client_id": "telegram-user-id",
  "client_name": "Telegram Display Name",
  "started_at": "2026-03-21T15:30:00+03:00",
  "last_activity": "2026-03-21T15:45:00+03:00",
  
  "conversation": {
    "current_phase": "discovery", // hook, discovery, analysis, presentation, approval
    "current_question": 3,
    "total_questions": 6,
    "messages_exchanged": 12
  },
  
  "collected_data": {
    "product": {
      "name": "Word Hype",
      "description": "Offline vocabulary learning app with local AI",
      "platform": ["iOS", "Android"],
      "current_status": "1000+ users, active marketing"
    },
    "target_audience": {
      "primary": "ESL students preparing for IELTS/TOEFL",
      "age_range": "18-35",
      "personas_selected": ["active_learner", "commuter"]
    },
    "competitors": [
      {"name": "Duolingo", "strength": "Brand recognition", "weakness": "Requires internet"},
      {"name": "Anki", "strength": "SRS system", "weakness": "Complex UI"}
    ],
    "constraints": {
      "budget": "zero",
      "time_per_week": "3-5 hours",
      "primary_goal": "user_acquisition"
    }
  },
  
  "generated_content": {
    "persona_analysis": "path/to/file.md",
    "keyword_strategy": "path/to/file.md",
    "roadmap": "path/to/file.md",
    "content_calendar": "path/to/file.json"
  },
  
  "approval": {
    "status": "pending", // pending, approved, rejected, needs_revision
    "approved_at": null,
    "revision_requests": []
  }
}
```

---

## Conversation Flow Implementation

### Phase Router

```python
class ConversationPhaseRouter:
    PHASES = ['hook', 'discovery', 'analysis', 'presentation', 'approval', 'execution']
    
    def __init__(self, state):
        self.state = state
    
    def get_next_message(self, user_input=None):
        """Main entry point for generating next message"""
        current_phase = self.state['conversation']['current_phase']
        
        phase_handlers = {
            'hook': self._handle_hook_phase,
            'discovery': self._handle_discovery_phase,
            'analysis': self._handle_analysis_phase,
            'presentation': self._handle_presentation_phase,
            'approval': self._handle_approval_phase,
            'execution': self._handle_execution_phase
        }
        
        handler = phase_handlers.get(current_phase)
        if handler:
            return handler(user_input)
        
        return self._generate_error_message()
    
    def _handle_hook_phase(self, user_input):
        """Handle initial rapport building"""
        if not user_input:
            return self._generate_welcome_message()
        
        # Check if user wants to start or needs more info
        if self._intent_is_start(user_input):
            self._transition_to_phase('discovery')
            return self._generate_discovery_question(1)
        else:
            return self._generate_explanation_message()
    
    def _handle_discovery_phase(self, user_input):
        """Handle information gathering"""
        if user_input:
            self._store_answer(user_input)
            self._increment_question()
        
        current_q = self.state['conversation']['current_question']
        
        if current_q > 6:
            self._transition_to_phase('analysis')
            return self._generate_analysis_transition()
        
        return self._generate_discovery_question(current_q)
    
    def _handle_analysis_phase(self, user_input):
        """Generate analysis and wait for completion"""
        # Trigger async analysis
        self._start_analysis()
        self._transition_to_phase('presentation')
        return self._generate_presentation()
    
    def _handle_presentation_phase(self, user_input):
        """Present plan and handle feedback"""
        if self._intent_is_approval(user_input):
            self._transition_to_phase('execution')
            return self._generate_execution_start()
        elif self._intent_is_revision(user_input):
            self._handle_revision_request(user_input)
            return self._generate_revised_presentation()
        else:
            return self._clarify_presentation()
    
    def _handle_approval_phase(self, user_input):
        """Handle explicit approval"""
        if self._intent_is_approval(user_input):
            self._mark_as_approved()
            self._transition_to_phase('execution')
            return self._generate_execution_start()
        else:
            return self._address_concerns(user_input)
    
    def _handle_execution_phase(self, user_input):
        """Execute approved plan"""
        return self._execute_plan_step()
```

---

## Response Parsing

### Intent Detection

```python
class IntentDetector:
    """Detect user intent from natural language input"""
    
    def __init__(self):
        self.intent_patterns = {
            'start': [
                r'başlayalım', r'hadi', r'tamam', r'evet', r'olur',
                r'let\'s go', r'start', r'yes', r'ok', r'okay'
            ],
            'approval': [
                r'onaylıyorum', r'tamam', r'evet', r'harika', r'mükemmel',
                r'begendim', r'approved', r'yes', r'great', r'perfect',
                r'love it', r'başlayalım'
            ],
            'revision': [
                r'değiştir', r'düzenle', r'başka', r'farklı', r'sanırım',
                r'change', r'edit', r'modify', r'different', r'not sure'
            ],
            'question': [
                r'neden', r'nasıl', r'ne', r'kim', r'nerede', r'niçin',
                r'why', r'how', r'what', r'who', r'where', r'when'
            ],
            'concern': [
                r'emin değilim', r'kararsızım', r'zannetmiyorum',
                r'not sure', r'uncertain', r'doubt', r'worried',
                r'expensive', r'too much', r'çok pahalı'
            ],
            'exit': [
                r'iptal', r'vazgeç', r'sonra', r'bitti',
                r'cancel', r'quit', r'exit', r'later', r'done'
            ]
        }
    
    def detect_intent(self, message):
        """Detect primary intent from message"""
        message_lower = message.lower()
        
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, message_lower):
                    return intent
        
        return 'unknown'
    
    def extract_product_info(self, message):
        """Extract product details from description"""
        # Platform detection
        platforms = []
        if any(word in message.lower() for word in ['ios', 'app store', 'iphone']):
            platforms.append('iOS')
        if any(word in message.lower() for word in ['android', 'play store', 'google play']):
            platforms.append('Android')
        if any(word in message.lower() for word in ['web', 'saas', 'browser']):
            platforms.append('Web')
        
        # Category detection
        categories = {
            'education': ['öğren', 'learn', 'education', 'eğitim', 'okul'],
            'productivity': ['productivity', 'verimlilik', 'çalış', 'work'],
            'health': ['health', 'sağlık', 'fitness', 'spor'],
            'finance': ['finance', 'para', 'money', 'finans']
        }
        
        detected_category = None
        for category, keywords in categories.items():
            if any(keyword in message.lower() for keyword in keywords):
                detected_category = category
                break
        
        return {
            'platforms': platforms,
            'category': detected_category,
            'description': message
        }
    
    def extract_persona_choice(self, message):
        """Extract which persona user selected"""
        numbers = re.findall(r'\d+', message)
        if numbers:
            return int(numbers[0])
        
        # Check for text mentions
        persona_keywords = {
            1: ['öğrenci', 'student', 'learner', 'öğren'],
            2: ['profesyonel', 'professional', 'çalış', 'work'],
            3: ['tech', 'developer', 'ai', 'teknoloji'],
            4: ['commuter', 'metro', 'yolculuk', 'seyahat']
        }
        
        for num, keywords in persona_keywords.items():
            if any(keyword in message.lower() for keyword in keywords):
                return num
        
        return None
```

---

## Content Generation Pipeline

### Async Analysis Pipeline

```python
class AnalysisPipeline:
    """Generate all marketing content after discovery phase"""
    
    async def generate_full_plan(self, collected_data):
        """Generate complete Phase 1 marketing plan"""
        
        results = {}
        
        # Parallel execution of independent tasks
        tasks = [
            self._analyze_persona(collected_data),
            self._research_keywords(collected_data),
            self._analyze_competitors(collected_data),
            self._generate_content_calendar(collected_data)
        ]
        
        persona, keywords, competitors, calendar = await asyncio.gather(*tasks)
        
        results['persona'] = persona
        results['keywords'] = keywords
        results['competitors'] = competitors
        results['calendar'] = calendar
        
        # Sequential dependent tasks
        results['roadmap'] = await self._generate_roadmap(
            persona, keywords, competitors
        )
        
        results['aso_metadata'] = await self._generate_aso_metadata(
            collected_data, keywords
        )
        
        return results
    
    async def _analyze_persona(self, data):
        """Generate detailed persona analysis"""
        product = data['product']
        audience = data['target_audience']
        
        prompt = f"""
        Analyze this target audience and create detailed personas:
        
        Product: {product['name']} - {product['description']}
        Target: {audience['primary']}
        
        Create 3 distinct personas with:
        1. Name and demographics
        2. Pain points
        3. Goals and motivations
        4. Where they spend time online
        5. Marketing messaging that resonates
        6. Content topics they care about
        
        Format as structured markdown.
        """
        
        return await self._call_llm(prompt)
    
    async def _research_keywords(self, data):
        """Research ASO keywords"""
        product = data['product']
        
        # This would integrate with actual keyword research APIs
        # For now, generate based on product description
        
        prompt = f"""
        Generate ASO keywords for this app:
        Name: {product['name']}
        Description: {product['description']}
        
        Provide:
        1. 5 head terms (high volume, competitive)
        2. 10 long-tail keywords (specific intent)
        3. 5 competitor brand names for conquesting
        4. 5 feature-based keywords
        
        Include search volume estimates (High/Medium/Low).
        """
        
        return await self._call_llm(prompt)
    
    async def _analyze_competitors(self, data):
        """Analyze competitors"""
        competitors = data.get('competitors', [])
        
        analysis = []
        for comp in competitors:
            analysis.append({
                'name': comp['name'],
                'strengths': comp.get('strength', 'Unknown'),
                'weaknesses': comp.get('weakness', 'Unknown'),
                'opportunities': self._identify_opportunities(comp)
            })
        
        return analysis
    
    async def _generate_roadmap(self, persona, keywords, competitors):
        """Generate Phase 1 roadmap"""
        
        prompt = f"""
        Create a detailed 2-week Phase 1 marketing roadmap:
        
        Personas: {persona}
        Keywords: {keywords}
        Competitors: {competitors}
        
        Include:
        1. Week 1 tasks (ASO, Persona, Competitor)
        2. Week 2 tasks (Content, GEO setup)
        3. Daily breakdown
        4. Expected outcomes
        5. Success metrics
        
        Format as markdown table.
        """
        
        return await self._call_llm(prompt)
    
    async def _generate_aso_metadata(self, data, keywords):
        """Generate App Store metadata"""
        
        product = data['product']
        
        return {
            'title': self._generate_title(product, keywords),
            'subtitle': self._generate_subtitle(product, keywords),
            'keywords': self._generate_keyword_string(keywords),
            'description': self._generate_description(product)
        }
```

---

## File System Integration

### Client Folder Structure

```python
class ClientFolderManager:
    """Manage file system for each client"""
    
    BASE_PATH = "/results/clients/{client_id}/"
    
    def create_client_structure(self, client_id, client_name):
        """Create folder structure for new client"""
        
        folders = [
            f"{self.BASE_PATH}/phase1/",
            f"{self.BASE_PATH}/phase2/",
            f"{self.BASE_PATH}/content/blog/",
            f"{self.BASE_PATH}/content/social/",
            f"{self.BASE_PATH}/content/newsletter/",
            f"{self.BASE_PATH}/assets/",
            f"{self.BASE_PATH}/analytics/",
            f"{self.BASE_PATH}/tasks/",
            f"{self.BASE_PATH}/reports/"
        ]
        
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
        
        # Create README for client
        self._create_client_readme(client_id, client_name)
        
        return self.BASE_PATH
    
    def save_generated_content(self, client_id, content_type, content):
        """Save generated content to appropriate location"""
        
        file_paths = {
            'persona': f"{self.BASE_PATH}/phase1/persona_analysis.md",
            'keywords': f"{self.BASE_PATH}/phase1/keyword_strategy.md",
            'competitors': f"{self.BASE_PATH}/phase1/competitor_analysis.md",
            'roadmap': f"{self.BASE_PATH}/phase1/marketing_roadmap.md",
            'calendar': f"{self.BASE_PATH}/tasks/content_calendar.json",
            'aso': f"{self.BASE_PATH}/phase1/aso_metadata.json"
        }
        
        file_path = file_paths.get(content_type)
        if not file_path:
            raise ValueError(f"Unknown content type: {content_type}")
        
        if isinstance(content, dict):
            with open(file_path, 'w') as f:
                json.dump(content, f, indent=2)
        else:
            with open(file_path, 'w') as f:
                f.write(content)
        
        return file_path
```

---

## Execution Tracking

### Weekly Task Automation

```python
class WeeklyExecutionManager:
    """Manage weekly marketing task execution"""
    
    def __init__(self, client_id):
        self.client_id = client_id
        self.client_path = f"/results/clients/{client_id}/"
    
    def get_todays_tasks(self):
        """Get tasks for today based on schedule"""
        
        day_of_week = datetime.now().strftime('%A').lower()
        
        schedule = {
            'monday': ['competitor_intelligence', 'keyword_tracking'],
            'tuesday': ['blog_post_creation'],
            'wednesday': ['social_content', 'reddit_engagement'],
            'thursday': ['geo_maintenance', 'directory_submission'],
            'friday': ['newsletter_creation', 'performance_review']
        }
        
        return schedule.get(day_of_week, [])
    
    def execute_task(self, task_name):
        """Execute a specific marketing task"""
        
        task_handlers = {
            'competitor_intelligence': self._run_competitor_analysis,
            'blog_post_creation': self._generate_blog_post,
            'social_content': self._generate_social_posts,
            'reddit_engagement': self._find_reddit_threads,
            'geo_maintenance': self._check_geo_status,
            'newsletter_creation': self._generate_newsletter
        }
        
        handler = task_handlers.get(task_name)
        if handler:
            return handler()
        
        return None
    
    def _generate_blog_post(self):
        """Generate weekly blog post"""
        
        # Load content calendar
        calendar = self._load_content_calendar()
        
        # Get next topic
        topic = calendar.get_next_topic()
        
        # Generate using blog_post_writer skill
        return self._run_skill('blog_post_writer', topic)
```

---

## Integration Points

### OpenClaw Integration

```yaml
# openclaw_config.yaml
client_onboarding_agent:
  name: "Client Onboarding Agent"
  description: "Interactive marketing consultant for client onboarding"
  
  triggers:
    - type: "message"
      pattern: ".*marketing.*|.*strateji.*|.*plan.*"
    
  capabilities:
    - name: "conversation_management"
      handler: "conversation_phase_router"
    
    - name: "content_generation"
      handler: "analysis_pipeline"
      requires:
        - "llm_api_key"
    
    - name: "file_management"
      handler: "client_folder_manager"
    
    - name: "task_scheduling"
      handler: "weekly_execution_manager"
      schedule: "daily"
  
  storage:
    path: "/results/clients/{client_id}/"
    
  notifications:
    on_completion: true
    on_approval: true
    weekly_digest: true
```

---

## Testing

### Conversation Flow Tests

```python
class TestConversationFlow(unittest.TestCase):
    """Test conversation flows"""
    
    def test_welcome_to_discovery_transition(self):
        """Test user accepts welcome and moves to discovery"""
        
        agent = ClientOnboardingAgent()
        
        # Start
        response1 = agent.get_next_message()
        self.assertIn("Merhaba", response1)
        
        # User says "Hadi başlayalım"
        response2 = agent.process_message("Hadi başlayalım")
        self.assertIn("Soru 1", response2)
        self.assertEqual(agent.state['phase'], 'discovery')
    
    def test_discovery_completion(self):
        """Test completing all 6 discovery questions"""
        
        agent = ClientOnboardingAgent()
        agent._transition_to_phase('discovery')
        
        # Answer all questions
        answers = [
            "Vocabulary learning app for ESL students",
            "iOS platform",
            "100-1000 users, no marketing yet",
            "ESL students preparing for IELTS",
            "Duolingo, Anki",
            "Zero budget, 3-5 hours/week, user acquisition"
        ]
        
        for answer in answers:
            agent.process_message(answer)
        
        self.assertEqual(agent.state['phase'], 'analysis')
    
    def test_approval_flow(self):
        """Test plan approval"""
        
        agent = ClientOnboardingAgent()
        agent._transition_to_phase('presentation')
        
        # User approves
        response = agent.process_message("Harika, onaylıyorum!")
        self.assertEqual(agent.state['approval']['status'], 'approved')
        self.assertEqual(agent.state['phase'], 'execution')
```

---

## Deployment Checklist

### Pre-Launch
- [ ] Conversation flows tested
- [ ] Intent detection validated
- [ ] Content generation working
- [ ] File system permissions set
- [ ] LLM API keys configured
- [ ] Error handling implemented

### Post-Launch Monitoring
- [ ] Track conversation completion rates
- [ ] Monitor response times
- [ ] Log user feedback
- [ ] A/B test message variants
- [ ] Track approval rates

---

## Future Enhancements

### Phase 2 Features
1. **Voice Input** - Accept voice messages, transcribe with Whisper
2. **Visual Persona** - Show persona cards with images
3. **Interactive Charts** - Show marketing funnel visualization
4. **Real Preview** - Show generated content preview before approval
5. **Collaboration** - Multiple team members per client
6. **API Integration** - Connect to App Store, Google Ads, etc.

### Analytics Dashboard
- Conversion rate: Conversations → Approvals
- Average time to approval
- Most common revision requests
- Popular personas by industry
- Content performance tracking

---

*Implementation Guide v1.0*
