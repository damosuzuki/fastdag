from typing import Optional, List, Dict

import gevent
from fastdag.node import Node

class Graph:
    __doc__ = """ A `Graph` is `fastdag`'s representation of data flow, based on
     the concept of a Directed Acyclic Graph (DAG) -- a graph with nodes connected 
     in one direction with no cycles. `fastdag` doesn't actually use many graph 
     theory algorithms in its implementation, but the concept is useful as a 
     mental model of the data flow. Note that a DAG can have more than one root 
     and more than one leaf despite the simple example above."""
    def __init__(self, id: str, roots: List):
        self.roots = []
        self.data = {}
        self.id = id
        self.roots += roots

    # load the nodes of the graph with a breadth first traversal 
    # Call load on all roots
    # For each child of each root:
    #   If child has all of the data it needs:
    #       Call its load function
    #       Store its data
    #   Once all children are loaded, load the next level
    
    def _load_level(self, nodes: List[Node]):
        # TODO
        pass
    
    def add_root(self, node: Node):
        self.roots.append(node)
    
    def run(self, context):
        jobs = [gevent.spawn(node._load) for node in self.roots]
        gevent.joinall(jobs)

        
