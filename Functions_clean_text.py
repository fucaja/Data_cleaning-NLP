import re

def remove_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.sub(pattern, '', text)

def remove_phone_number(text):
    # Pattern to find phone numbers in various formats
    pattern = re.compile(
        r'\+\d{1,4}\s?(\(\d{1,}\))?[-.\s]?\d{1,20}[-.\s]?\d{1,20}[-.\s]?\d{1,20}|'
        r'\(\d{3}\) \d{3}-\d{4}|'
        r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b|'
        r'\b\d{10}\b'
    )    
    result = re.sub(pattern, '', text)
    return result

def remove_hashtags(text):
    hashtag_pattern = r'\#\w+'
    return re.sub(hashtag_pattern, '', text)





# Ejemplo de uso
texto_original = """
Hola, mi correo es usuario@example.com. Puedes llamarme al 123 456 7890. #Python #Programacion
Validando correos usuario@example.com, usuario.nombre@example.com, usuario_nombre@example.com, usuario-nombre@example.com, usuario@subdominio.example.com, usuario+adicional@example.com
validando números (123) 456-7890, 123-456-7890, 123.456.7890, +1 (123) 456-7890, +44 20 7946 0958, 1234567890, +1-123-456-7890, +44-20-7946-0958, +11234567890, +442079460958
"""

texto_limpo = remove_email(texto_original)
texto_limpo = remove_hashtags(texto_limpo)
texto_limpo = remove_phone_number(texto_limpo)

print("Texto original:", texto_original)
print("Texto limpio:", texto_limpo)




import re

def remove_urls(text):
    # Patrón para eliminar diferentes tipos de URL
    url_pattern = re.compile(
        r'(http[s]?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(:\d+)?(/[^\s]*)?'
        r'|www\.[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(:\d+)?(/[^\s]*)?'
        r'|ftp://[^\s]+'
        r'|feed://[^\s]+'
        r'|file://[^\s]+'
    )
    return re.sub(url_pattern, '', text)


texto_original = """http://www.ejemplo.com
https://www.ejemplo.com
ftp://ftp.ejemplo.com:
ftp://anonymous:contraseña@ftp.ejemplo.com
file:///ruta/al/archivo.txt
feed://www.ejemplo.com/feed.xml"""
print("Validando urls: ",remove_urls(texto_original))
