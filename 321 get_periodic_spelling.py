def get_periodic_spelling(word):
    ELEMENTS = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];

    def find_spelling(word):
        if len(word) < 1:
            return []
        if word[:2].capitalize() in ELEMENTS:
            solution = find_spelling(word[2:])
            if solution != None:
                return solution + [word[:2].capitalize()]
        if word[:1].capitalize() in ELEMENTS:
            solution =  find_spelling(word[1:])
            if solution != None:
                return solution+[word[:1].capitalize()]
        return None

    return [] if find_spelling(word) == None else find_spelling(word)[::-1]

print(get_periodic_spelling("neon"))
print(get_periodic_spelling("rational"))
print(get_periodic_spelling("yarn"))
print(get_periodic_spelling("carbon"))
print(get_periodic_spelling("noisy"))
print(get_periodic_spelling("bicycles"))
print(get_periodic_spelling("optics"))
print(get_periodic_spelling("value"))
