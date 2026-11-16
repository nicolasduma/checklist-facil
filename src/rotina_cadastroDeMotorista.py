from bancoDeDados import BancoDeDados
from repositorioMotorista import RepositorioMotorista

bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
bancoDeDados.conectar()

repositorioMotorista = RepositorioMotorista(bancoDeDados)

def validarNumero(valor):
  try:
    numero = int(valor)

    if (numero > 0):
      return True
    
    return False
  
  except ValueError:
    return False

def validarRespostaPreDefinida(resposta, lista):
  respostaEhUmNumeroPositivo = validarNumero(resposta)

  if respostaEhUmNumeroPositivo == False or int(resposta) > len(lista):
    return False
  
  return True

def solicitarRespostaPreDefinida(titulo, etiqueta, lista):
  print()

  print(f"--- {titulo} ---")

  for indice in range(len(lista)):
    print(f"[{indice + 1}] - {lista[indice]}")
  print()

  estaNumeroValidado = False
  numero = None

  while estaNumeroValidado == False:
    numero = input(f"Digite o número do {etiqueta}: ")

    estaNumeroValidado = validarRespostaPreDefinida(numero, lista)

    if estaNumeroValidado == False:
      print("Número digitado é inválido!")
      print()
    else:
      numero = int(numero)
  
  return lista[numero - 1]

def validarRespostaDeSimOuNao(resposta):
  if (resposta == "s" or resposta == "n"):
    return True
  return False

def solicitarRespostaDeSimOuNao(etiqueta):
  print()

  estaRespostaValidada = False
  resposta = None

  while estaRespostaValidada == False:
    resposta = input(f"{etiqueta} [s/n]  ")

    estaRespostaValidada = validarRespostaDeSimOuNao(resposta)

    if estaRespostaValidada == False:
      print("Resposta inválida! Responda 's' para sim e 'n' para não.")
      print()
  
  if (resposta == "s"):
    return True
  
  return False

def solicitarRespostaNumerica(etiqueta):
  print()

  estaRespostaValidada = False
  resposta = None

  while estaRespostaValidada == False:
    resposta = input(f"{etiqueta}: ")

    estaRespostaValidada = validarNumero(resposta)

    if estaRespostaValidada == False:
      print("Resposta inválida! Digite um número.")
      print()
    else:
      resposta = int(resposta)
    
  return resposta

def solicitarRespostaTextual(etiqueta):
  print()

  estaRespostaValidada = False
  resposta = None

  while estaRespostaValidada == False:
    resposta = input(f"{etiqueta}: ")

    estaRespostaValidada = len(resposta) > 1

    if estaRespostaValidada == False:
      print("Resposta inválida! Digite um texto válido.")
      print()
    else:
      resposta = resposta
    
  return resposta

print("\n ========= Cadastro de motorista ========= ")

deveContinuar = True

while deveContinuar:
  print()
  nome = solicitarRespostaTextual("Digite o nome do motorista")
  matricula = solicitarRespostaNumerica("Digite a matrícula")
  senha = solicitarRespostaTextual("Digite a senha")

  resultadoDaCriacao = repositorioMotorista.criar(nome, matricula, senha)

  if (resultadoDaCriacao["foiBemSucedido"]):
    print("\n ---", resultadoDaCriacao["mensagem"], "\n")
  else:
    print("\n --- Houve um erro e não foi possivel cadastrar o motorista.")

  deveContinuar = solicitarRespostaDeSimOuNao("Deseja cadastrar outro motorista?")

  if deveContinuar == False:
    print()
    break
