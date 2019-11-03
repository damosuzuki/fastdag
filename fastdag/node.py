from typing import Optional, List, Dict

class Node:
    def __init__(self, id: str, parents: Optional[List[Node]], 
                                    children: Optional[List[Node]]):
        self._args_map = {}
        self._input_data = None
        self._output_data = None
        
        self.id = id
        self.parents = [] 
        self.children = []
        self.parents += parents
        self.children += children
    
    def add_parent(self, node: Node, argument_name: str):
        self.parents += node
        self._args_map[node.id + "|" + self.id] = argument_name
    
    def add_child(self, node: Node, argument_name: str):
        self.children += node
        self._args_map[self.id + "|" + node.id] = argument_name
    
    def _load(self, *args, **kwargs):
        # TODO support positional args
        context = kwargs["context"]
        data_args = {}
        for parent in parents:
            name = parent.id + "|" + self.id
            data_args[name] = kwargs[name]
        self._input_data = data_args
        self._output_data = self.load(context, data_args)
        # TODO invoke children
    
    def load(self, context, data_args: dict):
        pass