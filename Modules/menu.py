from Modules.messages import Messages

messages = Messages()
class Menu:

    def __init__(self):
        self._menu = {
            "Options": ["1", "2", "3", "4", "0"],
            "Functionalities": ["Contato", "Localização","Busca exames", "Área Kids", "Sair do sistema"]
        }
    
    def showMenuApplication(self):
        messages.welcomeMessage()
        messages.applicationDivisor()
        messages.optionMessage("\033[1;34m Selecione uma das opções disponíveis: \033[0m")

        for i in range(len(self._menu["Options"])):
            print(f"\033[92m{self._menu['Options'][i]}\033[0m - {self._menu['Functionalities'][i]}")


        messages.applicationDivisor()

        return self.inputValidation("", self._menu["Options"])
    

    def inputValidation(self, optionInput, possibleOptions, action = "option"):
        messages.optionMessage("\033[1;34m Sua opção: \033[0m")
        option = input(optionInput)
        while (option not in possibleOptions):
            messages.errorMessages(action)
            option = input(optionInput)
        return option

    def verifyOption(self, selectedOption):
        if(selectedOption == "1"): 
            messages.applicationDivisor()
            messages.optionMessage("\033[1;34m Contato InfoCR \033[0m")
            messages.applicationDivisor()

        if(selectedOption == "2"): return print("Logica para 2")
        if(selectedOption == "3"): return print("Logica para 3")
        if(selectedOption == "4"): return print("Logica para 4")



           
        






   
