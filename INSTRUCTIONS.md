# 🚀 Инструкция по публикации на GitHub

## ✅ Что готово

Проект обновлён и готов к публикации:
- ✅ Код бота обновлён (твоя версия)
- ✅ TOKEN берётся из .env файла (НЕ захаркожен!)
- ✅ Python синтаксис валиден
- ✅ Docker конфигурация упрощена
- ✅ Документация обновлена
- ✅ .gitignore настроен (исключает .env)

## 📋 Структура проекта

```
se-toolkit-hackathon/
├── src/
│   └── main.py              # Весь код бота
├── scripts/
│   ├── start.sh             # Запуск
│   ├── stop.sh              # Остановка
│   └── restart.sh           # Перезапуск
├── screenshots/             # Скриншоты (заглушки)
├── .github/workflows/
│   └── ci-cd.yml            # CI/CD pipeline
├── Dockerfile               # Docker
├── docker-compose.yml       # Docker Compose
├── .env.docker.example      # Шаблон .env
├── .gitignore
├── LICENSE                  # MIT
├── README.md                # Документация
├── requirements.txt         # Зависимости
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── SECURITY.md
```

## 🔥 ВАЖНО: TOKEN БОТА

**НИКОГДА не публикуй TOKEN в GitHub!**

Твой TOKEN: `8216167493:AAFtwhHUW2C7_uFTa6RxyAShCC6wR-CB068`

**НЕ ПИШИ ЕГО В КОД!** Он должен быть только в `.env` файле на сервере.

## 📤 Шаги публикации

### 1. Создай репозиторий

1. Открой https://github.com/new
2. Repository name: `se-toolkit-hackathon`
3. Описание: `Telegram bot that calculates academic scholarships`
4. **Public** репозиторий
5. **НЕ инициализируй** с README, .gitignore, license
6. Нажми **Create repository**

### 2. Загрузи код

Открой терминал/командную строку:

```bash
cd "C:\Users\User\Desktop\set govno\se-toolkit-hackathon"

# Инициализация Git
git init

# Добавь все файлы
git add .

# Проверь что будет закоммичено
git status

# Коммит
git commit -m "feat: Version 2.0.0 - Scholarship Calculator Bot

Features:
- Bilingual support (Russian/English)
- Multiple course support (B23-B25, M25)
- GPA input as numbers or letter grades
- Official scholarship formula
- Bonus system for achievements
- Docker containerization
- Secure token handling via environment variables"

# Добавь remote (ЗАМЕНИ YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/se-toolkit-hackathon.git

# Загрузи на GitHub
git push -u origin main
```

### 3. Проверь репозиторий

После загрузки проверь:
- [ ] Все файлы видны на GitHub
- [ ] README.md красиво отображается
- [ ] **НЕТ файла .env** (он в .gitignore)
- [ ] **НЕТ TOKEN в коде**
- [ ] LICENSE есть

### 4. Добавь topics

На странице репозитория:
1. Нажми ⚙️ рядом с "About"
2. Добавь topics:
   - `telegram-bot`
   - `scholarship`
   - `python`
   - `docker`
   - `education`

## 🎯 Как TA будет тестировать

```bash
# 1. Клонировать
git clone https://github.com/YOUR_USERNAME/se-toolkit-hackathon.git
cd se-toolkit-hackathon

# 2. Создать .env
cp .env.docker.example .env
# Редактировать .env и добавить BOT_TOKEN

# 3. Запустить
docker compose up -d --build

# 4. Тестировать в Telegram
# /start -> START -> выбрать язык -> курс -> GPA -> результат
```

## 📝 Основные функции

### Что реализовано ✅
- bilingual (RU/EN)
- ввод GPA числами или буквами (A, B, C, D)
- автоматический расчёт стипендии по формуле
- бонусы за отличную учёбу и конкурсы
- START/STOP кнопки
- новый расчёт после результата

### Формула расчёта
```
S = min + (max - min) * ((G - 2) / 3)^2.5
```

Где:
- `min` = 3000 (минимальная стипендия)
- `max` = 10000 (бакалавр) или 20000 (магистр)
- `G` = GPA (2.0-5.0)

### Бонусы
- +10,000₽ - все пятёрки 2 семестра подряд
- +6,000₽ - победа в конкурсе
- +12,000₽ дополнительно для бюджетников

## 🔧 Деплой на сервер (Ubuntu 24.04)

```bash
# Установить Docker
curl -fsSL https://get.docker.com | sh

# Клонировать репозиторий
git clone https://github.com/YOUR_USERNAME/se-toolkit-hackathon.git
cd se-toolkit-hackathon

# Создать .env
cp .env.docker.example .env
nano .env  # Добавить свой BOT_TOKEN

# Запустить
docker compose up -d --build

# Проверить
docker compose logs -f
```

## ⚠️ Чек-лист перед отправкой

- [ ] Репозиторий создан на GitHub
- [ ] Код загружен
- [ ] README.md отображается правильно
- [ ] **TOKEN НЕ в коде** (только в .env)
- [ ] .env **НЕ** в репозитории
- [ ] LICENSE есть
- [ ] Topics добавлены
- [ ] Могу склонировать и запустить с нуля

## 🆘 Если что-то пошло не так

### Git push не работает
```bash
# Если репозиторий уже создан с README
git pull origin main --allow-unrelated-histories
git push origin main
```

### TOKEN утечёт в GitHub
1. **СРОЧНО** зайди в @BotFather
2. Отправь `/revoke`
3. Выбери своего бота
4. Получи новый TOKEN
5. Обнови .env

---

**Успехов! 🎓🚀**
