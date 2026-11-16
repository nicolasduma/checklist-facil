import mysql.connector

class RepositorioViagem:
  _bancoDeDados = None
  _conexaoDoBancoDeDados = None
  _cursorDoBancoDeDados = None
  _nomeDaTabela = "viagem"

  def __init__(self, bancoDeDados):
    self._bancoDeDados = bancoDeDados
    self._conexaoDoBancoDeDados = bancoDeDados.getConexao()
    self._cursorDoBancoDeDados = bancoDeDados.getConexao().cursor()

  def listarComStatusAbertoPorIdDoVeiculo(self, idDoVeiculo):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela} WHERE idDoMotorista = %s AND status = 1"

    try:
      self._cursorDoBancoDeDados.execute(sql, (idDoVeiculo,))
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      viagens = [dict(zip(colunas, registro)) for registro in registros]

      if viagens:
        resultado = {"foiBemSucedido": True, "dados": viagens[0]}
      else:
        # Não encontrar viagem aberta NÃO é um erro de banco de dados,
        # então a consulta foi bem-sucedida, apenas sem dados.
        resultado = {"foiBemSucedido": True, "dados": None}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}
    return resultado

  def criar(self, idDoVeiculo, idDoMotorista, destino):
    resultado = None

    resultadoDaListagemComStatusAberto = self.listarComStatusAbertoPorIdDoVeiculo(idDoVeiculo)

    if not resultadoDaListagemComStatusAberto["foiBemSucedido"]:
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}
      return resultado
    elif resultadoDaListagemComStatusAberto["dados"] is not None:
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_VIAGEM_01", "mensagem": "O veículo já está em uma viagem aberta, finalize a viagem antes de criar uma nova."}
      return resultado

    sql = f"INSERT INTO {self._nomeDaTabela} (idDoVeiculo, idDoMotorista, destino) VALUES (%s, %s, %s)"

    try:
      self._cursorDoBancoDeDados.execute(sql, (idDoVeiculo, idDoMotorista, destino))
      self._conexaoDoBancoDeDados.commit()
      idCriado = self._cursorDoBancoDeDados.lastrowid
      resultado = {"foiBemSucedido": True, "mensagem": "A viagem foi cadastrada com sucesso.", "dados": idCriado}

    except mysql.connector.IntegrityError as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")

      if erro.errno == 1452:
        resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_VIAGEM_02", "mensagem": "O veículo ou motorista não está cadastrado."}
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
      viagens = [dict(zip(colunas, registro)) for registro in registros]

      resultado = {"foiBemSucedido": True, "dados": viagens}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}

    return resultado

  def listarPorId(self, id):
    resultado = None
    sql = f"SELECT * FROM {self._nomeDaTabela} WHERE id = %s"

    try:
      self._cursorDoBancoDeDados.execute(sql, (id,))
      registros = self._cursorDoBancoDeDados.fetchall()

      colunas = [desc[0] for desc in self._cursorDoBancoDeDados.description]
      viagens = [dict(zip(colunas, registro)) for registro in registros]

      if viagens:
        resultado = {"foiBemSucedido": True, "dados": viagens[0]}
      else:
        # Não encontrar a viagem por id NÃO é um erro de banco de dados.
        resultado = {"foiBemSucedido": True, "dados": None}
    except Exception as erro:
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}
    return resultado

  def alterarStatusParaFinalizadoPeloId(self, id):
    resultado = None
    sql = f"UPDATE {self._nomeDaTabela} SET status = 0 WHERE id = %s AND status = 1"

    try:
      self._cursorDoBancoDeDados.execute(sql, (id,))
      self._conexaoDoBancoDeDados.commit()
      resultado = {"foiBemSucedido": True, "mensagem": "O status da viagem foi alterado para finalizado com sucesso."}

    except Exception as erro:
      self._conexaoDoBancoDeDados.rollback()
      print(f"\n{erro}")
      resultado = {"foiBemSucedido": False, "codigoDeErro": "BD_01", "mensagem": "Houve um erro no banco de dados."}

    return resultado
