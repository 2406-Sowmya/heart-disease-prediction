from fusion_module.rag.retriever import retrieve_insights
from fusion_module.rag.rules_engine import apply_rules


def generate_explanation(fusion_output, echo, ecg, clinical):
    """
    Advanced RAG generator
    """

    # 🔹 Step 1: Retrieve insights
    insights = retrieve_insights(echo, ecg, clinical)

    # 🔹 Step 2: Apply rules
    rules = apply_rules(echo, ecg, clinical, fusion_output)

    final_level = fusion_output["final_level"]
    risk_percentage = fusion_output["risk_percentage"]

    # 🔹 Step 3: Build final explanation
    explanation = {
        "final_level": final_level,
        "risk_percentage": risk_percentage,
        "explanation": rules["summary"],
        "details": rules["details"]
    }

    return explanation