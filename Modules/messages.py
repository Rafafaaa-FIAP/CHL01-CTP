class Messages:

    @staticmethod
    def welcomeMessage():
        return print(" \033[1;34m Bem-vindo ao sistema InfoCR \033[0m")
    
    @staticmethod
    def byeMessage():
        link = "https://infocr.vercel.app/"
        print(" \033[1;34m Obrigado por utilizar o sistema InfoCR! \033[0m\n")
        print(f"\033[1;34m Para uma melhor experiência, acesse:\033[0m \033[92m{link}\033[0m")
        return 
    

    @staticmethod
    def applicationDivisor():
        return print("****************************************************************************************************")
    


    @staticmethod
    def optionMessage(message):
        return print(message)
    

    @staticmethod
    def errorMessages(error):
        if(error == "option"): return print("\033[91m Opção inválida\033[0m")
        if(error == "type"): return print("\033[91m Opção inválida\033[0m")
            
     