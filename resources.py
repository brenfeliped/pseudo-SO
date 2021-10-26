class ControlaRecursos:
    impressoras = [True, True]
    scanner = True
    modem = True
    SATA = [True, True]

    def solicitaRecurso(self, numeroImpressora, scanner, modem, numeroDisco):
        if numeroImpressora > 0:
            if self.impressoras[numeroImpressora-1] == False:#Avalia disponibilidade da impressora solicitada
                return False
            else:
                self.impressoras[numeroImpressora-1] = False
        if scanner == 1:
            if self.scanner == False:#Avalia disponibilidade do scanner
                return False
            else:
                self.scanner = False
        if modem == 1:
            if self.modem == False:#Avalia disponibilidade do modem
                return False
            else:
                self.modem = False
        if numeroDisco > 0:
            if self.SATA[numeroDisco-1] == False:#Avalia disponibilidade do disco
                return False
            else:
                self.SATA[numeroDisco-1] = False

        return True
    
    def liberaImpressora(self, numeroImpressora):
        self.impressoras[numeroImpressora-1] = True

    def liberaScanner(self):
        self.scanner = True

    def liberaModem(self):
        self.modem = True

    def liberaDisco(self, numeroDisco):
        self.SATA[numeroDisco-1] = True

