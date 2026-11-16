import mysql.connector

class RepositorioChecklist:
  _bancoDeDados = None
  _conexaoDoBancoDeDados = None
  _cursorDoBancoDeDados = None
  _nomeDaTabela = "checkList"

  def __init__(self, bancoDeDados):
    self._bancoDeDados = bancoDeDados
    self._conexaoDoBancoDeDados = bancoDeDados.getConexao()
    self._cursorDoBancoDeDados = bancoDeDados.getConexao().cursor()

  def criar(self, idDaViagem, data_hora, quilometragem, tipo, estado_pneus, estado_farois, estado_parabrisa, estado_nivel_oleo, estado_nivel_agua_radiador, estado_nivel_combustivel, estado_lataria, observacoes):
    resultado = None
    sql = f"INSERT INTO {self._nomeDaTabela} (idDaViagem, data_hora, quilometragem, tipo, estado_pneus, estado_farois, estado_parabrisa, estado_nivel_oleo, estado_nivel_agua_radiador, estado_nivel_combustivel, estado_lataria, observacoes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    try:
      self._cursorDoBancoDeDados.execute(sql, (idDaViagem, data_hora, quilometragem, tipo, estado_pneus, estado_farois, estado_parabrisa, estado_nivel_oleo, estado_nivel_agua_radiador, estado_nivel_combustivel, estado_lataria, observacoes))
      self._conexaoDoBancoDeDados.commit()
      resultado = {"foiBemSucedido": True, "mensagem": "O check-list foi cadastrado com sucesso."}

    except mysql.connector.IntegrityError as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")

      if erro.errno == 1452:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_CHECKLIST_01", "mensagem": "A viagem informada não está cadastrada."}
      else:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}

    except Exception as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}

    return resultado

  def listarTodos(self):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela}"

    try:
      self._cursorDoBancoDeDados.execute(sql)
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      checklists = [dict(zip(colunas, registro)) for registro in registros]

      resultado = {"foiBemSucedido": True, "dados": checklists}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}

    return resultado

  def listarPorId(self, idDaViagem):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela} WHERE idDaViagem = %s"

    try:
      self._cursorDoBancoDeDados.execute(sql, (idDaViagem,))
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      checklists = [dict(zip(colunas, registro)) for registro in registros]

      if checklists:
        resultado = {"foiBemSucedido": True, "dados": checklists[0]}
      else:
        # Não encontrar o checklist por id da viagem NÃO é um erro de banco de dados.
        resultado = {"foiBemSucedido": True, "dados": None}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}
    return resultado
