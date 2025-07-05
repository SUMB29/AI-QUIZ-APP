import openai
import os
from flask import Flask, render_template, request
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = Flask(__name__)

template = PromptTemplate.from_template(
    "Generate 5 questions on topic : {topic} ,each question having 4 options and one correct answer."
)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form["topic"]
        llm = OpenAI(temperature=0.9)
        chain = LLMChain(llm=llm, prompt=template)
        response = chain.run(topic)
        return render_template("output.html", response=response, topic=topic)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
