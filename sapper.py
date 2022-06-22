import random as r
    
views = {
    0: ':white_large_square:',
    1: ':one:',
    2: ':two:',
    3: ':three:',
    4: ':four:',
    5: ':five:',
    6: ':six:',
    7: ':seven:',
    8: ':eight:',
    9: ':nine:',
    10: ':keycap_ten:',
}

table = [
    [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:", ":white_large_square:",":white_large_square:"],
    [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:", ":white_large_square:",":white_large_square:"],
    [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:", ":white_large_square:",":white_large_square:"],
    [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:", ":white_large_square:",":white_large_square:"],
]

new_table = table.copy()

_ = 0
while _ < 4:
    n1 = r.randint(0,3)    
    n2 = r.randint(0,6)
    if table[n1][n2] == ":white_large_square:":
        table[n1][n2] = ":bomb:"
        _ += 1
        
for v,i in enumerate(table):
    for k in range(0, len(i)):
        if table[v][k] == ':bomb:':
            continue
              
        count = 0
        
        force = {
            0: v-1 if v-1 != -1 else None,
            1: v if v != -1 else None,
            2: v+1 if v+1 != -1 else None,
        }
        
        positions = {
            0: k-1 if k-1 != -1 else None,
            1: k if k != -1 else None,
            2: k+1 if k+1 != -1 else None,
        }
        
        for n in range(0,3):
            if force[n] is None:
                continue
            
            try:
                if table[force[n]][positions[0]] == ":bomb:":
                    count += 1
                    
            except:
                pass
            
            try:
                if table[force[n]][positions[1]] == ":bomb:":
                    count += 1

            except:
                pass
            
            try:
                if table[force[n]][positions[2]] == ":bomb:":
                    count += 1

            except:
                pass
            
        table[v][k] = views[count]
        
 
for i in table:
    for j in i:
        print(f'||{j}||', end='')
    print()