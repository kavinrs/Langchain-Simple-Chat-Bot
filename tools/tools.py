from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from pathlib import Path
import os
import sympy as sp


key=os.environ.get("OPENAI_API_KEY")
llm_openai=ChatOpenAI(model="gpt-4o-mini",
                      temperature=0,
                      api_key=key)

# Use absolute path relative to this file's location
csv_path = Path(__file__).parent / "Churn Prediciton Dataset.csv"

csv_agent = create_csv_agent(
    llm_openai,
    str(csv_path),
    verbose=True,
    allow_dangerous_code=True
)

#Mathematical Computations
@tool
def add(a:int ,b:int)->int:
    """Use this tool to add two numbers. Example: add(2, 3)"""
    return a+b

@tool
def subtract(a:int, b:int)->int:
    """Use this tool to subtract two numbers. Example: subtract(5, 2)"""
    return a-b

@tool
def multiply(a:int ,b:int)->int:
    """Use this tool to multiply two numbers. Example: multiply(2, 4)"""
    return a*b

@tool      
def divide(a:int,b:int)->float:
    """Use this tool to divide two numbers. Example: divide(10, 2)"""
    return a/b

@tool
def exponent(a:int,b:int)->int:
    """Use this tool to give power of a number . Example : exponent(5,2)"""
    return a**b

@tool
def scientific_calculator(expression: str) -> str:
    """
    Evaluates advanced mathematical expressions.
    
    Supports:
    - Basic arithmetic: +, -, *, /
    - Powers: ** or ^
    - Roots: sqrt(x)
    - Trigonometry: sin, cos, tan
    - Logs: log(x), ln(x)
    - Constants: pi, e
    - Equations: solve(x + 2 - 5)
    
    Examples:
    - "2 + 3 * 5"
    - "sin(pi/2)"
    - "log(100,10)"
    - "sqrt(16)"
    - "x**2 - 4"
    """

    try:
        expression = expression.replace("^", "**")
        expr = sp.sympify(expression)

        if expr.free_symbols:
            return str(expr)

        return str(expr.evalf())
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def differentiate(expression: str) -> str:
    """
    Differentiate expression.
    
    Example:
    "x**2 + 3*x"
    """
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        result = sp.diff(expr, x)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    
@tool
def integrate_expr(expression: str) -> str:
    """
    Integrate expression.
    
    Example:
    "x**2"
    """
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        result = sp.integrate(expr, x)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"



#Tool for Weather
@tool 
def weather(city:str)->str:
    """Use this to find the weather of the given city"""

    api_key=os.environ.get("OPENWEATHERMAP_API_KEY")
    weather = OpenWeatherMapAPIWrapper(openweathermap_api_key=api_key)
    weather_data = weather.run(city)
    return weather_data
    

#Tool for Web Search
@tool 
def web_search(query:str)->str:
    """Use this to search the web tool to the answer when you are unable to get answer from other tools"""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)


#Tool for executing python code
@tool
def python_execution(code:str):
    """
You are an AI assistant.

IMPORTANT RULES:
- If user asks for code → DO NOT execute tools
- ONLY return Python code
- Use tools ONLY when user asks for computation result
"""

    python=PythonREPL()

    # if "print(" not in code:
    #     code += "\nprint(locals())"
    return python.run(code)


#tool to extract keyword from the text
@tool
def extract_keyword(text:str)->str:
    """Use this tool extract the important keyword from the text """
    return llm_openai.invoke(f"Extract the important keyword from the text {text}")


#tool to summarize the text
@tool
def summarize_text(text:str)->str:
    """Use this tool to summarize the text"""

    return llm_openai.invoke(f"Summarize the text with only the important context {text}")

#tool to get content from the csv file
@tool
def churn_csvtool(query: str) -> str:
    """
STRICTLY use this tool for customer churn dataset queries.

You MUST use this tool if:
- The question involves churn rate, customer retention, or churn analysis
- The answer requires reading or analyzing the CSV dataset

DO NOT use web search for these questions.

Examples:
- "What is the churn rate?"
- "How many customers left?"
- "Average tenure of churned users"
"""
    try:
        return csv_agent.run(query)
    except Exception as e:
        return f"Error: {str(e)}"



#Final Answer Tool
@tool
def final_answer(answer:str)->str:
    """Use this tool to return the final answer for the user questions"""
    return answer



