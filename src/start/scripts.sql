-- CRIAÇÃO DO BANCO DE DADOS

CREATE DATABASE checklist_facil;

USE checklist_facil;

-- CRIAÇÃO DAS TABELAS

CREATE TABLE veiculo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    placa VARCHAR(7) UNIQUE NOT NULL,
    kmAtual INT NOT NULL
);

CREATE TABLE motorista (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    matricula VARCHAR(8) UNIQUE NOT NULL,
    senha VARCHAR(80) NOT NULL
);

CREATE TABLE viagem (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idDoVeiculo INT NOT NULL,
    idDoMotorista INT NOT NULL,
    status BOOLEAN DEFAULT 1, -- 1 = EM ANDAMENTO ; 0 = FINALIZADO
    destino VARCHAR(80) NOT NULL,

    FOREIGN KEY(idDoVeiculo) REFERENCES veiculo(id),
    FOREIGN KEY(idDoMotorista) REFERENCES motorista(id)
);

CREATE TABLE checkList (
    id INT PRIMARY KEY AUTO_INCREMENT,
    idDaViagem INT NOT NULL,
    data_hora DATETIME NOT NULL,
    quilometragem INT NOT NULL,
    tipo CHAR NOT NULL,
    estado_pneus BOOLEAN NOT NULL,
    estado_farois BOOLEAN NOT NULL,
    estado_parabrisa BOOLEAN NOT NULL,
    estado_nivel_oleo BOOLEAN NOT NULL,
    estado_nivel_agua_radiador BOOLEAN NOT NULL,
    estado_nivel_combustivel BOOLEAN NOT NULL,
    estado_lataria BOOLEAN NOT NULL,
    observacoes VARCHAR(150),

    FOREIGN KEY(idDaViagem) REFERENCES viagem(id)
)
