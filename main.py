from fastapi import FastAPI
from pydantic import BaseModel
from langchain_huggingface.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import json

app = FastAPI()

# Loading the model and tokenizer
model_id = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
pipe = pipeline("summarization", model=model, tokenizer=tokenizer, max_length=20, min_length=5, do_sample=False)
hf = HuggingFacePipeline(pipeline=pipe)

# Define the request type
class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(request: SummarizeRequest):
    text_to_summarize = request.text

    # Creating a template for a prompt
    template = f"""The following is a text
    {text_to_summarize}
    Based on this text, please identify the main themes
    Helpful Answer:"""

    prompt = PromptTemplate.from_template(template)

    # Combining a template and HuggingFace pipeline in LangChain
    chain = prompt | hf

    # Executing the chain and converting the result in JSON
    result = chain.invoke({"text": text_to_summarize})
    result = json.dumps({"result": result})

    return result

if __name__ == "__main__":
    # Start local web server
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

