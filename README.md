# se-toolkit-hackathon
# Scholarship Calculator Bot 🎓

Telegram bot that calculates academic scholarships based on GPA, course level, and personal achievements.

## Demo

![Bot Start Screen](screenshots/start.png)
![Course Selection](screenshots/course.png)
![GPA Input](screenshots/gpa.png)
![Result Screen](screenshots/result.png)

## Product Context

### End Users
- University students (Bachelor's and Master's programs)
- Academic advisors
- Scholarship administrators

### Problem Solved
Students struggle to estimate their potential scholarship amount due to complex calculation formulas involving:
- GPA conversion (2.0-5.0 scale)
- Course level differences (Bachelor vs Master)
- Bonus conditions (all A's for two semesters, competition wins, state funding status)

### Solution
A Telegram bot that:
- Takes GPA as numbers or letter grades (A, B, C, D)
- Applies the official formula: `S = min + (max - min) * ((G - 2) / 3)^2.5`
- Rounds down to hundreds as per university policy
- Adds bonuses: +10,000₽ for all A's, +6,000₽ for competition wins, +12,000₽ for state-funded winners
- Returns instant, accurate scholarship calculations

## Features

### Implemented ✅
- Bilingual support (Russian/English)
- Multiple course support (B23, B24, B25, M25)
- GPA input as numbers (2.0-5.0) or letter grades (A, B, C, D)
- Automatic GPA calculation from letter grades
- Scholarship calculation with formula exponentiation
- Round-down to hundreds
- Bonus system (all A's, competition wins, state funding)
- Conversation flow with YES/NO questions
- START/STOP bot controls

### Not Yet Implemented 🔜
- Database storage for user history
- Admin panel for modifying bonus amounts
- Export calculations as PDF
- Comparison with previous semester calculations
- Multi-student batch calculation

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
   - Converted letter grades (10 subjects)
   - Course level
   - GPA value
   - Total scholarship amount

### Example
Input: Course B24, GPA 4.5
Output: Grades: A A A A B B B C C C
Course: B24
GPA: 4.50
Scholarship: 7600
