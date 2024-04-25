mappa = [
    [1,1,1,0,1,1,1],  #0
    [1,0,0,2,0,1,1],  #1
    [1,1,1,0,1,1,1]   #2
]

def trova(mappa:list[list[int]], player_symbol=2):
    strato = list(filter(lambda x:player_symbol in x, mappa))#[0]
    if not strato: #if strato==[] then player_symbol not in mappa
        return (None)
    strato = strato[0]
    indice_strato = mappa.index(strato)
    indice_giocatore = strato.index(player_symbol)
    return strato, indice_strato, indice_giocatore

def get_lati(mappa, strato, indice_strato, indice_giocatore):
    m = mappa
    s = strato
    is_ = indice_strato
    ig = indice_giocatore
    sopra    = None if not is_ else [m[is_-1][ig-1], m[is_-1][ig], m[is_-1][ig+1]]
    sotto    = None if is_+1 >= len(m) else [m[is_+1][ig-1], m[is_+1][ig], m[is_+1][ig+1]]
    destra   = None if ig+1 >= len(s) else [ None if not is_ else m[is_-1][ig+1], s[ig+1], None if is_+1 >= len(m) else m[is_+1][ig+1] ]
    sinistra = None if not ig else [ None if not is_ else m[is_-1][ig-1], s[ig-1], None if is_+1 >= len(m) else m[is_+1][ig-1] ]
    return sopra, sotto, destra, sinistra

if __name__ == "__main__":
    sopra, sotto, destra, sinistra = get_lati(mappa, *trova(mappa, player_symbol=2))
    print(f"""
Sopra: {sopra}
Sotto: {sotto}
Destra. {destra}
Sinistra: {sinistra}
""")