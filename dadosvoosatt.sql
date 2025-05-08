CREATE TABLE CompanhiaAerea (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Aviao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_voo VARCHAR(100) NOT NULL UNIQUE,
    companhia_id INTEGER NOT NULL,
    FOREIGN KEY (companhia_id) REFERENCES CompanhiaAerea(id)
);

CREATE TABLE Passageiros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    numero_voo VARCHAR(100) NOT NULL,
    FOREIGN KEY (numero_voo) REFERENCES Aviao(numero_voo)
);

CREATE TABLE Passagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passageiro_id INTEGER NOT NULL,
    aviao_id INTEGER NOT NULL,
    data_viagem DATE NOT NULL,
    FOREIGN KEY (passageiro_id) REFERENCES Passageiros(id),
    FOREIGN KEY (aviao_id) REFERENCES Aviao(id)
);

INSERT INTO CompanhiaAerea (nome) VALUES
('LATAM'),
('Gol'),
('Azul');

INSERT INTO Aviao (numero_voo, companhia_id) VALUES
('1234', 1),
('3456', 2),
('7890', 3);

INSERT INTO Passageiros (nome, numero_voo) VALUES
('João Paulo', '1234'),
('Oliveirax', '3456'),
('Mariane', '7890');

INSERT INTO Passagens (passageiro_id, aviao_id, data_viagem) VALUES
(1, 1, '2025-06-01'),
(2, 2, '2025-06-03'),
(3, 3, '2025-06-05');

--Listar o nome dos passageiros com nome da companhia e numero de voo
SELECT p.nome AS passageiro, a.numero_voo, c.nome AS companhia
FROM Passageiros p
JOIN Aviao a ON p.numero_voo = a.numero_voo
JOIN CompanhiaAerea c ON a.companhia_id = c.id;

--contar quantos passaageiros tem por companhia

SELECT c.nome AS companhia, COUNT(p.id) AS total_passageiros
FROM Passageiros p
JOIN Aviao a ON p.numero_voo = a.numero_voo
JOIN CompanhiaAerea c ON a.companhia_id = c.id
GROUP BY c.nome;

--voo mais proximos e o mais de longe

SELECT MIN(data_viagem) AS primeira_viagem, MAX(data_viagem) AS ultima_viagem
FROM Passagens;

INSERT INTO Passageiros (nome, numero_voo)
VALUES ('Carlos Eduardo', '1234');

DELETE FROM Passageiros
WHERE nome = 'Carlos Eduardo';

