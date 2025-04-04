class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("Source list is empty")
    node_to_move = source
    source = source.next
    node_to_move.next = dest
    return Context(source, node_to_move)
