from bancoDeDados import BancoDeDados

nomeDeBancoDeDadosValido = "checklist_facil"
nomeDeBancoDeDadosInvalido = "banco_de_dados_que_nao_existe"

# Testar conexão com credenciais válidas
def testarConexao():
  bancoDeDados = BancoDeDados("localhost", nomeDeBancoDeDadosValido, "root", "root")

  conexaoAconteceu = bancoDeDados.conectar()

  conexao = bancoDeDados.getConexao()

  assert conexaoAconteceu is True
  assert conexao is not None

  conexao.close()

# Testar restrição de conexão com credenciais inválidas
def testarConexaoInvalida():
  bancoDeDados = BancoDeDados("localhost", nomeDeBancoDeDadosInvalido, "root", "root")

  conexaoAconteceu = bancoDeDados.conectar()
  conexao = bancoDeDados.getConexao()

  assert conexaoAconteceu is False
  assert conexao is None

# Testar restrição de conexão duplicada
def testarRestricaoDeConexaoDuplicada():
  bancoDeDados = BancoDeDados("localhost", nomeDeBancoDeDadosValido, "root", "root")

  bancoDeDados.conectar()
  conexaoDuplicadaAconteceu = bancoDeDados.conectar()

  conexao = bancoDeDados.getConexao()

  assert conexaoDuplicadaAconteceu is False

  conexao.close()

# Testar fechamento de conexão
def testarFechamentoDaConexao():
  bancoDeDados = BancoDeDados("localhost", nomeDeBancoDeDadosValido, "root", "root")

  bancoDeDados.conectar()
  conexao = bancoDeDados.getConexao()
  bancoDeDados.fecharConexao()

  assert conexao.is_connected() is False
  assert bancoDeDados.getConexao() is None
