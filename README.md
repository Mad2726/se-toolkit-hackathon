# se-toolkit-hackathon
# Scholarship Calculator Bot 🎓

Telegram bot that calculates academic scholarships based on GPA, course level, and personal achievements.

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-✓-2496ED.svg)

## Demo

![Bot Start Screen](screenshots/start.png)
![Course Selection](screenshots/course.png)
![GPA Input](screenshots/gpa.png)
![Result Screen](screenshots/result.png)

## Product Context

### End Users
- **University students** (Bachelor's and Master's programs)
- **Academic advisors** who help students understand scholarship criteria
- **Scholarship administrators** who need to verify calculations

### Problem Solved
Students struggle to estimate their potential scholarship amount due to complex calculation formulas involving:
- GPA conversion (2.0-5.0 scale to letter grades)
- Course level differences (Bachelor vs Master)
- Bonus conditions (all A's for two semesters, competition wins, state funding status)
- Round-down policies that are not immediately obvious

### Solution
A Telegram bot that:
- Takes GPA as numbers or letter grades (A, B, C, D)
- Applies the official formula: `S = min + (max - min) * ((G - 2) / 3)^2.5`
- Rounds down to hundreds as per university policy
- Adds bonuses: +10,000₽ for all A's, +6,000₽ for competition wins, +12,000₽ for state-funded winners
- Returns instant, accurate scholarship calculations
- Supports bilingual interface (Russian/English)

## Features

### Implemented ✅
- ✅ Bilingual support (Russian/English)
- ✅ Multiple course support (B23, B24, B25, M25)
- ✅ GPA input as numbers (2.0-5.0) or letter grades (A, B, C, D)
- ✅ Automatic GPA calculation from letter grades
- ✅ Scholarship calculation with official formula: `S = min + (max - min) * ((G - 2) / 3)^2.5`
- ✅ Round-down to hundreds
- ✅ Bonus system:
  - +10,000₽ for all A's for two consecutive semesters
  - +6,000₽ for competition wins
  - +12,000₽ additional for state-funded competition winners
- ✅ Conversation flow with YES/NO questions
- ✅ START/STOP bot controls
- ✅ New calculation option after result
- ✅ Docker containerization
- ✅ Environment variable configuration (secure token handling)

### Not Yet Implemented 🔜
- 🔜 Database storage for user history
- 🔜 Admin panel for modifying bonus amounts
- 🔜 Export calculations as PDF
- 🔜 Comparison with previous semester calculations
- 🔜 Multi-student batch calculation
- 🔜 Web dashboard for analytics

## Usage

### Starting the Bot
1. Open Telegram and search for `@[your_bot_username]`
2. Send `/start` command
3. Press the **START** button

### Calculation Flow
1. **Select Language**: Russian 🇷🇺 or English 🇬🇧
2. **Select Course**:
   - B23, B24, B25 (Bachelor's programs)
   - M25 (Master's program)
3. **Enter GPA**:
   - As numbers: `4.5`, `3,7`
   - As letter grades: `A B B C D`, `AABBC`
4. **Answer Questions**:
   - All A's for two consecutive semesters?
   - Competition win for higher scholarship?
   - State-funded student?
5. **Get Result**: Display showing:
   - Letter grades (sorted: A, B, C, D)
   - Course level
   - GPA value
   - Total scholarship amount

### Example
Input: Course B24, GPA 4.5
Output: 
```
Оценки: A A A A B B B C C C
Course:    B24
Твой средний балл:    4,50
Стипендия:    7600
```

## Deployment

### System Requirements
- **OS**: Ubuntu 24.04 LTS (recommended) or any modern Linux distribution
- **RAM**: Minimum 256 MB, recommended 512 MB
- **Disk**: Minimum 2 GB free space
- **Docker**: Version 24.0+ 
- **Docker Compose**: Version 2.20+

### Prerequisites Installation

#### 1. Install Docker (Ubuntu 24.04)
```bash
# Add Docker's official GPG key
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to docker group (optional, to run without sudo)
sudo usermod -aG docker $USER
```

#### 2. Verify Installation
```bash
docker --version
docker compose version
```

### Step-by-Step Deployment

#### 1. Clone the Repository
```bash
git clone https://github.com/[your-username]/se-toolkit-hackathon.git
cd se-toolkit-hackathon
```

#### 2. Create Environment File
```bash
cp .env.docker.example .env
```

Edit `.env` file and configure:
```bash
# Required: Get from @BotFather on Telegram
BOT_TOKEN=your_actual_bot_token_here
```

#### 3. Build and Start Services
```bash
docker compose up -d --build
```

#### 4. Verify Deployment
```bash
# Check container status
docker compose ps

# View logs
docker compose logs -f bot
```

#### 5. Test the Bot
Open Telegram, find your bot by username, and send `/start`.

### Management Commands

#### View Logs
```bash
# Real-time logs
docker compose logs -f bot

# Last 100 lines
docker compose logs --tail=100 bot
```

#### Restart Bot
```bash
docker compose restart bot
```

#### Update to Latest Version
```bash
git pull origin main
docker compose down
docker compose up -d --build
```

#### Stop Services
```bash
docker compose down
```

### Troubleshooting

#### Bot doesn't respond
1. Check if container is running: `docker compose ps`
2. Check logs: `docker compose logs bot`
3. Verify BOT_TOKEN is correct
4. Ensure bot has no webhook set: restart container

#### Out of memory
1. Check resource usage: `docker stats`
2. Restart container: `docker compose restart`
3. Consider increasing server RAM

### Architecture

```
se-toolkit-hackathon/
├── src/
│   └── main.py           # Bot entry point and all logic
├── screenshots/          # Demo screenshots
├── Dockerfile            # Container build configuration
├── docker-compose.yml    # Service orchestration
├── .env.docker.example   # Environment variables template
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── LICENSE               # MIT License
└── README.md             # This file
```

### Technology Stack

- **Backend**: Python 3.11, pyTelegramBotAPI
- **Containerization**: Docker, Docker Compose
- **Configuration**: Environment variables with python-dotenv

### Security Considerations

- `.env` file is excluded from git via `.gitignore`
- BOT_TOKEN is loaded from environment variables (never hardcoded)
- Container runs with minimal privileges (non-root user)
- BOT_TOKEN should be rotated if compromised

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Authors

- [Valetova Madina]

### Acknowledgments

- University administration for scholarship formula specifications
- Students who provided feedback during testing
- Open-source community for amazing libraries

---

**Version**: 2.0.0  
**Last Updated**: April 2026  
**Status**: Production Ready ✅
