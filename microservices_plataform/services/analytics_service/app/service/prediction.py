from app.agent.loader import load_agent
import pandas as pd
import lime
import lime.lime_tabular

def predict_churn(frequencia_semanal: int, total_checkins: int, tipo_plano: int) -> float:
    agent = load_agent()
    df = pd.DataFrame(
        {
            "frequencia_semanal": [frequencia_semanal],
            "tipo_plano": [tipo_plano],
            "total_checkins": [total_checkins],
        }
    )
    
    proba = agent.predict_proba(df)[0, 1]
    return proba

_explainer = None
def explain_churn(frequencia_semanal: int, total_checkins: int, tipo_plano: int) -> dict:
    global _explainer
     
    agent = load_agent()
    input_df = pd.DataFrame(
        {
            "frequencia_semanal": [frequencia_semanal],
            "tipo_plano": [tipo_plano],
            "total_checkins": [total_checkins],
        }
    )
    
    train_df = pd.read_csv("app/data/churn_data_cleaned.csv")
    train_df.drop(columns=["churn"], inplace=True)

    if _explainer is None:
        _explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data=train_df.values,
            feature_names=input_df.columns.tolist(),
            class_names=["No Churn", "Churn"],
            mode='classification'
        )

    exp = _explainer.explain_instance(
        input_df.values[0],
        agent.predict_proba,
        num_features=len(input_df.columns),
    )

    explanation = {feature: weight for feature, weight in exp.as_list()}
    return explanation
