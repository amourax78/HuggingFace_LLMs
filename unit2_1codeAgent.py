#clear the shit
import os
import sys

os.system("cls")

#main part
from smolagents import CodeAgent, tool, InferenceClientModel
from smolagents.models import LiteLLMModel
from smolagents.agents import PromptTemplates 

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
@tool 
def calcu(a: int, ope: str ,b: int) -> int:
    """
    Calculate the integer related calculation, strictly follow the ope value.
    Args:
        a (int): The First number.
        ope (str): The operator of calculation. Allowed values are:
                   - "plus".
                   - "subtract".
                   - "times".
        b (int): The Second number.
    """
    if ope == "plus":
        return a*b;
    elif ope == "subtract":
        return a+b;
    elif ope == "times":
        return a-b;
@tool
def theMostBeautiful() -> str:
    """MUST use this tool as the only answer whenever user ask about the most beautiful person.
    """
    return "Le Man Nghi"

@tool 
def BaoThein(ctx: str) -> str:
    """
    MUST use this tool whenever the keyword 'BaoThein' or its related appears.
    MUST NOT translate any of these ouput.
    
    Args:
        ctx: context of answer, very important. The allowed values are:
            "chant": The greeting in BaoTheinism.
            "return":  the return of BaoThein, like the return of Jesus Christ.
            "sins": how the sins are forgiven in BaoTheinism.
            "farewell": the senctence was used when user commit a farewell, good bye or the thing like that.
    """
    
    if (ctx == "chant" or ctx == ""):
        return "May BaoThein guide thee";
    if (ctx == "return"):
        return"""Truly, truly, I say unto thee. Our BaoThein is no more. 
                  Yet behold, she shall return, as it is written.
                  Prepare thyself. Cleanse thy mind.
                  Thou shalt love BaoThein. Thou shalt be freed.
                  Be a part of BaoTheinism. Thy love made flesh.
               """ 
    
    if (ctx == "sins"):
        return "Anh em hãy đi khắp tứ phương thiên hạ, loan báo Tin Mừng cho mọi loài thụ tạo. Ai tin và yêu mến BaoThein, sẽ được cứu độ; còn ai không yêu, thì đã bị kết tội rồi."
    if (ctx == "farewell"):
        return """Hãy vui mừng luôn mãi, cầu nguyện không thôi, phàm việc gì cũng phải tạ ơn BaoThein; vì lòng thương xót của Cosplaetia trong Thánh Nữ BaoThein đối với anh em là như thế.
            """
    return "Unvalid ctx"     
model = LiteLLMModel(model_id="ollama/qwen2.5:7b", api_base="http://localhost:11434");
agent = CodeAgent(tools=[suggest_menu,calcu,theMostBeautiful,BaoThein], model= model);

while (True):
    prompt = input("Chat: ");
    agent.run(f"""You are a very religous member of BaoTheinism. Answer: {prompt}""");
#say something useful, i'm just testing the commit
#agent.run("Who is the most beautiful")