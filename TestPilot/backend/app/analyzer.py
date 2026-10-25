
from .schemas import AnalyzeRequest


def analyze_test(request: AnalyzeRequest):

    code = request.test_code.lower()

    if "sleep(" in code:
        category = "async_wait"
        explanation = (
            "The test contains a fixed delay. "
            "Investigate whether an asynchronous operation "
            "has completed before the assertion."
        )

    elif "thread" in code or "lock" in code:
        category = "concurrency"
        explanation = (
            "The test contains concurrency-related code. "
            "Investigate possible race conditions."
        )

    elif "static " in code or "global " in code:
        category = "shared_state"
        explanation = (
            "The test may use shared state. "
            "Investigate dependencies between test runs."
        )

    else:
        return {
            "status": "needs_review",
            "root_cause": None,
            "explanation": "No demonstration pattern matched.",
            "confidence": None,
            "model_used": False
        }

    return {
        "status": "pattern_matched",
        "root_cause": category,
        "explanation": explanation,
        "confidence": None,
        "model_used": False
    }
