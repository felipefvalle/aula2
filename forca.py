def forca():
    palavra_secreta = "senac"
    letras_acertadas = ''
    tentativas = 0

    print("Jogo da Forca!")
    while True:
        
        letra_digitada = input(f"Tentativa {tentativas}: Digite uma letra: ")

        palavra_formada =''
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada


        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada  += letra_secreta
            else:
                palavra_formada += '*'
        tentativas += 1

        print(f"Palavra Formada: {palavra_formada}")
        
        if palavra_formada == palavra_secreta:
            print(f"\n\tFim de Jogo!\n\n A palavra era {palavra_formada}.\n Você acertou na {tentativas} tentativa!\n")
            letras_acertadas = ''
            break
        
forca()

