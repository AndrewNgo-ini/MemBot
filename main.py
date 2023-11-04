import discord
import os
import signal
from discord.ext import commands
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from membot import embed, predict

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command(name="learn")
async def learn_command(ctx, *, text):
    if os.getenv("OPENAI_API_KEY") == None:
        await ctx.send(
            "Bạn phải đăng kí key OPEN AI /register trước khi sử dụng /learn."
        )
    else:
        # Embed the text
        embed(db, text)
        await ctx.send("Bot đã học xong rồi ạ")


@bot.command(name="ask")
async def ask_command(ctx, *, text):
    if os.getenv("OPENAI_API_KEY") == None:
        await ctx.send("Bạn phải đăng kí key OPEN AI /register trước khi sử dụng /ask.")
    else:
        # Predict the answer
        answer = predict(model, retriever, text)
        await ctx.send(answer)


def save_retriever_and_exit(signum, frame):
    global db
    print("Saving FAISS index before shutdown...")
    db.save_local("faiss_index")
    print("Shutdown complete.")
    os._exit(0)


# Register the signal handlers for graceful shutdown
signal.signal(signal.SIGINT, save_retriever_and_exit)
signal.signal(signal.SIGTERM, save_retriever_and_exit)

if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY") == None:
        key = input("Enter OPENAI_API_KEY: ")
        os.environ["OPENAI_API_KEY"] = key
    if os.getenv("TOKEN") == None:
        key = input("Enter Discord Bot Token: ")
        print("Token: " + key)
        discord_token = key
    model = ChatOpenAI()
    if "faiss_index" in os.listdir("."):
        db = FAISS.load_local("faiss_index", OpenAIEmbeddings())
        retriever = db.as_retriever()
    else:
        db = FAISS.from_texts(["First set up"], OpenAIEmbeddings())
        retriever = db.as_retriever()
    try:
        bot.run(discord_token)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Attempt to save on other kinds of shutdown as well
        save_retriever_and_exit(None, None)
