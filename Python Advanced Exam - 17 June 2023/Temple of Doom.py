from collections import deque

def print_funct(tools:deque, substances:list, challenges:list):
    if challanges:
        print("Harry is lost in the temple. Oblivion awaits him.")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {(', ').join([str(x) for x in tools])}")
    if substances:
        print(f"Substances: {(', ').join([str(x) for x in substances])}")
    if challanges:
        print(f"Challenges: {(', ').join([str(x) for x in challenges])}")



tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challanges = [int(x) for x in input().split()]
while len(tools) and len(substances) :
    tool = tools[0]
    substance = substances[-1]
    product = tool * substance
    if product in challanges:
        challanges.remove(product)
        tools.popleft()
        substances.pop()
    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

print_funct(tools,substances,challanges)
