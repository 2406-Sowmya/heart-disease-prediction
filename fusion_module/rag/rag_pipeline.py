from fusion_module.rag.generator import generate_explanation


def run_rag(pipeline_output):
    """
    Runs Advanced RAG system
    """

    fusion_output = pipeline_output["fusion"]
    echo_output = pipeline_output["echo"]
    ecg_output = pipeline_output["ecg"]
    clinical_output = pipeline_output["clinical"]

    # 🔹 Generate advanced explanation
    rag_output = generate_explanation(
        fusion_output,
        echo_output,
        ecg_output,
        clinical_output
    )

    return rag_output