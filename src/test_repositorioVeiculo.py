from repositorioVeiculo import RepositorioVeiculo
from bancoDeDados import BancoDeDados

def testarCriacaoDeVeiculo():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioVeiculo = RepositorioVeiculo(bancoDeDados)

  resultado = repositorioVeiculo.criar("ABC1238", 300)

  assert resultado["foiBemSucedido"] is True

def testarRestricaoParaCriarVeiculoComPlacaDuplicada():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioVeiculo = RepositorioVeiculo(bancoDeDados)

  resultado = repositorioVeiculo.criar("ABC1234", 300)

  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_VEICULO_01"

def testarErroAlternativoParaCriarVeiculo():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioVeiculo = RepositorioVeiculo(bancoDeDados)

  resultado = repositorioVeiculo.criar("ABC-1234", 300)

  assert resultado["foiBemSucedido"] is False
  assert resultado["codigoDeErro"] is "BD_01"

def testarListagemDeVeiculos():
  bancoDeDados = BancoDeDados("localhost", "checklist_facil", "root", "root")
  bancoDeDados.conectar()

  repositorioVeiculo = RepositorioVeiculo(bancoDeDados)

  resultado = repositorioVeiculo.listarTodos()

  assert resultado["foiBemSucedido"] is True
  assert resultado["dados"][0]["placa"] == "ABC1234"
