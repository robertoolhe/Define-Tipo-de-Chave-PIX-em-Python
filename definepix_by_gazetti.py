#sub-Programa que identifica o tipo de chave PIX - by Gazetti

tam_chave = 0
chave_valida = False

#identifica o tipo de chave PIX

while chave_valida == False :
    chave = input('Digite a Chave PIX (ex.: cel.(##)99999-9999 ): ')
    tam_chave = len(chave)
    print('\n\n\n')
    
    if tam_chave == 14 and not '@' in chave :
        print('vc digitou um CNPJ!')
        chave_valida = True
    elif tam_chave > 14 and '-' in chave :
        print('vc digitou uma chave aleatória')
        chave_valida = True
    elif '@' in chave and '.' in chave :
        print('vc digitou um e-mail')
        chave_valida = True
    elif tam_chave == 11 :
        print('vc digitou um CPF! ')
        chave_valida = True
    elif '(' in chave[0] and ')' in chave[3] :
        print('vc digitou um telefone!')
        chave_valida = True
    else:
        print('chave inválida')
        chave_valida = False
