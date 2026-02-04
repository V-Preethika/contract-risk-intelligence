import json
from datetime import datetime
from pathlib import Path

AUDIT_FILE = Path("data/audit_logs.json")

def log_audit(filename, risk):
    AUDIT_FILE.parent.mkdir(exist_ok=True)
    if not AUDIT_FILE.exists():
        AUDIT_FILE.write_text("[]")

    data = json.loads(AUDIT_FILE.read_text())
    data.append({
        "file": filename,
        "risk": risk,
        "time": datetime.utcnow().isoformat()
    })
    AUDIT_FILE.write_text(json.dumps(data, indent=2))
