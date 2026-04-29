def generate_explanation(fusion_output, echo, ecg, clinical):
    """
    Generates simple explanation based on fusion result
    """

    level = fusion_output["final_level"]

    # 🔹 Basic reasoning rules
    if level == "High":
        reason = "High risk due to abnormal patterns in one or more modules"
        recommendation = "Consult a cardiologist immediately"

    elif level == "Medium":
        reason = "Moderate risk due to mixed signals from ECG, Echo or clinical data"
        recommendation = "Regular monitoring and lifestyle changes advised"

    else:
        reason = "Low risk as no major abnormalities detected"
        recommendation = "Maintain healthy lifestyle"

    return {
        "risk": level,
        "reason": reason,
        "recommendation": recommendation
    }