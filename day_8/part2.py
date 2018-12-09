with open('input.txt') as f:
    content = f.readlines()[0][:-1].split(' ')



class Node():
    def __init__(self,child_count, metadata_count):
        self.child_count = child_count
        self.metadata_count = metadata_count
        self.children = []
        self.metadata = []
    def print(self, level=0):
        print(str(level) + '   ' + str(self.metadata) + '  ' + str(self.child_count))
        for child in self.children:
            child.print(level + 1)


def process(no_children, content):
    nodes = []    
    while no_children > 0:
        no_children -= 1

        child_count = int(content[0])
        meta_count = int(content[1])
        node = Node(child_count, meta_count)

        if child_count == 0:
            metadata = content[2:2+meta_count]
            node.metadata = metadata
            nodes.append(node)
            content = content[2+meta_count:]
        
        else: 
            children, content = process(child_count, content[2:])
            metadata = content[:meta_count]
            node.metadata = metadata
            node.children = children
            content = content[meta_count:]
            nodes.append(node)

    return nodes, content

def sum_up(node):
    value = 0
    if node.child_count == 0:
        for number in node.metadata:
            value += int(number)
    else:
        for number in node.metadata:
            number = int(number)
            if number-1 < node.child_count:
                value += sum_up(node.children[number-1])
                
    return value

tree, y = process(1,content)
result = sum_up(tree[0])



print(result)