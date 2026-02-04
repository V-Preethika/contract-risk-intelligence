import streamlit as st

# -------------------- PAGE CONFIG (MUST BE FIRST) --------------------
st.set_page_config(
    page_title="Contract Risk Intelligence",
    layout="wide"
)

from core.contract_loader import extract_text
from core.clause_splitter import split_clauses
from core.risk_engine import assess_risk, RISK_EXPLANATIONS
from core.summarizer import summarize_contract
from core.audit import log_audit
from core.multilingual import normalize_to_english, translate_output
from core.entity_extractor import extract_entities
from core.ambiguity_detector import detect_ambiguity


# -------------------- HEADER --------------------
st.markdown("""
<h1 style='margin-bottom:0'>⚖️ Contract Risk Intelligence</h1>
<p style='color:gray;margin-top:0'>
AI-powered legal risk analysis for SMEs • Multilingual • Explainable
</p>
<hr>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.risk-high { color: #b00020; font-weight: bold; }
.risk-medium { color: #ff9800; font-weight: bold; }
.risk-low { color: #2e7d32; font-weight: bold; }
</style>
""", unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.header("⚙️ Analysis Settings")

    input_lang = st.selectbox(
        "Input Language",
        ["Auto Detect", "English", "Hindi", "Other"]
    )

    output_lang = st.selectbox(
        "Output Language",
        ["English", "Hindi"]
    )

    st.divider()
    st.caption("Contract Risk Engine v1.0")


# -------------------- MAIN UI --------------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)


# -------------------- PROCESSING PIPELINE --------------------
if uploaded_file:
    # 1️⃣ Extract text
    contract_text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.text_area("Contract Text", contract_text, height=200)

    # 2️⃣ Normalize language
    normalized_text, detected_lang = normalize_to_english(contract_text)
    st.caption(f"Detected language: **{detected_lang}**")

    # 3️⃣ Clause splitting
    clauses = split_clauses(normalized_text)

    # 4️⃣ Risk assessment
    risk_result = assess_risk(clauses)

    # 5️⃣ Entity & ambiguity detection
    entities = extract_entities(normalized_text)
    ambiguous_clauses = detect_ambiguity(clauses)

    # 6️⃣ Summary
    summary_en = summarize_contract(normalized_text)
    summary = translate_output(summary_en, output_lang)

    # 7️⃣ Audit log
    log_audit(uploaded_file.name, risk_result["overall_risk"])

    # -------------------- RESULTS --------------------
    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Summary",
        "⚠️ Risk Analysis",
        "🧩 Clause Details",
        "🔍 Entities & Ambiguity"
    ])

    # ----- TAB 1: SUMMARY -----
    with tab1:
        st.subheader("Plain-Language Summary")
        st.write(summary)

    # ----- TAB 2: RISK ANALYSIS -----
    with tab2:
        risk_level = risk_result["overall_risk"].lower()

        st.markdown(
            f"<span class='risk-{risk_level}'>Overall Risk: {risk_result['overall_risk']}</span>",
            unsafe_allow_html=True
        )

        st.divider()

        if risk_result["flags"]:
            for risk, matched_clauses in risk_result["flags"].items():
                st.subheader(f"⚠️ {risk}")

                why_text = translate_output(
                    RISK_EXPLANATIONS[risk]["why"],
                    output_lang
                )
                suggestion_text = translate_output(
                    RISK_EXPLANATIONS[risk]["suggestion"],
                    output_lang
                )

                st.write(why_text)
                st.info(suggestion_text)

                with st.expander("Show related clause text"):
                    for c in matched_clauses:
                        st.write(translate_output(c, output_lang))
        else:
            st.success("No major risk patterns detected.")

    # ----- TAB 3: CLAUSE DETAILS -----
    with tab3:
        st.subheader("Extracted Clauses")
        for i, clause in enumerate(clauses[:20], start=1):
            st.markdown(
                f"**Clause {i}:** {translate_output(clause, output_lang)}"
            )

    # ----- TAB 4: ENTITIES & AMBIGUITY -----
    with tab4:
        st.subheader("📌 Extracted Entities")
        st.json(entities)

        st.divider()

        st.subheader("⚠️ Ambiguous Clauses")
        if ambiguous_clauses:
            for item in ambiguous_clauses:
                st.warning(f"Ambiguous phrase: **{item['phrase']}**")
                st.write(translate_output(item["clause"], output_lang))
        else:
            st.success("No ambiguous clauses detected.")

else:
    st.info("⬆️ Upload a contract file to begin analysis.")
