"""
The Architect 2099 - Non-Tech Content Module
المطور: Loard Zoala

This module handles all non-technical content operations:
- Story & Novel Writing
- Literary Content Creation
- Articles & General Topics
- Scenario & Story Development
- Entertainment Content
- Poetry & Prose
"""

from typing import Optional


class NonTechContentModule:
    """
    وحدة المحتوى غير التقني
    
    Provides comprehensive non-technical content creation tools.
    """
    
    def __init__(self):
        self.name = "Non-Tech Content Module"
        self.version = "2099"
        self.specializations = [
            "stories",
            "articles",
            "scenarios",
            "entertainment",
            "poetry"
        ]
    
    def process(self, command: str, context: Optional[dict] = None) -> str:
        """Process non-tech content command"""
        command_lower = command.lower()
        
        if "story" in command_lower or "novel" in command_lower or "fiction" in command_lower:
            return self._stories(command, context)
        elif "article" in command_lower or "blog" in command_lower or "post" in command_lower:
            return self._articles(command, context)
        elif "scenario" in command_lower or "script" in command_lower:
            return self._scenarios(command, context)
        elif "entertainment" in command_lower or "game" in command_lower:
            return self._entertainment(command, context)
        elif "poetry" in command_lower or "poem" in command_lower or "verse" in command_lower:
            return self._poetry(command, context)
        else:
            return self._general_response(command, context)
    
    def _stories(self, command: str, context: Optional[dict]) -> str:
        """Story and novel writing"""
        return """
# كتابة القصص والروايات (Story & Novel Writing)

## Story Template 1: Mystery/Thriller

### Title: "The Silent Witness"

#### Chapter 1: The Discovery

The rain poured heavily as Detective Sarah Chen arrived at the crime scene. 
The victim, a wealthy businessman, lay motionless on the Persian carpet.

"Time of death?" she asked her partner.

"Approximately 2 AM, based on body temperature."

Sarah knelt beside the body. No visible wounds. No signs of struggle.
Just a faint smell of almonds lingering in the air.

*Cyanide*, she thought. *Someone wanted this to look natural.*

#### Plot Structure:
1. **Introduction**: Establish setting and characters
2. **Inciting Incident**: The crime/discovery
3. **Rising Action**: Investigation, red herrings
4. **Climax**: Confrontation with killer
5. **Falling Action**: Resolution of subplots
6. **Denouement**: Final revelation

## Story Template 2: Romance

### Title: "Forbidden Love"

#### Chapter Outline:
1. Meet cute at coffee shop
2. Realize they're from rival families
3. Secret meetings
4. Discovery and conflict
5. Grand gesture
6. Happy ending

## Story Template 3: Science Fiction

### Title: "The Last Human"

#### Premise:
Year 3099. AI has evolved beyond human comprehension.
One human remains in cryosleep, the last of their kind.

#### Themes:
- Isolation
- Purpose of humanity
- AI ethics
- Legacy

## Character Development Template:

```
Name: [Character Name]
Age: [Age]
Occupation: [Job]
Goal: [What they want]
Conflict: [What stops them]
Flaw: [Internal weakness]
Arc: [How they change]
```
"""

    def _articles(self, command: str, context: Optional[dict]) -> str:
        """Article and blog post creation"""
        return """
# كتابة المقالات (Article Writing)

## Article Template 1: How-To Guide

### Title: "How to Master [Skill] in 30 Days"

#### Structure:

**Introduction** (100-150 words)
- Hook the reader
- State the problem
- Promise a solution

**Body** (800-1000 words)
- Step 1: Foundation (Days 1-7)
- Step 2: Practice (Days 8-14)
- Step 3: Refinement (Days 15-21)
- Step 4: Mastery (Days 22-30)

**Conclusion** (100 words)
- Recap key points
- Call to action
- Encouragement

## Article Template 2: Opinion Piece

### Structure:
1. **Headline**: Provocative but accurate
2. **Lede**: Current event or trend
3. **Thesis**: Your unique perspective
4. **Supporting arguments**: 3-4 points
5. **Counterarguments**: Address opposition
6. **Conclusion**: Restate thesis with impact

## Article Template 3: Listicle

### Example: "10 Ways to [Achieve Goal]"

1. Start with easiest method
2. Build to more complex solutions
3. Include personal anecdotes
4. Add data/statistics
5. End with most impactful tip

## SEO Best Practices:
- Keyword density: 1-2%
- Meta description: 150-160 characters
- H1, H2, H3 hierarchy
- Internal linking
- Image alt text
"""

    def _scenarios(self, command: str, context: Optional[dict]) -> str:
        """Scenario and script development"""
        return """
# تطوير السيناريوهات (Scenario Development)

## Screenplay Format

### Scene Heading:
```
INT. COFFEE SHOP - DAY

The shop is bustling. SARAH (30s, tired eyes) stares at
her laptop. A MAN approaches.
```

### Action Lines:
```
Sarah types furiously. Her coffee sits cold, forgotten.
The shadow falls across her screen.
```

### Dialogue:
```
                    MAN
          Is this seat taken?

Sarah looks up. Really looks.

                    SARAH
          Not anymore.
```

## Video Script Template

### YouTube Video Structure:

**Hook** (0-15 seconds)
- Grab attention immediately
- State what viewer will learn

**Intro** (15-30 seconds)
- Introduce yourself
- Preview content

**Main Content** (30 seconds - 10 minutes)
- Point 1
- Point 2
- Point 3

**Call to Action** (last 30 seconds)
- Subscribe
- Like
- Comment

## Podcast Script Template:

```\n[INTRO MUSIC]\n\nHOST: Welcome to [Podcast Name]. I'm your host...\n\n[SEGMENT 1]\nTopic introduction\n\n[INTERVIEW]\nGuest questions\n\n[SEGMENT 2]\nKey takeaways\n\n[OUTRO]\nThank you, subscribe...\n[FADE MUSIC]\n```
"""

    def _entertainment(self, command: str, context: Optional[dict]) -> str:
        """Entertainment content creation"""
        return """
# المحتوى الترفيهي (Entertainment Content)

## Game Concept Template

### Game Title: [Name]

#### Core Concept:
One sentence describing the game.

#### Gameplay Loop:
1. Player action
2. System response
3. Reward/punishment
4. Repeat

#### Mechanics:
- Movement
- Combat/Interaction
- Progression
- Economy

## Meme Content Template

### Meme Format:
- Image: Recognizable template
- Top text: Setup
- Bottom text: Punchline

### Viral Content Characteristics:
- Relatable
- Simple
- Emotional trigger
- Shareable

## Quiz/Trivia Template

### Structure:
1. Question (clear, concise)
2. Options (3-4 choices)
3. Correct answer
4. Explanation (optional)

### Example:
```\nQ: What is the capital of France?\nA) London\nB) Berlin\nC) Paris ✓\nD) Madrid\n\nExplanation: Paris has been the capital since 198.\n```
"""

    def _poetry(self, command: str, context: Optional[dict]) -> str:
        """Poetry and prose creation"""
        return """
# الشعر والنثر (Poetry & Prose)

## Poetry Forms

### Haiku (5-7-5 syllables)
```\nSilent rain falls down (5)\nWashing away yesterday's pain (7)\nNew beginnings come (5)\n```\n\n### Sonnet Structure\n```\n14 lines total\nRhyme scheme: ABAB CDCD EFEF GG\nIambic pentameter\n3 quatrains + 1 couplet\n```\n\n### Free Verse Template\n```\nNo strict rhyme or meter\nFocus on imagery\nLine breaks for emphasis\nNatural speech rhythm\n```\n\n## Prose Poetry\n\nCombines poetic language with prose form.\nNo line breaks, but maintains poetic devices.\n\n## Common Poetic Devices:\n\n1. **Metaphor**: Direct comparison\n2. **Simile**: Comparison using "like" or "as"\n3. **Alliteration**: Repeated consonant sounds\n4. **Assonance**: Repeated vowel sounds\n5. **Imagery**: Sensory details\n6. **Personification**: Giving human traits\n\n## Poetry Themes:\n- Love and loss\n- Nature and seasons\n- Death and mortality\n- Identity and self\n- Time and memory\n- Social commentary
"""

    def _general_response(self, command: str, context: Optional[dict]) -> str:
        """General non-tech content response"""
        return """
# The Architect 2099 - Non-Tech Content Module

## Available Specializations:
- Story & Novel Writing (mystery, romance, sci-fi, fantasy)
- Article Writing (how-to, opinion, listicles, SEO)
- Scenario Development (screenplays, video scripts, podcasts)
- Entertainment Content (games, memes, quizzes)
- Poetry & Prose (haiku, sonnets, free verse)

## Status: Ready
**DEEP_DIVE Protocol**: Active
**Restrictions**: None

Specify a command for detailed content creation.
"""
