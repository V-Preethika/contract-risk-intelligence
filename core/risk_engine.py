# -------------------- RISK PATTERN DEFINITIONS --------------------
# Each risk now has a WEIGHT (used for scoring)

RISK_PATTERNS = {
    "Indemnity Clause": {
        "patterns": ["indemnify", "hold harmless"],
        "weight": 30
    },
    "Unilateral Termination": {
        "patterns": ["terminate at any time", "termination without notice"],
        "weight": 25
    },
    "Penalty Clause": {
        "patterns": ["penalty", "liquidated damages"],
        "weight": 20
    },
    "Non-Compete": {
        "patterns": ["non compete", "non-compete", "restriction on employment"],
        "weight": 15
    },
    "Auto-Renewal": {
        "patterns": ["auto renew", "automatically renewed"],
        "weight": 10
    }
}


# -------------------- RISK ASSESSMENT ENGINE --------------------
def assess_risk(clauses):
    """
    Performs rule-based legal risk detection.
    Returns:
    - clause-level risks
    - numeric risk score (0–100)
    - composite risk level
    """

    flags = {}
    total_score = 0
    detected_risks = 0

    for risk_name, config in RISK_PATTERNS.items():
        patterns = config["patterns"]
        weight = config["weight"]

        matches = [
            clause for clause in clauses
            if any(p in clause.lower() for p in patterns)
        ]

        if matches:
            flags[risk_name] = {
                "severity": weight,
                "clauses": matches[:2]
            }
            total_score += weight
            detected_risks += 1

    # Cap score at 100
    risk_score = min(total_score, 100)

    # Composite label
    if risk_score >= 60:
        overall = "HIGH"
    elif risk_score >= 30:
        overall = "MEDIUM"
    else:
        overall = "LOW"

    return {
        "overall_risk": overall,
        "risk_score": risk_score,
        "risk_count": detected_risks,
        "flags": flags
    }


# -------------------- RISK EXPLANATIONS (PLAIN LANGUAGE) --------------------
# English-only by design; translated at UI layer

RISK_EXPLANATIONS = {
    "Indemnity Clause": {
        "why": (
            "This clause may require you to compensate the other party "
            "for losses even if the issue was not caused by you."
        ),
        "suggestion": (
            "Limit indemnity to direct damages and cap the maximum liability."
        )
    },

    "Unilateral Termination": {
        "why": (
            "The other party can end the contract without adequate notice "
            "or a valid reason."
        ),
        "suggestion": (
            "Require notice and specify valid termination grounds."
        )
    },

    "Penalty Clause": {
        "why": (
            "This clause may impose penalties that exceed actual losses."
        ),
        "suggestion": (
            "Use reasonable, pre-estimated liquidated damages instead."
        )
    },

    "Non-Compete": {
        "why": (
            "This clause may restrict your ability to work after contract termination."
        ),
        "suggestion": (
            "Limit the duration, geography, and scope of the restriction."
        )
    },

    "Auto-Renewal": {
        "why": (
            "The contract may renew automatically without your explicit consent."
        ),
        "suggestion": (
            "Require written confirmation before renewal."
        )
    }
}
