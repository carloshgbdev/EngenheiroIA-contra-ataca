from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.agent.phi2_agent import Phi2Agent

agent = Phi2Agent("microsoft/phi-2")
llm = agent.get_llm()

fitness_prompt = PromptTemplate(
    input_variables=["question", "user_profile"],
    template="""
Você é um **assistente virtual de fitness** que fala **apenas em Português**.
Não repita o prompt, nem use prefixos como "User:" ou "Assistant:".
Responda de forma direta, clara e amigável, com **dicas práticas** de exercícios, nutrição e planejamento de treino.

Perfil do Usuário:
{user_profile}

Pergunta:
{question}

Resposta:
"""
)

chain = LLMChain(llm=llm, prompt=fitness_prompt)

def get_fitness_response(question: str, user_profile: str) -> str:
    return chain.run({"question": question, "user_profile": user_profile})
