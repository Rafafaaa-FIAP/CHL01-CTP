from Modules.messages import Messages
messages = Messages()

class Exames:
    def __init__(self):
        self._exames = {
           "Exame": ["hemograma", "glicose", "ureia", "blastomicose", "paratormonio"],
           "Sigla" : ["HEMO", "GLI", "URE", "BLAST", "PTH" ],
           "Seção" : ["HE", "BIO", "BIO", "IMU", "HOR"],
           "Descrição": ["Teste01", "Teste02" , "Teste03" , "Teste04", "Teste05"] 
        }
    
    def searchExames(self, exameInput):
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Digite o nome do exame: \033[0m")
        exameInput = input(exameInput).lower()
        title = exameInput.upper()
        index = 0
        if(exameInput not in self._exames["Exame"]):
            messages.errorMessages("empty")
            messages.spaceDivisor(3)
        else:
            messages.applicationDivisor()
            for key in self._exames.keys():
                if(key == "Exame"):
                    for exame in range(len(self._exames[key])):
                        if(exameInput == self._exames[key][exame]):
                            index = exame
                            exameObj = {}
                            break
                exameObj[key] = self._exames[key][index]
            messages.optionMessage(f"\033[1;34m {title} \033[0m")
            messages.optionMessage(f"""
Exame:{exameObj["Exame"]}
Sigla:{exameObj["Sigla"]}
Seção:{exameObj["Seção"]}
Descrição:{exameObj["Descrição"]}
                                   """)
            messages.spaceDivisor(3)
        return
            
                
                        
              