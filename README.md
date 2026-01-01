# Smart Homework AI Study Planner 🧠📚

An intelligent, multi-agent AI system that creates personalized, balanced study plans for students. Built with **CrewAI**, **FastAPI**, **React**, and **Docker**.

![Status](https://img.shields.io/badge/Status-Active-success)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![AI](https://img.shields.io/badge/AI-Ollama%20%2B%20CrewAI-purple)

## 🌟 Features

- **Multi-Agent Collaboration**: Four specialized AI agents work together to plan, schedule, balance, and motivate.
- **Personalized Planning**: Takes into account assignments, deadlines, and daily available hours.
- **Well-Being Focused**: Automatically schedules breaks and prevents burnout by balancing daily workload.
- **Local Private LLM**: Uses a local **Ollama** instance running `gemma3:1b` for privacy and cost-efficiency.
- **Premium UI**: Modern, glassmorphism-inspired interface built with React and Vanilla CSS.

## 🏗 Architecture

### AI Agents (CrewAI)
1. **🤖 Planner Agent**: Breaks down assignments into manageable study sessions.
2. **⏳ Time Management Agent**: Estimates durations and distributes workload across the week.
3. **🧘 Focus & Well-Being Agent**: Ensures breaks are included and workload is age-appropriate.
4. **🧠 Motivation Agent**: Adds encouraging notes and study tips.

### Tech Stack
- **Frontend**: React + Vite (Custom Premium CSS)
- **Backend**: Python FastAPI
- **Orchestration**: CrewAI + LangChain
- **LLM**: Ollama (gemma 3:1b)
- **Database**: PostgreSQL
- **Infrastructure**: Docker Compose

## 🚀 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

### Installation & Running

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd smart-homework-ai-study-planner
   ```

2. **Start the application with Docker Compose**:
   ```bash
   docker compose up --build
   ```
   > **Note**: The first run will take a few minutes as it pulls the Postgres image, builds the services, and downloads the `gemma3:1b` model (approx. 2GB) inside the Ollama container.

3. **Verify Services**:
   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Ollama: [http://localhost:11434](http://localhost:11434)

## 📖 Usage Guide

1. Open the **Frontend** at `http://localhost:5173`.
2. Enter your assignments in natural language.
   - *Example: "Math Midterm on Friday, History Essay due Tuesday, read Chapter 4 for Science."*
3. Set your **Daily Study Hours** (e.g., 2 hours/day).
4. Click **Generate Plan**.
5. Watch the **Agent Status** badges pulse as the AI team works on your plan.
6. View your **Weekly Schedule**, complete with breaks and motivational tips!

## 🔧 Troubleshooting

- **Ollama Model Not Found**: If the planner fails or hangs, the model might not have pulled correctly. Run this command manually while the containers are running:
  ```bash
  docker compose exec ollama ollama pull gemma3:1b
  ```
- **Port Conflicts**: Ensure ports `5173` (Frontend), `8000` (Backend), and `5432` (Postgres) are free.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
