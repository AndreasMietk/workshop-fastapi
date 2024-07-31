# Workshop: Software Architecture
## Setup 
Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

Lokalen development server starten

```bash
fastapi dev main.py
```

## Einrichten eines neuen Tech-Stacks

### Aufgabe 1: Implementierung eines ORMs und einer Datenbank zur Persistenz von Modellen

- Richte eine Datenbank ein (z.B. SQLite), um unsere Modelle zu speichern.
- Wähle ein ORM (z.B. SQLAlchemy) zur Interaktion mit der Datenbank.
- Definiere die Modellschemata mithilfe des ORMs.

### Aufgabe 2: Erstellung eines Migrationsskripts zur Initialisierung der Tabelle für unser Modell

- Schreibe ein Skript, das das Migrationswerkzeug des ORMs verwendet, um die notwendige(n) Tabelle(n) in der Datenbank zu erstellen.
- Installiere ein Migrationswerkzeug (z.B. Alembic bei Verwendung von SQLAlchemy).
- Erstelle ein Migrationsskript, das die Tabellenstruktur basierend auf dem ORM-Modell definiert.
- Führe das Migrationsskript aus, um die Änderungen an der Datenbank anzuwenden.

## Zusatz: Implementierung der API-Endpunkte

### Aufgabe 1: Implementierung des "store" API-Endpunkts zum Speichern von Modellen

- Erstelle einen Endpunkt, der es Clients ermöglicht, neue Instanzen des Modells in der Datenbank zu speichern.
- Implementiere die Logik zum Speichern der validierten Daten als neue Modellinstanz in der Datenbank.
- Gebe eine angemessene Antwort zurück (z.B. anzeigen des Templates mit der Route in der Karte).

### Aufgabe 2: Implementierung der "index" API-Endpunkte zum Abrufen von Modellen

- Erstelle Endpunkte, um alle Modelle oder ein einzelnes Modell anhand seiner ID aus der Datenbank abzurufen.
- Definiere die Routen (z.B. `GET /routes` für alle Modelle und `GET /routes/{route_id}` für ein einzelnes Modell).
