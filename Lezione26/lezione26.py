from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave):
        self.chiave = chiave

    def _sposta_carattere(self, c, direzione):
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            return chr((ord(c) - offset + direzione * self.chiave) % 26 + offset)
        return c

    def codifica(self, testoInChiaro):
        return ''.join(self._sposta_carattere(c, 1) for c in testoInChiaro)

    def decodifica(self, testoCodificato):
        return ''.join(self._sposta_carattere(c, -1) for c in testoCodificato)

    def leggi_da_file(self, percorso):
        with open(percorso, 'r') as file:
            return file.read()

    def scrivi_su_file(self, percorso, testo):
        with open(percorso, 'w') as file:
            file.write(testo)
            
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n):
        self.n = n

    def _combinazione(self, testo):
        meta = (len(testo) + 1) // 2
        prima_meta = testo[:meta]
        seconda_meta = testo[meta:]
        combinato = []
        for i in range(meta):
            combinato.append(prima_meta[i])
            if i < len(seconda_meta):
                combinato.append(seconda_meta[i])
        return ''.join(combinato)

    def _decodifica_combinazione(self, testo):
        meta = (len(testo) + 1) // 2
        prima_meta = testo[::2]
        seconda_meta = testo[1::2]
        return prima_meta + seconda_meta

    def codifica(self, testoInChiaro):
        risultato = testoInChiaro
        for _ in range(self.n):
            risultato = self._combinazione(risultato)
        return risultato

    def decodifica(self, testoCodificato):
        risultato = testoCodificato
        for _ in range(self.n):
            risultato = self._decodifica_combinazione(risultato)
        return risultato

    def leggi_da_file(self, percorso):
        with open(percorso, 'r') as file:
            return file.read()

    def scrivi_su_file(self, percorso, testo):
        with open(percorso, 'w') as file:
            file.write(testo)

#Test del Cifratore a Scorrimento
cifratore_scorrimento = CifratoreAScorrimento(3)
testo_in_chiaro = cifratore_scorrimento.leggi_da_file('testo_in_chiaro.txt')
testo_codificato = cifratore_scorrimento.codifica(testo_in_chiaro)
cifratore_scorrimento.scrivi_su_file('testo_codificato.txt', testo_codificato)
print(f'Testo codificato (scorrimento): {testo_codificato}')
testo_decodificato = cifratore_scorrimento.decodifica(testo_codificato)
print(f'Testo decodificato (scorrimento): {testo_decodificato}')

#Test del Cifratore a Combinazione
cifratore_combinazione = CifratoreACombinazione(3)
testo_in_chiaro = cifratore_combinazione.leggi_da_file('testo_in_chiaro.txt')
testo_codificato = cifratore_combinazione.codifica(testo_in_chiaro)
cifratore_combinazione.scrivi_su_file('testo_codificato.txt', testo_codificato)
print(f'Testo codificato (combinazione): {testo_codificato}')
testo_decodificato = cifratore_combinazione.decodifica(testo_codificato)
print(f'Testo decodificato (combinazione): {testo_decodificato}')
