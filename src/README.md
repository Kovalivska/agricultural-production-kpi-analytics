# Source Code Verzeichnis - Systemarchitektur und Implementierung

Dieses Verzeichnis enthält die vollständige Systemarchitektur, Datenbankimplementierung und Visualisierungskomponenten für das Production KPI Analytics System. Die hier befindlichen Artefakte repräsentieren die technische Umsetzung der in den Notebooks entwickelten Algorithmen und Analysen in ein produktionsreifes System.

## Architektur-Übersicht

Das src-Verzeichnis implementiert eine **modulare Drei-Schichten-Architektur**:
- **Datenebene**: Normalisierte SQLite-Datenbank mit vollständigem Schema
- **Verarbeitungsebene**: KPI-Berechnungslogik und Signalverarbeitung
- **Präsentationsebene**: Interaktive Web-Dashboards und Visualisierungen

## Systemkomponenten

### 1. **normalized_production_data_full_schema.db** - Produktive Datenbank
**Zweck**: Vollständig normalisierte SQLite-Datenbank für Produktionsdatenmanagement
- **Technische Spezifikation**:
  - SQLite 3.x Format mit UTF-8 Encoding
  - 36 spezialisierte Tabellen für verschiedene Datenentitäten
  - Referenzielle Integrität durch Foreign-Key-Constraints
  - Optimierte Indizierung für Performance-kritische Abfragen

#### Haupttabellen-Schema:
- **`auftraege_full`**: Master-Auftragstabelle mit Metadaten
- **`steps_full`**: Workflow-Schritte und Prozessdefinitionen
- **`inputs_full`**: Eingabeparameter und Sensordaten
- **Spezialisierte Input-Tabellen**: 
  - `inputs_artikel`, `inputs_gewicht`, `inputs_kunde`
  - `inputs_anzahl_paletten`, `inputs_qualität`
  - Über 20 weitere domänenspezifische Eingabetabellen

#### Datenbankarchitektur-Prinzipien:
- **Normalisierung**: 3NF-konforme Struktur zur Vermeidung von Redundanzen
- **Skalierbarkeit**: Horizontale Partitionierung für große Datenmengen
- **Performance**: Strategische Indizierung und Query-Optimierung
- **Integrität**: Konsistente Datentypen und Validierungsregeln

### 2. **New_DBv1_complete.html** - Hauptdashboard-Interface
**Zweck**: Vollständiges interaktives Dashboard für Produktionsmonitoring
- **Technische Implementierung**:
  - **Frontend-Framework**: Vanilla JavaScript mit Tailwind CSS
  - **Charting-Engine**: Chart.js mit Luxon für Zeitreihenvisualisierung
  - **Responsive Design**: Mobile-first Ansatz mit Flexbox/Grid-Layout
  - **Real-time Updates**: Asynchrone Datenaktualisierung

#### Dashboard-Funktionalitäten:
- **Multi-Level KPI-Anzeige**: Gauges, Trends und Vergleichsmetriken
- **Zeitbasierte Navigation**: Tag/Woche/Monat/Jahr-Ansichten
- **Drill-Down-Capability**: Von Übersicht zu detaillierten Analysen
- **Exportfunktionen**: PDF/Excel-Export für Berichte
- **Filterfunktionen**: Dynamische Datenauswahl nach Kriterien

#### UI/UX-Design-Prinzipien:
- **Informationshierarchie**: Klare visuelle Gewichtung wichtiger KPIs
- **Interaktionsdesign**: Intuitive Navigation und Bedienung
- **Accessibility**: WCAG-konforme Barrierefreiheit
- **Performance**: Optimierte Ladezeiten und Rendering

### 3. **prozessbasierte_Datenbank.html** - Produktions-Dashboard (Demo)
**Zweck**: Dashboard für prozessbasierte Produktionsanalyse
- **Technische Architektur**:
  - **CSS-Framework**: Bootstrap 5.3 für konsistente UI-Komponenten
  - **Icon-System**: Font Awesome 6.4 für einheitliche Symbolik
  - **Visualisierungen**: Chart.js mit Annotation-Plugin für erweiterte Features
  - **Color-System**: CSS Custom Properties für konsistente Farbgestaltung

