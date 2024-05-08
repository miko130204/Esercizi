class Persona:

    def __init__(self, nome: str, cognome: str, codice_fiscale: str) -> None:
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale: str = codice_fiscale




persona_1: Persona = Persona(nome = "Miko", cognome = "Mrc", codice_fiscale = "MRCMLJ04")

print(persona_1.nome, persona_1.cognome, persona_1.codice_fiscale)