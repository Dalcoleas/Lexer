from lexer.lexer import lex_source_file
from lexer.type import Type
from lexer.identificador import Identificador

tokens = lex_source_file('./Ejemplo.kt')

listaIdentificadores = list()

bandera = False
banderaAssing = False 
banderaVar = False
tokenValue = ''
cont = 0
tokenV = 0
tokenV1 = 0
tokenV2 = 0


print("Analizador Lexigrafico\n")
print("=======================\n")

for token in tokens:
    if token.type not in [Type.ESPACIO, Type.SALTO_DE_LINEA, Type.LINEA_DE_COMENTARIO, Type.BLOQUE_DE_COMENTARIO]:
        print(token)
        
        if(token.type == Type.VAR or token.type == Type.VAL):
            banderaVar = True
            tokenV1 = tokens.index(token)
        if(token.type == Type.IDENTIFICADOR and tokens.index(token)-2 == tokenV1 and banderaVar):
            bandera = True
            tokenValue = token.value
            tokenV = tokens.index(token)
        if (token.type == Type.ASIGNACION and tokens.index(token)-2 == tokenV and bandera):
            banderaAssing = True
            tokenV2 = tokens.index(token)
        if (token.type == Type.CADENA_LITERAL or token.type == Type.CONSTANTE_INT and tokens.index(token)-2 == tokenV2 or token.type == Type.CONSTANTE_DOUBLE or token.type == Type.CADENA_LITERAL or token.type == Type.BOOLEAN_VAL and banderaAssing):
            iden = Identificador(tokenValue, token.value, token.type)
            listaIdentificadores.append(iden)
            bandera = False
            banderaAssing = False
            banderaVar = False


print("\n")
print("=======================\n")
print("Tabla Hash de Identificadores, con su respectivo nombre, tipo y valor.\n")

for algo in listaIdentificadores:
    print (algo)