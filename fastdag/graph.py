import gevent
import fastdag.node

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

    def _wrap(self, node, context):
        
    
    def add_root(self, node: Node):
        self.roots.append(node)
    
    def run(self, context):
        spawn_list = [gevent.spawn(node.load) for node in self.roots]
        gevent.joinall(spawn_list)
