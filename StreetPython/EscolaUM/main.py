from random import randint
from datetime import datetime
import os
from pathlib import Path

ROOT_DIR = Path(os.path.abspath(os.path.curdir))


class RA:
    def __init__(self):
        self.data_emissao = datetime.now()
        self.__numeros_base = [randint(0, 9) for i in range(11)]

    @property
    def numeros(self):
        return ''.join(str(i) for i in self.__numeros_base)


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.ra = RA()
        self.__cursos_matriculados = []
        self.__inadimplente = False
        self.__matricula_ativa = False

    def ativar_matricula(self):
        self.__matricula_ativa = True

    def desativar_matricula(self):
        self.__matricula_ativa = False

    @property
    def status_matricula(self):
        return 'Matricula Ativa' if self.__matricula_ativa else 'Matricula Inativa'

    @property
    def status_inadimplencia(self):
        return 'Inadimplente' if self.__inadimplente else 'Sem débitos'

    @property
    def status_matricula_bool(self):
        return True if self.__matricula_ativa and not self.__inadimplente else False

    @property
    def listar_cursos_matriculados(self):
        return self.__cursos_matriculados

    def show_cursos_matriculados(self):
        for i in self.__cursos_matriculados:
            print(i)

    def aplicar_novo_curso(self, novo_curso):
        self.__inadimplente = self.check_indaimplencia()
        if self.__inadimplente:
            return False
        self.__cursos_matriculados.append(novo_curso)
        return True

    def check_indaimplencia(self):
        # simulando uma checagem externa no sistema de pagamentos da escola.
        return randint(1, 100) == 11  # 1% de chance de um aluno ficar inandimplente


class Turma:
    def __init__(self, nome_curso, semetres, cod, professor):
        self.nome_curso = nome_curso
        self.semestres = semetres
        self.cod = cod
        self.professor = professor
        self.__lista_alunos = []

    def registrar_aluno(self, aluno: Aluno):
        if not aluno.status_matricula_bool:
            return
        if aluno.aplicar_novo_curso(self.nome_curso):
            self.__lista_alunos.append(aluno)


if __name__ == '__main__':
    turma_si = Turma('Sistemas de informação', 5, 't-SI-0001', 'JOSE CARLOS')
