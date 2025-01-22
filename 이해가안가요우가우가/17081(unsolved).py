class Character:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
        self.max_hp = 20
        self.hp = self.max_hp
        
        self.exp = 0
        self.level = 1
        
        self.atk = 2
        self.arm = 2
        
        self.equip = [0, 0] # 0: weapon, 1: armor
        
        self.slot_size = 0 # max = 4
        self.slot = set() # accessory
    
    def __str__(self):
        return f'''
LV : {self.level}
HP : {self.hp}/{self.max_hp}
ATT : {self.atk}/{self.equip[0]}
DEF : {self.arm}/{self.equip[1]}
EXP : {self.exp}/{self.level * 5}
              '''
    
    def level_up(self):
        if self.exp >= self.level * 5:
            self.max_hp += 5
            self.hp = self.max_hp
            self.atk += 2
            self.arm += 2
            self.exp -= self.level*5
            self.level += 1

    def equip_item(self, chest):
        if chest.name == 'W':
            self.equip[0] = int(chest.item)
        elif chest.name == 'A':
            self.equip[1] = int(chest.item)
        else:
            if self.slot_size < 4 and not chest.opened:
                self.slot.add(chest.item)
                self.slot_size += 1
            elif self.slot_size < 4 and not chest.opened and chest.item == 'RE':
                self.slot.add(chest.item)
    
    def move(self, r, c):
        self.row = r
        self.column = c

class Monster:
    def __init__(self, S, W, A, H, E):
        self.name = S
        self.atk = W
        self.arm = A
        self.max_hp = H
        self.hp = self.max_hp
        self.exp = E
    
class Chest:
    def __init__(self, T, S):
        self.name = T
        self.item = S
        self.opened = False


def mob_count(N, M):
    K, L = 0, 0
    for i in range(N):
        for j in range(M):
            print(i, j)
            if field[i][j] == '&' or field[i][j] == 'M':
                K += 1
            elif field[i][j] == 'B':
                L += 1
    return K, L

def fight(char, mob):
    if 'CO' in char.slot:
        mob.hp -= char.atk
        if 'DX' in char.slot:
            mob.hp -= char.atk
    
    if 'HU' in char.slot and mob.name == 'Boss':
        char.hp = char.max_hp + mob.atk - char.arm
    
    char_atk = max(char.atk - mob.arm, 1)
    mob_atk = max(mob.atk - char.arm, 1)
    
    # char, mob time to kill
    char_ttk = char.hp // mob_atk
    mob_ttk = (mob.hp // char_atk)+1 # character faster

    turn = min(char_ttk, mob_ttk)
    char.hp -= turn * mob_atk
    mob.hp -= turn * char_atk
    
    while char.hp > 0 and mob.hp > 0:
        char.hp -= mob.atk
        mob.hp -= char.atk
    
    if char.hp <= 0: # 캐릭 패배
        if 'RE' in char.slot:
            char.hp = char.max_hp
            mob.hp = mob.max_hp
            # 태초마을
        else:
            defeat(char, mob.name)
    else: # 캐릭 이김
        if mob.hp <= 0:
            char.exp += mob.exp
            if 'EX' in char.slot:
                char.exp += mob.exp//5
            char.level_up()
            if 'HR' in char.slot:
                char.hp = min(char.hp+3, char.max_hp)
            if mob.name == 'Boss':
                print(char)
                print('YOU WIN!')
                exit()

def defeat(char, name):
    for i in range(N):
        print(*field[i], sep='')
    print(char)
    print(f'YOU HAVE BEEN KILLED BY {name}..')
    exit()

    
move = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}

input = open(0).readline

N, M = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]

commands = input().strip()

K, L = mob_count(N, M)


# start row, column
start = (0, 0)
for i in range(N):
    for j in range(M):
        if field[i][j] == '@':
            start = (i, j)

monsters = {}
chests = {}

for i in range(K):
    R, C, S, W, A, H, E = input().split()
    monsters[int(R)-1, int(C)-1] = Monster(S, int(W), int(A), int(H), int(E))

for i in range(L):
    R, C, T, S = input().split()
    chests[int(R)-1, int(C)-1] = Chest(T, S)

char = Character(*start)

passed_turn = 0
for command in commands:
    if char.hp <= 0:
        break

    r, c = move[command]
    nr, nc = char.row + r, char.column + c
    field[char.row][char.column] = '.'
    
    nr = max(0, min(N-1, nr))
    nc = max(0, min(M-1, nc))
    if field[nr][nc] == '#': nr, nc = r, c
    r, c = nr, nc
    char.move(r, c)

    cell = field[r][c]
    if cell in ['&', 'M']:
        fight(char, monsters[(char.row, char.column)])
        field[r][c] = '.'
    elif cell == '^':
        char.hp -= 1 if 'DX' in char.slot else 5
        if char.hp <= 0:
            defeat(char, 'SPIKE TRAP')
    elif cell == 'B':
        chest = chests[(char.row, char.column)]
        char.equip_item(chest)
        chest.opened = True

    field[r][c] = '@'
    passed_turn += 1
print('Press any key to continue.')