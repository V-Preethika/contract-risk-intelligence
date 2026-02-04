⚖️ Contract Risk Intelligence



Multilingual AI-Powered Contract Analysis \& Risk Assessment System for SMEs



📌 Overview



Small and Medium Enterprises (SMEs) often sign legal contracts without fully understanding hidden risks, ambiguous clauses, or unfavorable terms due to complex legal language and lack of legal expertise.



Contract Risk Intelligence is a multilingual, explainable legal AI system that helps SMEs understand contracts in plain language, identify legal risks, and make informed decisions before signing.



The system analyzes contracts uploaded in common formats and provides structured insights such as risk scoring, clause explanations, ambiguity detection, and multilingual summaries.



🎯 Problem Statement



Legal contracts are lengthy and difficult for non-legal users to interpret.



SMEs lack access to in-house legal counsel.



Language barriers further reduce contract comprehension.



Hidden risks such as indemnity, penalties, and unilateral termination often go unnoticed.



✅ Solution



This project provides a rule-based, explainable, and multilingual contract analysis platform that:



Breaks contracts into readable clauses



Flags legal risks and ambiguous language



Explains issues in plain business language



Supports Hindi and extensible multilingual output



Maintains transparency without relying on external legal databases



🧠 Key Features

🔹 Contract Processing



Upload PDF, DOCX, or TXT contracts



Automatic language detection



Hindi → English normalization for internal analysis



🔹 Clause \& Risk Analysis



Robust clause and sub-clause extraction



Detection of unfavorable clauses:



Indemnity clauses



Penalty clauses



Unilateral termination



Non-compete clauses



Auto-renewal clauses



Clause-level severity scoring



Composite contract risk score (LOW / MEDIUM / HIGH)



🔹 Explainable Legal Insights



Plain-language explanations for each risk



Suggested renegotiation alternatives



Clause-by-clause display with expandable details



🔹 Entity Extraction (NER-Lite)



Parties involved



Dates



Financial amounts



Jurisdiction references



Contract duration



🔹 Ambiguity Detection



Flags vague or subjective terms such as:



“reasonable efforts”



“sole discretion”



“from time to time”



Helps reduce future disputes



🔹 Multilingual Output



Output available in English and Hindi



Clause translation handled safely at the UI layer



Architecture supports easy addition of more languages



🔹 Audit Logging



Tracks analyzed contracts and risk levels



Maintains local audit history for traceability



🧩 Architecture Overview

├── app.py                     # Streamlit UI

├── core/

│   ├── contract\_loader.py     # File extraction

│   ├── clause\_splitter.py     # Clause parsing

│   ├── risk\_engine.py         # Risk detection \& scoring

│   ├── entity\_extractor.py    # Entity extraction (NER-lite)

│   ├── ambiguity\_detector.py  # Ambiguity detection

│   ├── multilingual.py        # Language handling \& translation

│   ├── summarizer.py          # Plain-language summary

│   └── audit.py               # Audit logging

└── .gitignore



🛠️ Tech Stack



Language: Python 3.11



UI Framework: Streamlit



NLP: Rule-based processing, regex heuristics



Language Detection: langdetect



Translation: googletrans



Storage: Local JSON audit logs



⚠️ No external legal databases, APIs, or case law are used (as per constraints).



▶️ How to Run the Project

1️⃣ Install dependencies

pip install -r requirements.txt



2️⃣ Run the application

python -m streamlit run app.py



3️⃣ Open in browser

http://localhost:8501



📷 Screenshots



(Add screenshots here for UI, risk analysis, and multilingual output)



🚧 Limitations



Rule-based analysis (no ML training)



No external legal statute or case-law lookup



Entity extraction is heuristic-based (NER-lite)



🔮 Future Enhancements



Contract type classification (Employment, Lease, Vendor, etc.)



Obligation vs Right vs Prohibition tagging



Clause similarity matching to standard templates



PDF report generation



Advanced multilingual support



LLM-assisted legal reasoning (optional)



📜 Disclaimer



This tool provides informational insights only and does not constitute legal advice. Users should consult a qualified legal professional before making contractual decisions.



👩‍💻 Author



V-Preethika

Multilingual Contract Risk Intelligence System

