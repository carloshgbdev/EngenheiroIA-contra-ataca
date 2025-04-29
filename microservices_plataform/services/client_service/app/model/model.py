from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    frequencia_semanal = Column(Integer)
    ultimo_checkin_id = Column(Integer, ForeignKey("checkins.id"), nullable=True)
    tipo_plano = Column(Integer, ForeignKey("planos.id"))

    ultimo_checkin = relationship("Checkin", foreign_keys=[ultimo_checkin_id])

    checkins = relationship("Checkin", back_populates="aluno", foreign_keys="Checkin.aluno_id")

    plano = relationship("Plano", back_populates="alunos", foreign_keys=[tipo_plano])

class Checkin(Base):
    __tablename__ = 'checkins'

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    data_checkin = Column(TIMESTAMP, server_default=func.now())
    duracao = Column(Integer)
    tipo_atividade = Column(String(100))

    aluno = relationship("Aluno", back_populates="checkins", foreign_keys=[aluno_id])

class Plano(Base):
    __tablename__ = 'planos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(500))
    preco = Column(Integer)
    duracao_meses = Column(Integer)

    alunos = relationship("Aluno", back_populates="plano")
