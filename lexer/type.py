from enum import Enum


class Type(Enum):


    PALABRA_RESERVADA = "\\b(class|private|if|else|while|lateinit|const|override)\\b.*"

    # Variables
    VAR = "\\b(var)\\b.*"
    VAL = "\\b(val)\\b.*"

    # Tipos de datos
    CONSTANTE_DOUBLE = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    CONSTANTE_INT = "\\b(\\d{1,9})\\b.*"
    BOOLEAN_VAL = "\\b(true|false)\\b"
    INT = "\\b(Int)\\b.*"
    DOUBLE = "\\b(Double)\\b.*"
    BOOLEAN = "\\b(Boolean)\\b.*"
    STRING = "\\b(String)\\b.*"
    CHAR = "\\b(Char)\\b.*"

    # Identificadores
    IDENTIFICADOR = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"


    # Cadenas de texto
    CADENA_LITERAL = '\"(\\.|[^\\"])*\"'
    CARACTER_LITERAL = r"\'(\\.|[^\\'])*\'"

    # Comentarios
    BLOQUE_DE_COMENTARIO = "(/\\*.*?\\*/).*"
    LINEA_DE_COMENTARIO = "(//(.*?)[\r$]?\n).*"

    PARENTESIS_ABRIR = "(\\().*"
    PARENTESIS_CERRAR = "(\\)).*"
    COMA = "(,).*"
    BLOQUE_INICIO = "(\\{).*"
    BLOQUE_CIERRE = "(\\}).*"
    CORCHETE_ABIERTO = "(\\[).*"
    CORCHETE_CERRADO = "(\\]).*"
    PUNTO = "(\\.).*"    

    # Operadores
    SUMA = "(\\+{1}).*"
    RESTA = "(\\-{1}).*"
    MULTIPLICACION = "(\\*).*"
    DIVISION = "(/).*"
    IGUAL = "(==).*"
    ASIGNACION = "(=).*"
    NO_IGUAL = "(\\!=).*"
    MAYOR = "(>).*"
    MENOR = "(<).*"

    # Excepciones
    ESPACIO = "( ).*"
    SALTO_DE_LINEA = "(\\n).*"

    # Lexico Incorrecto
    LEXICO_INCORRECTO = "(sdfgsd).*"
