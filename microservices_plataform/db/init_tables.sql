CREATE TABLE IF NOT EXISTS planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    duracao_meses INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS checkins (
    id SERIAL PRIMARY KEY,
    aluno_id INT,
    data_checkin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    duracao INT, 
    tipo_atividade VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    frequencia_semanal INT,
    ultimo_checkin_id INT,
    tipo_plano INT
);

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'fk_ultimo_checkin') THEN
        ALTER TABLE alunos ADD CONSTRAINT fk_ultimo_checkin FOREIGN KEY (ultimo_checkin_id) REFERENCES checkins(id);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'fk_tipo_plano') THEN
        ALTER TABLE alunos ADD CONSTRAINT fk_tipo_plano FOREIGN KEY (tipo_plano) REFERENCES planos(id);
    END IF;

    IF NOT EXISTS (SELECT 1 FROM information_schema.table_constraints WHERE constraint_name = 'fk_aluno_checkin') THEN
        ALTER TABLE checkins ADD CONSTRAINT fk_aluno_checkin FOREIGN KEY (aluno_id) REFERENCES alunos(id);
    END IF;
END$$;

INSERT INTO planos (nome, descricao, preco, duracao_meses)
SELECT * FROM (VALUES
  ('Plano Básico', 'Acesso em horário comercial', 99.90, 1),
  ('Plano Padrão', 'Acesso integral e aulas coletivas', 149.90, 3),
  ('Plano Premium', 'Acesso integral, aulas e personal trainer', 249.90, 6)
) AS p(nome, descricao, preco, duracao_meses)
WHERE NOT EXISTS (SELECT 1 FROM planos);

DO $$
DECLARE
  i INT := 1;
  total_alunos INT := 100;
  plano_id INT;
  new_aluno_id INT;
  checkin_id INT;
  j INT;
  total_checkins INT;
  ult_checkin_id INT;

BEGIN
  FOR i IN 1..total_alunos LOOP
    SELECT id INTO plano_id FROM planos ORDER BY random() LIMIT 1;

    INSERT INTO alunos (nome, frequencia_semanal, tipo_plano)
    VALUES (
      'Aluno ' || i,
      (FLOOR(random() * 6) + 1)::INT,
      plano_id
    )
    RETURNING id INTO new_aluno_id;

    total_checkins := (FLOOR(random() * 11))::INT;

    FOR j IN 1..total_checkins LOOP
      INSERT INTO checkins (aluno_id, data_checkin, duracao, tipo_atividade)
      VALUES (
        new_aluno_id,
        NOW() - (INTERVAL '1 day' * (FLOOR(random() * 180))),
        (FLOOR(random() * 120) + 30)::INT,
        CASE WHEN random() < 0.5 THEN 'Musculação' ELSE 'Cardio' END
      )
      RETURNING id INTO checkin_id;
    END LOOP;

    IF total_checkins > 0 THEN
      SELECT id INTO ult_checkin_id FROM checkins WHERE aluno_id = new_aluno_id ORDER BY data_checkin DESC LIMIT 1;
      UPDATE alunos SET ultimo_checkin_id = ult_checkin_id WHERE id = new_aluno_id;
    END IF;
  END LOOP;
END$$;
