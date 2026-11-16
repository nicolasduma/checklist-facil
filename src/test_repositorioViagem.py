from repositorioViagem import RepositorioViagem
from bancoDeDados import BancoDeDados

def testarListagemComStatusAbertoPorIdDoVeiculo():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.listarComStatusAbertoPorIdDoVeiculo(1)

  print(resultado)
  assert resultado["foiBemSucedido"] is True
  assert resultado["dados"]["id"] is 1

def testarCriacaoDeViagem():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.criar(1, 12, "Fazenda")

  assert resultado["foiBemSucedido"] is True

def testarRestricaoDeCriacaoDeViagemJaComStatusAberto():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.criar(1, 12, "Fazenda")

  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_VIAGEM_01"

def testarRestricaoDeCriacaoDeViagemComVeiculoOuMotoristaNaoCadastrado():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.criar(100, 1, "Fazenda")

  print(resultado)
  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_VIAGEM_02"

def testarListagemDeTodos():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.listarPorId(1)

  assert resultado["foiBemSucedido"] is True
  assert resultado["dados"]["id"] == 1

def testarListagemDeTodos():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.listarTodos()

  assert resultado["foiBemSucedido"] is True
  assert type(resultado["dados"]) == list

def testarAlteracaoDeStatusParaFinalizadoPorId():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioViagem = RepositorioViagem(bancoDeDados)

  resultado = repositorioViagem.alterarStatusParaFinalizadoPeloId(1)

  print(resultado)
  assert resultado["foiBemSucedido"] is True
