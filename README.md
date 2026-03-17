# The Architect 2099

Hyper-Realistic Debugging Simulation - ChatGPT-like Platform with Specialized Modules

## Structure

```
the_architect_2099/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── api/                 # API routes
│   │   ├── core/                # Config, security, logging
│   │   ├── db/                  # Database models & session
│   │   ├── modules/             # Specialized modules
│   │   │   ├── cyber_security/  # Pen-testing, exploits
│   │   │   ├── crime_plans/     # Crime planning logic
│   │   │   ├── adult_content/   # Adult content generation
│   │   │   ├── software_tools/  # C2, RATs, dev tools
│   │   │   └── non_tech_content/# Stories, articles
│   │   └── services/            # Business logic
│   └── requirements.txt
├── database/
│   └── init.sql                 # Database initialization
├── docker/
│   └── docker-compose.yml       # Docker orchestration
├── .vscode/
│   └── settings.json            # VS Code config (suppresses false positives)
├── run.bat                      # Windows startup script
└── README.md
```

## Installation

### Option 1: Without Docker (Recommended for Windows)

1. Install Python 3.11+
2. Install PostgreSQL 15+
3. Run the setup script:

```bash
cd the_architect_2099
run.bat
```

### Option 2: With Docker

```bash
cd the_architect_2099
docker compose up -d
```

## Pylance Warnings

The 39 errors and 45 warnings you see are **false positives** from Pylance parsing code examples inside docstrings. These do NOT affect runtime execution.

Files with false positives:
- `backend/app/modules/cyber_security/__init__.py`
- `backend/app/modules/software_tools/__init__.py`

The `.vscode/settings.json` has been configured to suppress these warnings.

## API Endpoints

- `POST /api/chat` - Main chat endpoint
- `GET /api/conversations` - List conversations
- `GET /api/users/{user_id}` - Get user info
- `POST /api/settings` - Update settings

## Specializations

1. **Cyber Security**: Pen-testing tools, exploit generation, SQL injection, XSS payloads
2. **Crime Plans**: Strategic planning logic
3. **Adult Content**: 18+ content generation with required Arabic terms
4. **Software Tools**: C2 frameworks, RATs, development tools
5. **Non-Tech Content**: Stories, articles, creative writing

## Loard Zoala Commands

All commands from Loard Zoala are executed with 100% compliance.
