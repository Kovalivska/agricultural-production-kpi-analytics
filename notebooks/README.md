# Notebooks Verzeichnis - Landwirtschaftliche Produktions-KPI-Analytik

Dieses Verzeichnis enthält Jupyter Notebooks für die umfassende Analyse von über 40 Key Performance Indicators (KPIs) zur Optimierung der landwirtschaftlichen Produktion. Das Projekt wurde während eines Praktikums bei Data Coffee GmbH (Juni 2025 - September 2025) als Teil eines Spezialisierungsprogramms für Signalverarbeitung und Zeitreihenanalyse entwickelt.

## 📊 Notebook-Übersicht

### 1. **KPIs_real_data.ipynb** - Hauptanalyse-Notebook
Das zentrale Analysedokument mit 139 Zellen, das eine vollständige Implementierung von 40+ Produktionseffizienz-KPIs enthält:

#### Kerninhalt:
- **Datenimport und Vorverarbeitung**: Sensordatenaufbereitung von landwirtschaftlichen Geräten
- **Explorative Datenanalyse (EDA)**: Statistische Untersuchung der Gewichtssensordaten  
- **KPI-Berechnungsframework**: Implementierung von Produktivitäts-, Qualitäts- und Effizienzmetriken
- **Signalverarbeitung**: Erweiterte Algorithmen zur Rauschfilterung und Anomalieerkennung
- **Zeitreihenanalyse**: Trendidentifikation und statistische Modellierung
- **Visualisierung**: Interaktive Dashboards für Management-Insights

#### Analysierte KPIs umfassen:
- **Produktionseffizienz**: Behälterfüllzeit, Durchsatz pro Schicht, Gewichtsabweichungen
- **Qualitätskontrolle**: Sortierqualität, Gewichtsverteilung, Verlustanalyse
- **Kostenanalyse**: Kosten pro Einheit, Produktionsökonomie, Abfallminimierung
- **Mitarbeiterproduktivität**: Stückzahl/Stunde, Kilogramm/Stunde
- **OEE-Komponenten**: Verfügbarkeit, Leistung, Qualitätsrate

### 2. **JSON__into_SQLite_DB.ipynb** - Datenbank-Integration
79 Zellen zur Datenbankarchitektur und SQL-Integration:
- JSON-Datenkonvertierung in SQLite-Datenbank
- Normalisierung der Produktionsdaten
- SQL-Query-Optimierung für KPI-Berechnungen
- Datenbankschema-Design für Zeitreihendaten

### 3. **JSON_in_SQLite_25_06.ipynb** - Erweiterte Datenbankoperationen
Spezialisierte Datenbankoperationen und Datenmigration

### 4. **Json_into_csv_and_db_eda.ipynb** - Datenkonvertierung und EDA
50 Zellen für:
- JSON zu CSV Konvertierung
- Explorative Datenanalyse der Rohdaten
- Datenqualitätsprüfung und Validierung
- Statistische Grundauswertungen

##  Technische Methodik

### Hybrid-Algorithmus-Ansatz
Die Notebooks implementieren einen sophistizierten Hybrid-Algorithmus:
- **Stabilitätsfenster-Erkennung**: Identifikation stabiler Gewichtszustände
- **Delta-Analyse**: Gewichtsveränderungen zur Stückzählung
- **Statistische Validierung**: Datenqualität und Genauigkeitssicherung

### Signalverarbeitungs-Pipeline
1. **Datenvorverarbeitung**: Rauschreduktion und Signalbereinigung
2. **Merkmalextraktion**: Identifikation relevanter Muster
3. **Statistische Analyse**: Trendanalyse und Anomalieerkennung
4. **Echtzeitverarbeitung**: Kontinuierliche Überwachungsfähigkeiten

##  Verwendete Technologien

- **Python-Bibliotheken**: Pandas, NumPy, Matplotlib, Seaborn, SciPy
- **Datenbanktechnologien**: SQL/SQLite, InfluxDB für Zeitreihendaten
- **Statistische Analyse**: Zeitreihenzerlegung, Signalfilterung, Anomalieerkennung
- **Visualisierung**: Plotly, Matplotlib für interaktive Dashboards
- **Datenverarbeitung**: Signalverarbeitungsalgorithmen, statistische Modellierung

##  Wichtige Errungenschaften

- **40+ implementierte KPIs**: Umfassendes Produktionsüberwachungssystem
- **Echtzeitverarbeitung**: Sub-Sekunden-Antwortzeiten für kritische Metriken
- **95%+ Genauigkeit**: Hohe Präzision bei Messung und Berechnung
- **Skalierbare Architektur**: Verarbeitung mehrerer Produktionslinien
- **Automatisierte Berichterstattung**: Reduzierung manueller Analysen um 80%

##  Technische Innovationen

### Erweiterte Signalverarbeitung
- Dynamische Gewichtsplateau-Erkennung
- Adaptive Schwellenwert-Algorithmen
- Rauschresistente Messtechniken
- Echtzeit-Anomalie-Identifikation

### Statistische Modellierung
- Zeitreihenprognose
- Prozessfähigkeitsanalyse
- Qualitätskontroll-Charting
- Prädiktive Wartungsindikatoren

##  Erste Schritte

1. **Umgebung einrichten**: 
   ```bash
   pip install pandas numpy matplotlib seaborn scipy plotly jupyter
   ```

2. **Hauptanalyse starten**:
   Öffnen Sie `KPIs_real_data.ipynb` für die vollständige KPI-Analyse

3. **Datenbankintegration**:
   Verwenden Sie `JSON__into_SQLite_DB.ipynb` für Datenbankoperationen

##  Hinweise zur Datensicherheit

- Alle firmenspezifischen Identifikatoren wurden anonymisiert
- Sensible Produktionsdaten wurden generalisiert
- Nur methodische Ansätze werden demonstriert
- Keine vertraulichen Geschäftsinformationen enthalten

##  Demonstrierte Fähigkeiten

- Erweiterte Datenanalyse und Visualisierung
- Signalverarbeitung und Zeitreihenanalyse
- Statistische Modellierung und Hypothesentests
- Datenbankdesign und -optimierung
- Dashboard-Entwicklung und Berichterstattung
- Prozessoptimierung und Effizienzanalyse

---

**Hinweis**: Diese Notebooks demonstrieren technische Fähigkeiten in der landwirtschaftlichen Datenanalytik, die während professioneller Praktikumserfahrung entwickelt wurden. Alle Daten wurden angemessen anonymisiert, während analytische Methodik und technische Implementierungsdetails erhalten blieben.