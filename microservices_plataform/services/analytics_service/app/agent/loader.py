import joblib
import os

_agent = None

def load_agent():
    global _agent
    if _agent is None:
        path = os.path.join(os.path.dirname(__file__), "churn_agent.joblib")
        _agent = joblib.load(path)
    return _agent
