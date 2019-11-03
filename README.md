# fastdag
Async data flow-control for real-time data processing and aggregation.

# Motivation

There are certain kinds of web services that fan-out to many other services to munge and aggregate data. Such logic easily becomes unmanageble without a simple way to manage data flow and to add/remove processing steps. I have found that managing data flow in the form of data producers/consumers in a Directed Acyclic Graph (one-way data flow) extremely effective for reasoning about these complex workflows.

Services with significant fan-out and munging also perform pitifully unless IO is async. This is because there are often several IO operations that can happen in parallel, but by default in Python these will be executed sequentially. This is why fastdag uses `gevent` to ensure that all IO operations that can be parallelized are executed concurrently.

# Components

## Graph

A `Graph` is `fastdag`'s representation of data flow, based on the concept of a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph#Data_processing_networks)
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Topological_Ordering.svg/1920px-Topological_Ordering.svg.png" alt="Simple Directed Acyclic Graph Example" width="200"/>

A graph with nodes connected in one direction with no cycles. `fastdag` doesn't actually use graph theory in its implementation, but the concept is useful as a mental model of the data flow. Note that a DAG can have more than one root and more than one leaf despite the simple example above.

## Graph.resolve(context)
This triggers the data flow. All data will be available in the context object when execution is complete.

## Node

A `Node` can take data and/or produce data. If it is a root then the node doesn't take data. Leaf nodes can produce data which become the output of `Graph.resolve()`.

## Context

As data flows through the graph, the context maintains a record of the data produced by each node, as well as a merged view of the data. 


