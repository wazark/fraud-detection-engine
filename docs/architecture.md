# 🏗️ System Architecture

## 📌 Overview

The Fraud Detection Engine is designed as a modular and scalable system, separating responsibilities between client-side processing, detection logic, and backend services.

The goal is to ensure:
- Performance (fast local analysis)
- Scalability (backend-driven intelligence)
- Security (controlled exposure of detection logic)
- Maintainability (modular components)

---

## 🧠 High-Level Architecture

```text
            ┌──────────────────────┐
            │   Mobile Application │
            │      (Flutter)       │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │  Local Detection     │
            │      Engine          │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │   Backend Services   │
            │  (APIs & Scoring)    │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │ External Intelligence│
            │ (Threat APIs, Lists) │
            └──────────────────────┘