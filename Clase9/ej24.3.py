mensajes = ["Hola, como estas?", "Chau, no puedo ahora", "Chau amigo, después hablamos"]
mensajes_enviados = []

def enviar_mensajes(mensajes, mensajes_enviados):
    """Imprime cada mensaje y lo mueve a la lista de mensajes enviados."""
    while mensajes: 
        mensaje = mensajes.pop(0) 
        print(mensaje) 
        mensajes_enviados.append(mensaje)  

enviar_mensajes(mensajes[:], mensajes_enviados)


print("Lista de mensajes originales:", mensajes) 
print("Lista de mensajes enviados:", mensajes_enviados)  
