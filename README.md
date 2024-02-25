# Vocabify

## Über das Projekt

Vocabify ist ein Vokabeltrainer nach dem Leitner-System für effektives Wiederholungstraining im Rahmen der Facharbeit Q1.2 GSM entwickelt wurde.

## Ordner-Struktur
    ├── Nuxt-Webseite/                  # Ordner für die Nuxt.js-Webanwendung
        ├── assets/css/main.scss        # Globale CSS-Datei für die Webanwendung
        ├── components/                 # Wiederverwendbare Vue.js-Komponenten
            ├── BoxSnaek.vue            # Komponente für eine Box-Snake-Ansicht
            ├── Nav.vue                 # Navigationskomponente
            └── Words.vue               # Komponente für Wörteransicht
        ├── pages/                      # Seiten der Webanwendung
            ├── box-edit/[id].vue       # Seite zur Bearbeitung einer Box mit dynamischer ID
            ├── box/[id].vue            # Seite zur Anzeige einer Box mit dynamischer ID
            ├── learn/[id].vue          # Seite zum Lernen mit dynamischer ID
            ├── index.vue               # Startseite
            ├── login.vue               # Login-Seite
            └── register.vue            # Registrierungsseite
        ├── public/...                  # Öffentliche Dateien und Ressourcen
        ├── server/...                  # Serverseitiger Code
        ├── README.md                   # Dokumentation und Anweisungen zum Projekt
        ├── .gitignore                  # Git-Konfigurationsdatei, um bestimmte Dateien zu ignorieren
        ├── .npmrc                      # Konfigurationsdatei für npm
        ├── app.vue                     # Haupt-Vue.js-Datei für die Webanwendung
        ├── nuxt.config.ts              # Konfigurationsdatei für Nuxt.js
        ├── package-lock.json           # Datei, die alle installierten Pakete mit ihren Versionen festhält
        ├── package.json                # Liste der benötigten Pakete und deren Versionen
        └── tsconfig.json               # Konfigurationsdatei für TypeScript
    ├── Python-Skript/                  # Ordner für das Python-Skript zur Berechnung von Markov-Ketten
        ├── Simulation.py               # Python-Skript für die Simulation
        └── .gitignore                  # Git-Konfigurationsdatei, um bestimmte Dateien zu ignorieren
    └── Beispiel Vokabeln.csv           # CSV-Datei mit Beispielvokabeln


## Installation

Folgen Sie diesen Schritten, um das Projekt auf Ihrem lokalen System zu installieren:

1. Klonen Sie dieses Repository: `git clone https://github.com/fabianskutta/Vocabify.git`

2. Installieren Sie Node.js: [Node.js herunterladen](https://nodejs.org/en/download/current)

3. Navigieren Sie in den Ordner der Nuxt-Webseite: `cd .\Nuxt-Webseite\`

4. Installieren Sie die Abhängigkeiten: `npm install`

## Ausführen

1. Starten Sie den Entwicklungsserver: `npm run dev`
2. Der lokale Server ist nun erreichbar unter: [http://localhost:3000](http://localhost:3000)
