from fusion_module.rag.generator import generate_explanation


def run_rag(pipeline_output):
    """
    Takes full pipeline output and returns explanation
    """

    fusion_output = pipeline_output["fusion"]
    echo_output = pipeline_output["echo"]
    ecg_output = pipeline_output["ecg"]
    clinical_output = pipeline_output["clinical"]

    explanation = generate_explanation(
        fusion_output,
        echo_output,
        ecg_output,
        clinical_output
    )

    return explanation