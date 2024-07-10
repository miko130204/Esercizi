class Documento:
    def __init__(self, testo: str):
        self.testo: str = testo
        
    def get_Text(self):
        return self.testo
    
    def setText(self, text: str):
        self.testo = text
    
    def isInText(self, keyword: str):
        if keyword in self.testo:
            return True
        else:
            return False
    
class Email(Documento):
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str):
        super().__init__(testo)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo
    
    def getMittente(self):
        return self.mittente
        
    def getDestinatario(self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setMittente(self, sender: str):
        self.mittente = sender
        
    def setDestinatario(self, reciever: str):
        self.destinatario = reciever
    
    def setTitolo(self, title: str):
        self.titolo = title
    
    def getText(self):
        print (f"Da: {self.mittente}, A: {self.destinatario}")
        print(f"Titolo: {self.titolo}")
        print(f"Messagio: {self.testo}")
        
    def writeToFile(self, file_path: str):
        with open(file_path, 'w') as file:
            file.write(self.getText())
        
    
class File(Documento):
    def __init__(self, nomePercorso: str):
        self.nomePercorso: str = nomePercorso
        self.testo: str = ""
        self.leggiTestoDaFile()
    
    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
            self.testo = file.read()
    
    def getText(self):
        return (f"Percorso: {self.nomePercorso}\n"
                f"Contenuto: {self.testo}")