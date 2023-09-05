from collections import deque

def Add_Result_Into_Dict(gifts:dict,sum_of_magic_presents:int):
    if 100 <= sum_of_magic_presents <= 199:
        gifts["Gemstone"] += 1
        return True
    elif 200 <= sum_of_magic_presents <= 299:
        gifts['Porcelain Sculpture'] += 1
        return True
    elif 300 <= sum_of_magic_presents <= 399:
        gifts['Gold'] += 1
        return True
    elif 400 <= sum_of_magic_presents <= 499:
        gifts['Diamond Jewellery'] += 1
        return True
    return False

def sum_edge_case(magic:int , materials:int):
    if magic + materials < 100:
        if (magic + materials) % 2 == 0:
            return 2 * materials + 3 * magic
        else:
            return 2 * (materials + magic)
    elif magic + materials > 499:
        return int((materials + magic) / 2)

def succeded(gifts:dict):
   if (gifts['Gemstone'] > 0 and gifts["Porcelain Sculpture"]>0) or (gifts['Gold'] and gifts['Diamond Jewellery']):
       print("The wedding presents are made!")
   else:
       print("Aladdin does not have enough wedding presents.")


def print_magic_materials(materials: list, magic :deque):
    if len(materials):
        print(f'Materials left: {(", ").join([str(x) for x in materials])}')
    elif len(magic):
        print(f"Magic left: {(', '.join([str(x) for x in magic]))}")
    else:
        return

def print_dict(gifts:dict):
    gifts = dict(sorted(gifts.items(), key = lambda kvpt: kvpt[0]))
    for key,value in gifts.items():
        if value != 0:
            print(f'{key}: {value}')

gifts = {"Gemstone" : 0 , "Porcelain Sculpture" : 0 , 'Gold' : 0 , "Diamond Jewellery" : 0}

wedding_presents_materials =[int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

while magic_level and wedding_presents_materials:
    magic = magic_level.popleft()
    materials = wedding_presents_materials.pop()
    sum_of_magic_presents = magic + materials
    if not Add_Result_Into_Dict(gifts,sum_of_magic_presents):
        temp_value = sum_edge_case(magic,materials)
        Add_Result_Into_Dict(gifts,temp_value)

succeded(gifts)
print_magic_materials(wedding_presents_materials, magic_level)
print_dict(gifts)