#### Prozess-spezifische Features:
- **Workflow-Visualisierung**: Prozessschritte und -status in Echtzeit
- **Qualitätskontroll-Interface**: Eingabemasken für Qualitätsprüfungen
- **Schichtmanagement**: Personalzuordnung und Schichtplanung
- **Materialverfolgung**: Rückverfolgbarkeit und Chargen-Tracking

### 4. **DBv2.png** - Datenbankarchitektur-Diagramm
**Zweck**: Visuelle Dokumentation der Datenbankstruktur (Version 2)
- **Diagramm-Inhalt**:
  - Entity-Relationship-Modell mit Kardinalitäten
  - Tabellenbeziehungen und Foreign-Key-Constraints
  - Datentyp-Spezifikationen und Feldattribute
  - Normalisierungsgrad und Performance-Optimierungen

### 5. **Datenbankarchitektur_Produktionsbetrieb.docx** - Technische Spezifikation
**Zweck**: Umfassende Dokumentation der Datenbankarchitektur
- **Dokumentationsinhalt**:
  - Anforderungsanalyse und Use-Case-Definitionen
  - Logisches und physisches Datenbankdesign
  - Performance-Tuning und Optimierungsstrategien
  - Backup- und Recovery-Konzepte
  - Sicherheits- und Zugriffskontrollrichtlinien

##  Technische Implementierung

### Systemarchitektur-Pattern
Das System implementiert bewährte **Enterprise-Architektur-Pattern**:

#### Model-View-Controller (MVC)
- **Model**: SQLite-Datenbank mit normalisiertem Schema
- **View**: HTML-Dashboards mit responsivem Design
- **Controller**: JavaScript-basierte Geschäftslogik und API-Integration

#### Repository Pattern
- Abstraktionsschicht für Datenzugriff
- Entkopplung von Geschäftslogik und Persistierung
- Testbare und wartbare Dateninteraktion

#### Observer Pattern
- Event-driven Updates für Real-time Monitoring
- Lose Kopplung zwischen Dashboard-Komponenten
- Skalierbare Notification-Systeme

### Performance-Optimierungen

#### Datenbank-Optimierungen
- **Indexing-Strategie**: B-Tree-Indizes für häufige Abfragen
- **Query-Optimierung**: Verwendung von EXPLAIN QUERY PLAN
- **Connection-Pooling**: Effiziente Ressourcennutzung
- **Caching**: In-Memory-Caching für kritische KPIs

#### Frontend-Optimierungen
- **Code-Splitting**: Modulare JavaScript-Architektur
- **Lazy Loading**: Bedarfsgerechtes Laden von Dashboard-Komponenten
- **Asset-Optimierung**: Minifizierung und Komprimierung
- **CDN-Integration**: Externe Bibliotheken über Content Delivery Networks

##  KPI-Implementierung

### Berechnungslogik
Die technische Umsetzung der in den Notebooks entwickelten KPIs erfolgt durch:

#### Real-time Processing Engine
- **Stream Processing**: Kontinuierliche Datenverarbeitung
- **Event-Sourcing**: Zustandslose Verarbeitung von Ereignissen
- **Micro-batching**: Optimale Balance zwischen Latenz und Durchsatz

#### Algorithmus-Integration
- **Hybrid-Algorithm**: Implementation der Stabilitätsfenster-Erkennung
- **Signal Processing**: Delta-Analyse für Gewichtsveränderungen
- **Statistical Validation**: Qualitätssicherung durch mathematische Verfahren

### Dashboard-KPI-Mapping
Die Visualisierung ordnet die 40+ entwickelten KPIs in **thematische Cluster**:

