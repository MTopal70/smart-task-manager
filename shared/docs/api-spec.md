# API-Spezifikation – Smart Task Manager (MVP)

## Auth

### POST `/login`
- **Body:** `{ "username": "string", "password": "string" }`
- **Returns:** `{ "access_token": "JWT", "token_type": "bearer" }`

---

## Tasks

### GET `/tasks`
- **Auth:** Bearer Token
- **Returns:** Liste aller Tasks des Users

### POST `/tasks`
- **Body:** `{ "title": "string", "description": "string", "due_date": "ISO8601" }`
- **Returns:** Neuer Task

---

## Users

### POST `/users`
- **Body:** `{ "username": "string", "email": "string", "password": "string" }`
- **Returns:** Neuer User

---

## Projekte (optional für MVP)

### GET `/projects`
- **Returns:** Alle Projekte des Users
