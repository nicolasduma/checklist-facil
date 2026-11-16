import mysql.connector

class RepositorioVeiculo:
  _bancoDeDados = None
  _conexaoDoBancoDeDados = None
  _cursorDoBancoDeDados = None
  _nomeDaTabela = "veiculo"

  def __init__(self, bancoDeDados):
    self._bancoDeDados = bancoDeDados
    self._conexaoDoBancoDeDados = bancoDeDados.getConexao()
    self._cursorDoBancoDeDados = bancoDeDados.getConexao().cursor()
    
  def criar(self, placa, kmAtual):
    resultado = None
    sql = f"INSERT INTO {self._nomeDaTabela} (placa, kmAtual) VALUES (%s, %s)"

    try:
      self._cursorDoBancoDeDados.execute(sql, (placa, kmAtual))
      self._conexaoDoBancoDeDados.commit()
      resultado = {"foiBemSucedido": True, "mensagem": "O veículo foi cadastrado com sucesso."}

    except mysql.connector.IntegrityError as erro:
      self._conexaoDoBancoDeDados.rollback()

      if erro.errno == 1062:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_VEICULO_01", "mensagem": f"A placa '{placa}' já está cadastrada."}
      else:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
      
    except Exception as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
    
    return resultado

  def listarTodos(self):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela}"

    try:
      self._cursorDoBancoDeDados.execute(sql)
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      veiculos = [dict(zip(colunas, registro)) for registro in registros]

      resultado = {"foiBemSucedido": True, "dados": veiculos}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": f"Houve um erro no banco de dados."}
    
    return resultado
