import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    text = txt_importer(path_file)
    if not text:
        return sys.stderr.write("Arquivo não encontrado\n")

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }

    for item in range(instance.__len__()):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return sys.stderr.write(f"Arquivo {path_file} já está na fila\n")

    instance.enqueue(file_info)
    print(file_info)


def remove(instance):
    if not instance or instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    removed_file = instance.dequeue()
    target_path = removed_file["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {target_path} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
