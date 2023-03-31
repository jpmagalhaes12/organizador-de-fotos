import os
import time
import shutil

EXTENSOES = ['.png', '.PNG', '.jpeg', '.JPEG', '.jpg', '.JPG']


class Organizador:
    atual = os.getcwd()
    files = []

    def list_files(self):
        """
        Adiciona na lista 'files' os arquivos do diretorio atual que possuem a extensao
        especificada.
        """
        for s in os.listdir('.'):
            for i in EXTENSOES:
                if s.endswith(i):
                    self.files.append(s)

    def see_time(self, arquivo):
        """
        Verifica a ultima data de criacao e modificacao do arquivo, para nomear os
        diretorios
        :param arquivo: str
        :return: o nome da pasta(data) que o arquivo ficara e também o nome do diretorio
        anterior(ano).
        """
        destino = self.atual + '\\'
        ti_m = os.path.getmtime(destino + arquivo)
        ti_c = os.path.getctime(destino + arquivo)
        last_modified = time.ctime(ti_m)
        last_creation = time.ctime(ti_c)
        if len(last_creation) != 0:
            data = str(last_creation).split(' ')
        elif len(last_creation) == 0:
            data = str(last_modified).split(' ')
        for y, k in enumerate(data):
            if '' == k:
                del(data[y])
        name_file = data[4] + '-' + data[1] + '-' + data[2]
        return name_file, data[4]

    def main(self):
        """
        Codigo principal, nomeia e realoca todos os arquivos selecionados.
        """
        name = self.see_time
        self.list_files()
        for arquivo in self.files:
            destino = self.atual + '\\'
            if not os.path.exists(destino + name(arquivo)[1]):
                os.mkdir(destino + name(arquivo)[1])
                if not os.path.exists(destino + name(arquivo)[1] + '\\' + name(arquivo)[0]):
                    os.mkdir(destino + name(arquivo)[1] + '\\' + name(arquivo)[0])
                shutil.move(destino + arquivo, destino + name(arquivo)[1] + '\\' + name(arquivo)[0])

            elif os.path.exists(destino + name(arquivo)[1]):
                if not os.path.exists(destino + name(arquivo)[1] + '\\' + name(arquivo)[0]):
                    os.mkdir(destino + name(arquivo)[1] + '\\' + name(arquivo)[0])
                shutil.move(destino + arquivo, destino + name(arquivo)[1] + '\\' + name(arquivo)[0])


org = Organizador()
org.main()

