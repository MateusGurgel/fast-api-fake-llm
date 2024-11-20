from langchain_core.language_models.fake import FakeListLLM

class FakeLLMServices:
    @staticmethod
    def generate(question: str) -> str:

        responses = [
            "Hello",
        ]

        fake_llm = FakeListLLM(responses=responses)

        return fake_llm.invoke(question)
