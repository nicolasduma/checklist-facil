from repositorioMotorista import RepositorioMotorista
from bancoDeDados import BancoDeDados

def testarCriacaoDeMotorista():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioMotorista = RepositorioMotorista(bancoDeDados)

  resultado = repositorioMotorista.criar("João da Silva", "500", "senha1234")

  assert resultado["foiBemSucedido"] is True

def testarRestricaoParaCriarVeiculoComPlacaDuplicada():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioMotorista = RepositorioMotorista(bancoDeDados)

  resultado = repositorioMotorista.criar("João da Silva", "300", "senha1234")

  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_MOTORISTA_01"

def testarErroAlternativoParaCriarVeiculo():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioMotorista = RepositorioMotorista(bancoDeDados)

  resultado = repositorioMotorista.criar("João da Silva", "123456789", "senha1234")

  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_01"

def testarListagemDeMotorista():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioMotorista = RepositorioMotorista(bancoDeDados)

  resultado = repositorioMotorista.listarTodos()

  assert resultado["foiBemSucedido"] is True
  assert resultado["dados"][0]["nome"] == "João da Silva"
