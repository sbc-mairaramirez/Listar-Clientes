#Interfaz del repositorio (puerto de salida)
#define lo que un repositorio debe implementar
class ClienteRepositoryInterface:
    def listar(self):
        #metodo abstracto que debe implementarse en una clase concreta
        raise NotImplementedError
