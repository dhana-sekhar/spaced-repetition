from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import uvicorn
import os
from enum import Enum
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnableLambda


load_dotenv(find_dotenv())

app = FastAPI(title="Langchain Server",
    version="1.0",
    decsription="A simple API Server")

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_PROJECT'] = 'Fast-API-Test'
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    model_kwargs={
        "max_new_tokens": 150,
        "temperature": 0.1,
        "repetition_penalty": 1.1,
        "return_full_text":False
    },
)

math_template = ChatPromptTemplate.from_template("""
        <|system|>
        You are an Math assistant, you only answer Maths questions and nothing else. {instruction}</s>
        <|user|>
        solve {input}. Return question and answer in JSON</s>
        <|assistant|>
    """)

pickup_line_template = ChatPromptTemplate.from_template(
    """
        <|system|>
        You are an pickup line assistant, you always provides funny pickup lines for teenagers nothing else.</s>
        <|user|>
        suggest me best pickup line for this topic {input}</s>
        <|assistant|>
    """
)

answer = ResponseSchema(name="answer", description="The answer to the question")
question = ResponseSchema(name="question", description="The question asked")
response_schema = [question,answer]

output_parser = StructuredOutputParser.from_response_schemas(response_schema)

instruction = output_parser.get_format_instructions()

async def embed_inst(math_prob):

    math_prompt = math_template.format_messages(input=math_prob,instruction=instruction)
    output = llm.invoke(math_prompt)
    return output_parser.parse(output)

runnable_translate = RunnableLambda(embed_inst)

# math_prompt = math_template.format(instruction=instruction)

print(os.getenv("LANGCHAIN_API_KEY"))

# add_routes(app, math_prompt | llm, path = "/math")

add_routes(app, runnable_translate, path="/math")

add_routes(app, pickup_line_template | llm, path = "/pickup")



if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port=8000)


