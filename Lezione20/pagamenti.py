class Pagamento:
    def __init__(self):
        self.__importo = 0.0
        
    def get(self):
        return self.__importo
    
    def set(self, importo: float):
        self.__importo = importo
        
    def dettagliPagamento(self):
        importo_formattato = "{:.2f}".format(self.__importo)
        print(f"Importo del pagamento: €{importo_formattato}")

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()
    
    def dettagliPagamento(self):
        importo = self.get()
        importo_formattato = "{:.2f}".format(importo)
        print(f"Pagamento in contanti di: €{importo_formattato}")
        self.inPezziDa()
    
    def inPezziDa(self):
        importo = self.get()
        pezzi = {
            500: 0, 200: 0, 100: 0, 50: 0, 20: 0,
            10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0,
            0.2: 0, 0.1: 0, 0.05: 0, 0.01: 0
        }
        for valore in pezzi.keys():
            pezzi[valore] = int(importo // valore)
            importo = round(importo % valore, 2)
        
        for valore, quantita in pezzi.items():
            if quantita > 0:
                tipo = "banconota" if valore >= 5 else "moneta"
                print(f"{quantita} {tipo}/e da {valore} euro")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare: str, scadenza: str, numero: str):
        super().__init__()
        self.titolare = titolare
        self.scadenza = scadenza
        self.numero = numero
    
    def dettagliPagamento(self):
        importo_formattato = "{:.2f}".format(self.get())
        print(f"Pagamento di: €{importo_formattato} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.titolare}")
        print(f"Data di scadenza: {self.scadenza}")
        print(f"Numero della carta: {self.numero}")

# test
pagamento1 = PagamentoContanti()
pagamento1.set(150.00)
pagamento1.dettagliPagamento()
print()
pagamento2 = PagamentoContanti()
pagamento2.set(95.25)
pagamento2.dettagliPagamento()
print()
pagamento3 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
pagamento3.set(200.00)
pagamento3.dettagliPagamento()
print()
pagamento4 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "6543210987654321")
pagamento4.set(500.00)
pagamento4.dettagliPagamento()
