def retrieve_insights(echo, ecg, clinical):
    """
    Extract reasoning from all agents
    """

    insights = []

    # Echo
    if echo.get("reason"):
        insights.append(echo["reason"])

    # ECG
    if ecg.get("reason"):
        insights.append(ecg["reason"])

    # Clinical
    if clinical.get("reason"):
        insights.append(clinical["reason"])

    return insights