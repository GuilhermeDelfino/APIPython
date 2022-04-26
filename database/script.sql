CREATE DATABASE Agenda;
USE Agenda;

CREATE TABLE Usuario(
	idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45)
);
CREATE TABLE Telefone(
	idTelefone INT PRIMARY KEY AUTO_INCREMENT,
    numero CHAR(11),
    fkUsuario INT,
    FOREIGN KEY(fkUsuario) REFERENCES Usuario(idUsuario)
);
