def vencedor_posicao(a, b, c):
    posicoes = {'Bob': a, 'Rex': b, 'Oli': c}
    dist_bob_oli = abs(posicoes['Bob'] - posicoes['Oli'])
    dist_rex_oli = abs(posicoes['Rex'] - posicoes['Oli'])
    
    if dist_bob_oli < dist_rex_oli:
        return 'Bob'
    elif dist_rex_oli < dist_bob_oli:
        return 'Rex'
    else:
        return 'Oli'