import json
from pathlib import Path
from datetime import datetime

AUDIT_FILE = Path("audit_log.json")


def log_audit(filename, risk_level):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "filename": filename,
        "overall_risk": risk_level
    }

    # If file doesn't exist or is empty → start a list
    if not AUDIT_FILE.exists() or AUDIT_FILE.read_text().strip() == "":
        data = []
    else:
        try:
            data = json.loads(AUDIT_FILE.read_text())
            if not isinstance(data, list):
                data = []
        except json.JSONDecodeError:
            data = []

    data.append(entry)

    AUDIT_FILE.write_text(json.dumps(data, indent=2))
