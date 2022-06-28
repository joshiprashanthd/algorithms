class GraphError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class VertexNotFoundError(GraphError):
    def __init__(self, graph_name, v) -> None:
        super().__init__(f"Graph '{graph_name}' does not contain vertex {v}")

class EdgeNotFoundError(GraphError):
    def __init__(self, graph_name, u, v) -> None:
        super().__init__(f"Graph '{graph_name}' does not contain edge ({u}, {v})")
