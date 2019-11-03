![stability-wip](https://img.shields.io/badge/stability-work_in_progress-lightgrey.svg)

# fastdag
Async data flow-control for real-time data processing and aggregation.

# Motivation

There are certain kinds of web services that fan-out to many other services to munge and aggregate data. Such logic easily becomes unmanageble without a simple way to manage data flow and to add/remove processing steps. I have found that managing data flow in the form of data producers/consumers in a Directed Acyclic Graph (one-way data flow) extremely effective for reasoning about these complex workflows.

Services with significant fan-out and munging also perform pitifully unless IO is async. This is because there are often several IO operations that can happen in parallel, but by default in Python these will be executed sequentially. This is why fastdag uses `gevent` to ensure that all IO operations that can be parallelized are executed concurrently.

# Components

## Graph

A `Graph` is `fastdag`'s representation of data flow, based on the concept of a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph#Data_processing_networks)
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Topological_Ordering.svg/1920px-Topological_Ordering.svg.png" alt="Simple Directed Acyclic Graph Example" width="200"/>

A graph with nodes connected in one direction with no cycles. `fastdag` doesn't actually use graph theory algorithms in its implementation, but the concept is useful as a mental model of the data flow. Note that a DAG can have more than one root and more than one leaf despite the simple example above.

### `add_root(id)`
Adds a root node to the graph. The graph needs to keep track of root nodes in order to kick off execution of the data flow. All other nodes should be added using the `Node` `add_parent` and `add_child` methods before or after calling `add_root`.

### `run(context)`
This triggers the data flow and returns a tuple containing a map of the data produced by each node in the graph (`node_data`) and a merged view of all output data (`merged`). A context can also be provided that can be any value. It is typically an instance of a class that exposes access to state and methods needed by nodes in the graph (request id is a common use case).


## `Node`

A `Node` can take data and/or produce data. If it is a root then the node doesn't take data. Leaf nodes can produce data which become the final addition to the context.

### `Node(id)`
The `Node` constructor takes an id.

### `add_parent(parent_node, argument_name)`
Adds `parent_node` as an ancestor of the node, using `argument_name` when passing the data to the node's `resolve` method.

### `id` 
Identifier for the node.

### `load(context, [named data arguments])`
Takes the context (value passed to `Graph.run()`) and data from ancestors (nodes it depends on) and optionally returns data that will be forwarded to descendents (downstream nodes). The resolve method should be implemented with named arguments so that the parent node data can be forwarded in the expected position. Without named arguments the data will forwarded as argument parameters after `context` in the order they were received.

## `@add_parent(id, argument_name)`
Decorator that can be applied to a `Node` class that specifies a parent node by id, and the argument name to use when passing the parent's data to the `resolve` method.

## `@add_child(id, argument_name)`
Decorator that can be applied to a `Node` class that specifies a child node by id, and the argument name to use when passing the node's data to the child's `resolve` method.




