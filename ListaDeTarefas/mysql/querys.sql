CREATE DATABASE listadetarefas;

CREATE TABLE usuarios(
	id int not null PRIMARY KEY AUTO_INCREMENT,
    nome varchar(150) not null,
    senha varchar(32) not null
    email VARCHAR(120)
);


CREATE TABLE tarefas(
	id_tarefa int not null PRIMARY KEY AUTO_INCREMENT,
    id_usuario int not null,
    tarefa varchar(60) not null,
    descricao text
);