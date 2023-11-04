from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)


def embed(db, raw_text):
    print("Embedding", raw_text)
    docs = text_splitter.split_text(raw_text)
    db.add_texts(docs)


def predict(model, retriever, text):
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}

    Answer in the following language: Vietnamese
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    return chain.invoke(text)
