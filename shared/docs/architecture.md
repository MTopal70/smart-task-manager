# Architekturübersicht – Smart Task Manager

## Ziel
Ein intelligentes Task-Management-System mit REST API, JWT-Auth und PostgreSQL, das später durch KI-gestützte Funktionen erweitert werden kann.

## Komponentenübersicht

- **Backend (FastAPI)** – REST API mit Authentifizierung, Validierung und Datenlogik
- **Datenbank (PostgreSQL)** – Speicherung von Tasks, Usern und Projekten
- **Auth (JWT)** – Login, Token-Handling, geschützte Endpunkte
- **Deployment (Render)** – Containerisierte Bereitstellung mit ENV-Variablen
- **Dokumentation (GitHub)** – Architektur, API-Spezifikation, Setup

## Verzeichnisstruktur
smart-task-manager/ ├── dev-mac/       # FastAPI-Backend ├── dev-win/       # .NET-Komponenten (später) ├── shared/docs/   # Dokumentation


## Datenfluss (MVP)

1. User sendet Login-Request → JWT wird generiert
2. Authentifizierter User ruft `/tasks` auf
3. FastAPI verarbeitet Request, validiert Daten
4. PostgreSQL liefert oder speichert Daten
5. Antwort wird als JSON zurückgegeben
