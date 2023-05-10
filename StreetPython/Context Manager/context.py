
class Aluno:
    # For context manager
    def __enter__(self):
        self.__unlock_notas = True
        return self

    def __exit__(self, cls_exception, context_exception, traceback_exception):
        self.__unlock_notas = False

    def __init__(self, nome, idade):
        self.nome = nome
        self.__n1 = 0
        self.__n2 = 0
        self.__unlock_notas = False
        self.idade = idade

    @property
    def n1(self):
        return self.__n1

    @n1.setter
    def n1(self, vlr, force=False):
        if self.__unlock_notas or force:
            self.__n1 = vlr
        else:
            print("Modificação não permitida.")

    @property
    def n2(self):
        return self.__n2

    @n2.setter
    def n2(self, vlr, force=False):
        if self.__unlock_notas or force:
            self.__n2 = vlr
        else:
            print("Modificação não permitida.")


if __name__ == "__main__":
    a = Aluno('Pedro', 30)
    a.n1 = 10
    print("Nota do aluno: ", a.n1)

    with a as aluno:
        print("Nome: ", aluno.nome)
        aluno.n1 = 10
        print("Nota do aluno com contexto: ", aluno.n1)

    a.n2 = 10
    print("Nota 2 do aluno: ", a.n2)

    a.n1 = 20
    print("Nota 1 do aluno: ", a.n1)