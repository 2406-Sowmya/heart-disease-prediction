def apply_rules(echo, ecg, clinical, fusion_output):
    """
    Apply logical rules to generate structured reasoning
    """

    rules_output = {
        "summary": "",
        "details": []
    }

    echo_level = echo.get("level")
    ecg_level = ecg.get("level")
    clinical_level = clinical.get("level")

    # 🔹 Rule 1: High risk condition
    if echo_level == "High" and ecg_level == "High":
        rules_output["summary"] = "High risk due to both structural and electrical abnormalities"

    elif clinical_level == "High":
        rules_output["summary"] = "High risk driven by clinical factors"

    elif ecg_level == "High":
        rules_output["summary"] = "Elevated risk due to ECG abnormalities"

    elif echo_level == "High":
        rules_output["summary"] = "Elevated risk due to structural heart issues"

    elif ecg_level == "Medium" or clinical_level == "Medium":
        rules_output["summary"] = "Moderate risk due to mixed indicators"

    else:
        rules_output["summary"] = "Low risk with no major abnormalities"

    # 🔹 Collect detailed reasons
    if echo.get("reason"):
        rules_output["details"].append(f"Echo: {echo['reason']}")

    if ecg.get("reason"):
        rules_output["details"].append(f"ECG: {ecg['reason']}")

    if clinical.get("reason"):
        rules_output["details"].append(f"Clinical: {clinical['reason']}")

    return rules_output