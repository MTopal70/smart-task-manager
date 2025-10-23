# smart-task-manager

An intelligent task management system that not only stores tasks but also automatically categorizes, prioritizes, and suggests reminders—based on deadlines, content, and user behavior.

## 🔧 Tech Stack
- FastAPI  
- PostgreSQL  
- JWT Authentication  
- Docker & Render Deployment  

## 📦 Features
- REST API mit 3 Kern-Entities (Task, User, Project)  
- JWT-basierter Login & geschützte Endpunkte  
- Datenvalidierung  
- GitHub Actions-ready  
- ENV-basierte Konfiguration  

## 🚀 Setup

```bash
git clone https://github.com/MTopal70/smart-task-manager.git
cd smart-task-manager
cp .env.example .env
docker-compose up --build

📁 Struktur
app/
  ├── main.py
  ├── models/
  ├── routes/
  ├── auth/
  ├── config.py
tests/
.env.example
requirements.txt
docker-compose.yml

📜 License
MIT

🔐 .env.example
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
JWT_SECRET_KEY=your_jwt_secret_key
JWT_ALGORITHM=HS256

📦 requirements.txt
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
python-jose
passlib[bcrypt]
python-dotenv

