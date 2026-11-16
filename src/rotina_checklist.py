from bancoDeDados import BancoDeDados
from repositorioMotorista import RepositorioMotorista
from repositorioVeiculo import RepositorioVeiculo
from repositorioViagem import RepositorioViagem
from repositorioChecklist import RepositorioChecklist
from datetime import datetime

bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
bancoDeDados.conectar()

repositorioMotorista = RepositorioMotorista(bancoDeDados)
repositorioVeiculo = RepositorioVeiculo(bancoDeDados)
repositorioViagem = RepositorioViagem(bancoDeDados)
repositorioChecklist = RepositorioChecklist(bancoDeDados)


listagemDeMotoristas = repositorioMotorista.listarTodos()["dados"]
listagemDeVeiculos = repositorioVeiculo.listarTodos()["dados"]

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

def solicitarRespostaPreDefinida2(titulo, etiqueta, lista, tituloDoIndice):
  print()

  print(f"--- {titulo} ---")

  for indice in range(len(lista)):
    print(f"[{indice + 1}] - {lista[indice][f"{tituloDoIndice}"]}")
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

def solicitarRespostaDeSimOuNao(item):
  print()

  estaRespostaValidada = False
  resposta = None

  while estaRespostaValidada == False:
    resposta = input(f"{item} está apto para operação? [s/n]  ")

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

def solicitarRespostaDeTexto(etiqueta):
  print()

  estaRespostaValidada = False
  resposta = None

  while estaRespostaValidada == False:
    resposta = input(f"{etiqueta}: ")

    estaRespostaValidada = len(resposta) > 5

    if estaRespostaValidada == False:
      print("Resposta inválida! Digite um texto com mais de 5 caractéres.")
      print()
    
  return resposta

print()
print(" ========= Check-list Fácil ========= ")

veiculo = solicitarRespostaPreDefinida2("Veículos cadastrados", "veículo", listagemDeVeiculos, "placa")
motorista = solicitarRespostaPreDefinida2("Motoristas cadastrados", "motorista", listagemDeMotoristas, "nome")
destino = solicitarRespostaDeTexto("Destino")
quilometragem = solicitarRespostaNumerica("Digite a quilometragem de veículo")
situacaoParabrisa = solicitarRespostaDeSimOuNao("Parabrisa")
situacaoLimpeza = solicitarRespostaDeSimOuNao("Limpeza")
situacaoLataria = solicitarRespostaDeSimOuNao("Lataria")
situacaoPneus = solicitarRespostaDeSimOuNao("Pneus")
situacaoDosFarois = solicitarRespostaDeSimOuNao("Faróis")
situacaoNivelDeOleo = solicitarRespostaDeSimOuNao("Nível de óleo do motor")
situacaoNivelDeAguaDoRadiador = solicitarRespostaDeSimOuNao("Nível de água do radiador")
situacaoNivelDeCombustivel = solicitarRespostaDeSimOuNao("Nivel de combustível")
situacaoLataria = solicitarRespostaDeSimOuNao("Nivel de combustível")
observacoes = solicitarRespostaDeTexto("Observações")

def salvar():
  resultadoDaCriacaoDaViagem = repositorioViagem.criar(veiculo["id"], motorista["id"], destino)

  if (resultadoDaCriacaoDaViagem["foiBemSucedido"]):
    resultadoDaCriacaoDoChecklist = repositorioChecklist.criar(resultadoDaCriacaoDaViagem["dados"], datetime.now(), quilometragem, "s", situacaoPneus, situacaoDosFarois, situacaoParabrisa, situacaoNivelDeOleo, situacaoNivelDeAguaDoRadiador,  situacaoNivelDeCombustivel, situacaoLataria, observacoes)
    
    if resultadoDaCriacaoDoChecklist["foiBemSucedido"]:
      print(" ========= Check-list registrado com sucesso! ========= ")
      return
    else:
      print("--- Houve um erro e o check-list não foi registrado!")
    
  else:
    print("\n--- Houve um erro e o check-list não foi registrado!")
    
print()
salvar()
print()
