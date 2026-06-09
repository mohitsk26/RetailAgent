from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END

from src.agents.recommendation_agent import (
    generate_recommendation
)


# ----------------------------------------
# Graph State
# ----------------------------------------

class GraphState(TypedDict):

    customer: dict

    result: dict


# ----------------------------------------
# Recommendation Node
# ----------------------------------------

def recommendation_node(

    state: GraphState

):

    recommendation = generate_recommendation(

        state["customer"]

    )

    return {

        "result": recommendation

    }


# ----------------------------------------
# Build Graph
# ----------------------------------------

builder = StateGraph(

    GraphState

)

builder.add_node(

    "recommendation",

    recommendation_node

)

builder.set_entry_point(

    "recommendation"

)

builder.add_edge(

    "recommendation",

    END

)

graph = builder.compile()


# ----------------------------------------
# Test
# ----------------------------------------

if __name__ == "__main__":

    customer = {

        "Recency": 95,

        "Frequency": 3,

        "Monetary": 12000,

        "Avg_Discount": 25,

        "Customer_Tier": "Silver",

        "Favorite_Category": "Fashion"

    }

    output = graph.invoke(

        {

            "customer": customer

        }

    )

    print("=" * 80)

    print("LANGGRAPH OUTPUT")

    print("=" * 80)

    print(output)