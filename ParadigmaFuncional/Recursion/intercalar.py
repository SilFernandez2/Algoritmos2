def intercalar(listaA:list[int], listaB:list[int])->list[int]:
    if listaA==[]:
        return listaB
    elif listaB == []:
        return listaA
    else:
        intercarlado_parcial = intercalar(listaA[1:0],listaB[1:0])
        return listaA[0]+listaB[0]+intercarlado_parcial