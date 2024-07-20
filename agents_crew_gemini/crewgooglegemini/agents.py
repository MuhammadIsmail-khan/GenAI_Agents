from crewai import Agent
from dotenv import load_dotenv
import os
load_dotenv()
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
### call gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

news_researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
# creating a write agent with custom tools responsible in writing news blog
news_writer=Agent(
    role="writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in a accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

