tit = (' CONVERSOR DE MEDIDAS ')
fim = (' FIM DO PROGRAMA ')
print('{:-^48}' .format(tit))
metros = float(input('Digite uma medida em metros: '))
conv_km = metros / 1000
conv_hm = metros / 100
conv_dam = metros / 10
conv_dm = int(metros * 10)
conv_cen = int(metros * 100)
conv_mil = int(metros * 1000)
print('{} metros, equivalem a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm' .format(metros, conv_km, conv_hm, conv_dam, conv_dm, conv_cen, conv_mil))
print('{:-^48}' .format(fim))