# O problema do cartão de crédito lá Puff.
# 1) Objetivo: usuário vai inserir os números do cartão e o programa vai responder se o número é inválido OU, se válido, de qual bandeira.
# 2) Amex tem 15 dígitos. Mastercard tem 16 dígitos. Visa tem 13 ou 16 dígitos.
# 3) Amex os números começam com 34 ou 37. Mastercard os números começam com 51, 52, 53, 54, ou 55 (nesse exemplo, pq eles trabalham com outras numerações); e Visa começa com 4.
# 4) Validação do número:
#
# - Multiplicar cada outro número por 2, começando pelo penultimo dígito.
# Ex: Se o número for 4003600000000014, vc faz:
# [4]0[0]3[6]0[0]0[0]0[0]0[0]0[1]4
# (4*2) + (0*2) + (6*2) + (0*2) + (0*2) + (0*2) + (0*2) + (1*2)
# 8 + 0 + 12 + 0 + 0 + 0 + 2

# Alguns cartões válidos:
# Mastercard: 5110305538901234
# Mastercard: 5510305138901234
# Visa: 4612045678901232
# Amex: 341214567880120

def validaNumero(cartao):
    mult = 0
    soma = 0
    for i in range(0,len(cartao),2):
        mult += int(cartao[i]) * 2
    for i in range(1,len(cartao),2):
        soma += int(cartao[i])
    if(mult % soma == 0):
        return True
    return False


def validaBandeira(cartao):
    if((len(cartao) == 13) and cartao[:1] == '4'):
        return 'Visa'
    elif((len(cartao) == 15) and (cartao[:2]) in ['34','37']):
        return 'Amex'
    elif(len(cartao) == 16):
        if(cartao[:1] == '4'):
            return 'Visa'    
        elif(cartao[:2] in ['51','52','53','54','55']):
            return 'Mastercard'
    return False


def main():
    cartao = input('Digite o Numero do seu Cartão:').strip()
    if(validaNumero(cartao)):
        bandeira = validaBandeira(cartao)
        print('Cartão', (bandeira + ' válido.' if (bandeira) else 'inválido.')) 
    else:
        print('Cartão inválido.')


main()