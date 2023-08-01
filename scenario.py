import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, UniqueConstraint, select, ForeignKey, Boolean, insert
from sqlalchemy.orm import mapper, registry, relationship, declarative_base, Session
from sqlalchemy import text
from sqlalchemy.orm import Mapped
import matplotlib.pyplot as plt

def create_scenario_diagram():
    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Define the nodes and edges of the scenario diagram
    nodes = ['access to Jenkins', 'log in', 'configure system', 'tigger pipeline', 'to assign nodes', 'prepare environnement', 'excute job: code compilation, test execution, artifact generation', 'have an error', 'notification to pipeline: node changement',
             'to assign nodes', 'prepare environnement', 'excute job: code compilation, test execution, artifact generation', 'have a success', 'send results', 'send notifications']
    edges = [('access to Jenkins', 'log in'), ('log in', 'configure system'), ('configure system', 'tigger pipeline'), ('configure system', 'tigger pipeline'), ('tigger pipeline', 'to assign nodes'), ('to assign nodes', 'prepare environnement'),
             ('prepare environnement', 'excute job: code compilation, test execution, artifact generation'), ('excute job: code compilation, test execution, artifact generation', 'have an error'), ('have an error', 'notification to pipeline: node changement'), ('notification to pipeline: node changement', 'to assign nodes'),
             ('to assign nodes', 'prepare environnement'), ('prepare environnement', 'excute job: code compilation, test execution, artifact generation'), ('excute job: code compilation, test execution, artifact generation', 'have a success'),
             ('have a success', 'send results'), ('send results', 'send notifications')]

    # Draw the nodes as circles with labels
    for node in nodes:
        ax.add_patch(plt.Circle((0, 0), 0.1, color='white', ec='black'))
        ax.text(0, 0, node, ha='center', va='center')

    # Draw the edges as arrows between nodes
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        start_index = nodes.index(start_node)
        end_index = nodes.index(end_node)
        dx = end_index - start_index
        ax.arrow(start_index, 0, dx, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')



    # Set the axis limits and remove ticks
    ax.set_xlim(-1, len(nodes))
    ax.set_ylim(-0.5, 0.5)
    ax.set_xticks([])
    ax.set_yticks([])

    return fig

def main() :
    #Create the scenario diagram
    scenario_diagram = create_scenario_diagram()

    # Save the diagram as an image (e.g., scenario_diagram.png)
    file_path = 'scenario_diagram.png'
    scenario_diagram.savefig(file_path, format='png')

if __name__ == "__main__":
    main()
create_scenario_diagram()
plt.show()

