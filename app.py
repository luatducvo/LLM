import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model

load_dotenv()

@tool('get_weather', description='Return weather information for a given city', return_direct=False)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model = 'google_genai:gemini-3.1-flash-lite',
    # model_provider = 'google_genai',
    tools = [get_weather],
    system_prompt='you are a helpful weather assistant, who always cracks jokes and is humorous while are remaining helpful'
)

response = agent.invoke({
    'messages':[
        {'role':'user', 'content':'what is the weather like in Vienna?'}
    ]
})

print(response)
print('---------------------------------------------------')
print(response['messages'][-1].content)



