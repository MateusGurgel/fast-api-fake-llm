from pydantic import BaseModel

class FakeLLMQuestion(BaseModel):
    question: str

class FakeLLMAnswer(BaseModel):
    answer: str