<<<<<<< HEAD
# Autonomous GTM Support-to-Sales Triage Engine

## Overview
A production-grade Python and PostgreSQL microservice designed to automate outbound sales generation. The pipeline queries local relational state for high-intent accounts and leverages Google's Gemini AI SDK to dynamically draft personalized cold outreach, updating database states asynchronously.

## Architecture
- **Database Layer:** PostgreSQL 18 running locally via Postgres.app (`gtm_engine`) managing customer interactions and outbound prospects.
- **Orchestration Layer:** Python 3 asynchronous execution loop handling database connection states via `psycopg2`.
- **AI Engine:** Google Gemini SDK (`gemini-3.8-flash`) utilizing robust retry logic and exponential backoff to handle high-demand network states.
- **Security:** Strict environment variable isolation utilizing `python-dotenv` and `.gitignore` protocols.

## Database Schema (`outbound_prospects`)
| Column Name | Data Type | Constraints / Defaults |
| :--- | :--- | :--- |
| `lead_id` | SERIAL | PRIMARY KEY |
| `company_name` | VARCHAR(100) | - |
| `decision_maker` | VARCHAR(100) | - |
| `intent_score` | INT | DEFAULT 0 |
| `outreach_status` | VARCHAR(50) | DEFAULT 'Pending' |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## Setup & Execution

### 1. Environment Configuration
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_actual_api_key_here

=======
# Autonomous GTM Engine: PostgreSQL + Gemini AI

## The Problem
Business Development Executives (BDEs) lose over 60% of their operational bandwidth manually context-switching between database metrics, intent tracking, and writing bespoke cold outreach emails. 

## The Solution
An asynchronous, lightweight Python microservice that queries a local PostgreSQL database for uncontacted, high-intent accounts and orchestrates Google’s Gemini AI SDK to dynamically generate personalized outbound copy.

## Architecture & Data Flow
1. **Database Layer:** PostgreSQL instance (`gtm_engine`) running locally via Postgres.app on port `5432`. Stores customer interaction logs and target outbound accounts (`outbound_prospects`).
2. **Orchestration Layer:** Python 3 script utilizing `psycopg2` for transactional database communication and safe connection parameters.
3. **AI Generation Layer:** Uses the modern `google-genai` SDK (`gemini-3.8-flash`) with integrated exponential backoff to automatically handle network and rate-limit friction (`503 High Demand`).
4. **Security Layer:** Environment credentials are strictly isolated using `python-dotenv` and protected from version control exposure via `.gitignore`.

## Setup & Execution

### 1. Environment Configuration
Create a `.env` file in the root directory and add your Google AI Studio API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
>>>>>>> 38fadfe (chore: finalize production-ready agent and documentation)
