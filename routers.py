from dtos import FakeLLMQuestion, FakeLLMAnswer
from services import FakeLLMServices


from fastapi import APIRouter
fake_llm_router = APIRouter()

@fake_llm_router.post("/")
def generate_answer(question: FakeLLMQuestion) -> FakeLLMAnswer:
    answer = FakeLLMServices.generate(question.question)
    return {"answer": answer}