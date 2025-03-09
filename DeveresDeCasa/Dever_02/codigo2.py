entrada = input("Escreva uma frase:\n")
if entrada == "":
  print("entrada está vazia.")
else : 
  numeroCaracteres = len(entrada)
  print(f"A frase possui {numeroCaracteres} caracteres")
  listaPalavras = entrada.split()
  numeroPalavras = len(listaPalavras)
  print(f"A frase possui {numeroPalavras} palavras")
  maiorPalavra = max(listaPalavras, key=len)
  print(f"A maior palavra é {maiorPalavra}")
  caracteresInvertidos = entrada[::-1]
  print(f"Os caracteres invertidos ficam: {caracteresInvertidos}")
  palavrasInvertidas = ' '.join(entrada.split()[::-1])
  print(f"As palavras invertidas ficam: {palavrasInvertidas}")
  entrada = entrada.upper()
  print(f"Frase em maiúscula fica: {entrada}")
  entrada = entrada.lower()
  print(f"Frase em minúscula fica: {entrada}")
  tupla = tuple(listaPalavras)
  print(f"A tupla fica: {tupla}")



print("fim da aplicação")