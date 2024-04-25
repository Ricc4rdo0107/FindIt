from pprint import pprint

class Player:
    def __init__(self, map_:list[list[str|int]], layer_index:int, index:int, name="7"):
        self.name = name
        self.map = map_
        self.layer_index = layer_index
        self.index = index

        self.precedent_value = self.map[layer_index][index]
        self.map[self.layer_index][index] = self
        self.surroundings = self.update_surroundings()

    def __str__(self):
        return self.name
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        try:
            v = self.update_surroundings()[self.n]
            self.n+=1
            return v
        except:
            raise StopIteration
        
    def calculate_coords(self, move):
        coords = self.get_coords()
        if move == self.move_up:
            coords[1] -= 1
        elif move == self.move_down:
            coords[1] += 1
        elif move == self.move_left:
            coords[0] -= 1
        elif move == self.move_right:
            coords[0] += 1
        return tuple(coords)
        
    def get_coords(self):
        return [self.index,self.layer_index]

    def move_up(self):
        if self.layer_index:
            self.map[self.layer_index][self.index] = self.precedent_value
            self.precedent_value = self.map[self.layer_index-1][self.index]
            self.map[self.layer_index-1][self.index] = self
            self.layer_index-=1

    def move_down(self):
        if not(self.layer_index+1 >= len(self.map)):
            self.map[self.layer_index][self.index] = self.precedent_value
            self.precedent_value = self.map[self.layer_index+1][self.index]
            self.map[self.layer_index+1][self.index] = self
            self.layer_index += 1

    def move_right(self):
        if not(self.index+1 >= len(self.map[self.layer_index])):
            self.map[self.layer_index][self.index] = self.precedent_value
            self.precedent_value = self.map[self.layer_index][self.index+1]
            self.map[self.layer_index][self.index+1] = self
            self.index += 1

    def move_left(self):
        if self.index:
            self.map[self.layer_index][self.index] = self.precedent_value
            self.precedent_value = self.map[self.layer_index][self.index-1]
            self.map[self.layer_index][self.index-1] = self
            self.index -=1
    

    def update_surroundings(self):
        self.show_up, self.show_down, self.show_right, self.show_left = self.get_surroundings()
        v = self.show_up, self.show_down, self.show_right, self.show_left
        self.surroundings = v
        return v
    
    def find(self):
        layer = list(filter(lambda x:self in x, self.map))#[0]
        if not layer: #if strato==[] then player_symbol not in mappa
            return (None)
        layer = layer[0]
        layer_index = self.map.index(layer)
        index = layer.index(self)
        return layer, layer_index, index
    
    def get_surroundings(self):
        m = self.map
        s, is_, ig = self.map[self.layer_index], self.layer_index, self.index
        up    = [None]*3 if not is_ else [m[is_-1][ig-1], m[is_-1][ig], None if ig+1 >= len(s) else m[is_-1][ig+1]]
        down  = [None]*3 if is_+1 >= len(m) else [m[is_+1][ig-1], m[is_+1][ig], None if ig+1 >= len(s) else m[is_+1][ig+1]]
        right = [None]*3 if ig+1 >= len(s) else [ None if not is_ else m[is_-1][ig+1], s[ig+1], None if is_+1 >= len(m) else m[is_+1][ig+1] ]
        left  = [None]*3 if not ig else [ None if not is_ else m[is_-1][ig-1], s[ig-1], None if is_+1 >= len(m) else m[is_+1][ig-1] ]
        return up, down, left, right
    


mappa = [
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0],
    # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
]


def find_gen(mappa:list[list[int]], start:tuple[int, int], target=9, verbose=False):
    """
    the map must have zeros as free path symbol
    """
    layer_index, index = start
    p = Player(mappa, layer_index=layer_index, index=index)
    directions = [ p.move_up, p.move_down, p.move_left, p.move_right ]
    moves : list[tuple[int,int]] = []
    while p.precedent_value != target:
        if verbose: pprint([list(map(str, x)) for x in mappa])
        cross = [ x[1] for x in p.get_surroundings() ]
        if target in cross:
            direction = cross.index(target)
            directions[direction]()
            if verbose: pprint([list(map(str, x)) for x in mappa])
            return True
        else:
            direction = cross.index(0)
            move = directions[direction]
            coords = p.index, p.layer_index
            next_coords = p.calculate_coords(move)
            if verbose: pprint(f"Coords:{coords} NextCoords:{next_coords} Cross:{cross} Moves:{moves}")
            if next_coords in moves:
                direction = cross.index(0, direction+1)
        move = directions[direction]
        coords = p.index, p.layer_index
        moves.append(coords)
        move()
        yield mappa


def find(mappa:list[list[int]], start:tuple[int, int], target=9, verbose=False):
    """
    the map must have zeros as free path symbol
    """
    layer_index, index = start
    p = Player(mappa, layer_index=layer_index, index=index)
    directions = [ p.move_up, p.move_down, p.move_left, p.move_right ]
    moves : list[tuple[int,int]] = []
    while p.precedent_value != target:
        if verbose: pprint([list(map(str, x)) for x in mappa])
        cross = [ x[1] for x in p.get_surroundings() ]
        if target in cross:
            direction = cross.index(target)
            directions[direction]()
            if verbose: pprint([list(map(str, x)) for x in mappa])
            return True
        else:
            direction = cross.index(0)
            move = directions[direction]
            coords = p.index, p.layer_index
            next_coords = p.calculate_coords(move)
            if verbose: pprint(f"Coords:{coords} NextCoords:{next_coords} Cross:{cross} Moves:{moves}")
            if next_coords in moves:
                direction = cross.index(0, direction+1)
        move = directions[direction]
        coords = p.index, p.layer_index
        moves.append(coords)
        move()

if __name__ == "__main__":
    find(mappa, start=(0,1), verbose=1)