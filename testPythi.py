from langgraph.graph import StateGraph,MessagesState,START,END
from typing import TypedDict


class BMIState(TypedDict):
    weight_kg:float
    height_m:float
    bmi:float  



def hello_world_node(state: BMIState)->BMIState:
    weight=state['weight_kg']
    height=state['height_m']

    bmi=weight/(height**2)
    state[bmi]=round(bmi,2)
    return state


graph=StateGraph(BMIState)
graph.add_node('bmi calculator',hello_world_node)
graph.add_edge(START,'bmi calculator')
graph.add_edge('bmi calculator',END)

workflow=graph.compile()

initiaState={'weight_kg':71.3,'height_m':5.10}

final_state=workflow.invoke(initiaState)

print(final_state)