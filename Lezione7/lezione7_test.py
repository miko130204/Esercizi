def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for k, v in da_rimuovere.items():
        for x in range(v):
            if k in lista:
                lista.remove(k)
                
    return lista

###############################

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    student_grades = {}
    for student in voti:
        nome = student['nome']
        voto = student['voto']
        if nome not in student_grades:
            student_grades[nome] = []

        student_grades[nome].append(voto)
        
       

    return student_grades

###############################

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    item = {}
    for key, value in prodotti:
        value_discount = value - (value/100)*10
        if value_discount > 20:
            item.extend((key, value_discount))
            
    return item

###############################

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    items = {}
    for key, value in prodotti.items():
        value_discount = value - (value/100)*10
        if value_discount > 20:
            items[key] = value_discount
            
    return items