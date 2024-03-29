class Exames:
    def __init__(self):
        self._exames = {
           "Exames": ["Hemograma", "Glicose", "Ureia", "Blastomicose", "Paratormonio"],
           "Sigla" : ["HEMO", "GLI", "URE", "BLAST", "PTH" ],
           "Seção" : ["HE", "BIO", "BIO", "IMU", "HOR"],
           "Descrição": ["Teste01", "Teste02" , "Teste03" , "Teste04", "Teste05"] 
        }
    
    def searchExames(self, exameInput):
        exameInput = input(exameInput)
        index = 0;
        if(exameInput not in self._exames["Exames"]):
            print("Nao foi possivel localizar o exame!")
        else:
            for key in self._exames.keys():
                if(key == "Exames"):
                    for exame in range(len(self._exames[key])):
                        if(exameInput == self._exames[key][exame]):
                            index = exame
                            exameObj = {}
                            break
                exameObj[key] = self._exames[key][index]
                print(self._exames[key][index])
                
                        
              