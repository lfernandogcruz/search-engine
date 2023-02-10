def exists_word(word, instance):
    result = list()
    lowered_word = word.lower()

    for index in range(instance.__len__()):
        file_name = instance.search(index)["nome_do_arquivo"]

        res = {
            "palavra": lowered_word,
            "arquivo": file_name,
            "ocorrencias": [],
        }

        rows = instance.search(index)["linhas_do_arquivo"]

        for row in rows:
            if (row.lower()).__contains__(lowered_word):
                res["ocorrencias"].append({"linha": (rows.index(row) + 1)})

        if res["ocorrencias"]:
            result.append(res)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
