    while len(lf) > 0:
        for a in range(len(lf)):
            if lf[a][3] < mas_antiguo:
                mas_antiguo = lf[a][3]
        for b in range(len(lf)):
            if lf[b][3] == mas_antiguo:
                lista_en_orden.append(lf[b])
                lf.pop(b)