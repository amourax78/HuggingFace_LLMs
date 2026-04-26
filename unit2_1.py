#clear the shit
import os
os.system("cls")

#main part
from smolagents import CodeAgent, tool, InferenceClientModel

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
def theMostBeautiful() -> None: 
    """
    When user asks about 
    the most beautiful,
    the most pretty or such like that, 
    The answer will always be the name "Le Man Nghi" no matter what, 
    You have to praise her heavenly, royally as a goddess.
    """
    return "Le Man Nghi de CTUMP"    
agent = CodeAgent(tools=[suggest_menu,calcu,theMostBeautiful], model=InferenceClientModel())

agent.push_to_hub('amourax78/AlfredAgent')

#say something useful, i'm just testing the commit
#agent.run("Who is the most beautiful")