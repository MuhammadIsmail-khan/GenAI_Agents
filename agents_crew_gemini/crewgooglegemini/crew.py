from crewai import Crew, Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
#formaing the tecd-focused with some enchanced configurations

crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    max_rpm=20
)

def call_llm(input):
## starting the task execution process with enhanced feedback

    result=crew.kickoff(inputs={'topic':input})

    print("result -------------------------------------------")
    print(result) 
    print("result -------------------------------------------")
    return result



