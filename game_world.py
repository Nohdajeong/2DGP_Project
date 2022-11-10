# layer 0 : Background Objects
# layer 1 : Foreground Objects

objects = [[], []]

# collision informaiton
# key 'character:desk' string
# value [ [character], [desk1, desk2, desk3] ]
# collision_group = dict()

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
        raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()