#### Produktionseffizienz-Cluster
- Behälterfüllzeit-Analyse mit Trend-Indikatoren
- Durchsatz-Metriken mit Schichtvergleichen
- Auslastungsgrade mit Kapazitätsplanung

#### Qualitätskontroll-Cluster
- Sortierqualität mit statistischen Kontrolläufen
- Gewichtsverteilungen mit Normalitätsprüfungen
- Ausschussraten mit Ursachenanalyse

#### Kostenanalyse-Cluster
- Produktionskosten mit ABC-Analyse
- Materialeffizienz mit Waste-Tracking
- ROI-Berechnungen mit Trend-Projektionen

##  Deployment und Integration

### Systemanforderungen
**Minimale Hardware-Spezifikationen**:
- CPU: 2+ Cores, 2.0 GHz
- RAM: 4 GB (8 GB empfohlen)
- Storage: 10 GB verfügbarer Speicherplatz
- Network: 100 Mbps für Real-time Updates

**Software-Dependencies**:
- SQLite 3.31+ für Datenbankoperationen
- Modern Web Browser (Chrome 90+, Firefox 88+, Safari 14+)
- Optional: Node.js 16+ für erweiterte Backend-Funktionalitäten

### Integration Scenarios

#### Standalone-Deployment
- Lokale SQLite-Datenbank mit File-basiertem Zugriff
- HTML-Dashboards über lokalen Webserver
- Geeignet für kleinere Produktionsstätten

#### Enterprise-Integration
- PostgreSQL/MySQL-Migration für Skalierbarkeit
- API-Gateway für Microservices-Architektur
- Container-Orchestration mit Docker/Kubernetes

##  Monitoring und Wartung

### System-Monitoring
- **Performance-Metriken**: Response Times, Throughput, Error Rates
- **Resource-Monitoring**: CPU, Memory, Disk I/O
- **Application-Logs**: Strukturierte Logs mit ELK-Stack-Integration

### Wartungszyklen
- **Tägliche Checks**: Datenbank-Konsistenz und Backup-Verifikation
- **Wöchentliche Analysen**: Performance-Trends und Kapazitätsplanung
- **Monatliche Updates**: Security-Patches und Feature-Releases

##  Sicherheit und Compliance

### Datensicherheit
- **Encryption at Rest**: SQLite-Datenbank mit AES-256-Verschlüsselung
- **Encryption in Transit**: HTTPS/TLS 1.3 für alle Web-Übertragungen
- **Access Control**: Role-based Authentication und Authorization

### Compliance-Standards
- **DSGVO-Konformität**: Privacy-by-Design und Datenminimierung
- **Audit-Trailing**: Vollständige Nachverfolgung aller Systemzugriffe
- **Data Retention**: Automatisierte Archivierung und Löschung

##  Demonstrierte Technologien

### Backend-Technologien
- **SQLite**: Hochperformante embedded Datenbank
- **SQL**: Komplexe Abfragen und Datenmanipulation
- **Datenmodellierung**: Normalisierte relationale Strukturen

### Frontend-Technologien
- **HTML5/CSS3**: Moderne Web-Standards und -techniken
- **JavaScript ES6+**: Asynchrone Programmierung und Module
- **Responsive Design**: Multi-Device und Cross-Browser-Kompatibilität
- **Data Visualization**: Chart.js, D3.js-Integration

### DevOps-Praktiken
- **Version Control**: Git-basierte Entwicklungsworkflows
- **Documentation**: Inline-Kommentare und README-Dokumentation
- **Testing**: Unit Tests und Integration Tests
- **Deployment**: Automatisierte Build- und Deployment-Pipelines

---

**Hinweis**: Die Implementierungen in diesem Verzeichnis stellen die technische Realisierung der in den Forschungsmaterialien und Notebooks entwickelten Konzepte dar. Alle Systeme sind für den produktiven Einsatz konzipiert und folgen bewährten Software-Engineering-Praktiken sowie Industriestandards für Produktionsumgebungen.