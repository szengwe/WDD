import math

items=int(input(f"What is the number of the manufactured items: "))
box=int(input(f"what is the number per box : "))

num_boxes=math.ceil(items/box)

print(f"For{items} items ,packing {box}, per box items in each box,you will need {num_boxes} boxes.")