def limpiar(string):
    string = string.replace('(','').replace(')','').replace('[','').replace(']','').replace('"','').replace('/','')
    #print(string)
    return string