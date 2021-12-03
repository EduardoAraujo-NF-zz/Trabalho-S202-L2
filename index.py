import documentConfig
from database import Database
from collections import OrderedDict
import os
import bson

db = Database('Stream')
command = OrderedDict([('collMod', 'Stream'),
                      ('validator', documentConfig.validation),
                      ('validationLevel', 'strict')])
db.executeDbCommand(command)


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1 -> Inserir novo filme')
    print('2 -> Mostrar todos os filmes')
    print('3 -> Pesquisar por ator e genero')
    print('4 -> Editar item')
    print('5 -> Deletar item')
    print('6 -> Exit')


def alterar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1 -> Nome')
    print('2 -> Gêneros')
    print('3 -> Diretores')
    print('4 -> Atores')
    print('5 -> Duração')
    print('6 -> Data de lançamento')
    print('7 -> Poster url')
    print('8 -> Trailer url')
    print('9 -> Cancelar')

    opcao = input('\nEntre com a opção desejada: ')
    if opcao == "1":
        return "title"
    elif opcao == "2":
        return "genres"
    elif opcao == "3":
        return "directors"
    elif opcao == "4":
        return "actors"
    elif opcao == "5":
        return "duration"
    elif opcao == "6":
        return "release_date"
    elif opcao == "7":
        return "image_url"
    elif opcao == "8":
        return "trailer_url"
    else:
        return 0


def main():
    opcao = 0
    while opcao != '6':
        menu()
        opcao = input('\nEntre com a opção desejada: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcao == '1':
            print('Inserir novo filme')
            print('Separe varios valores utilizando barra')
            nome = input('Nome: ')
            genero = input('Gêneros: ').split('/')
            diretores = input('Diretores: ').split('/')
            atores = input('Atores: ').split('/')
            duracao = input('Duração do filme: ')
            lancamento = input('Data de lançamento: ')
            image_url = input('Poster url: ')
            trailer_url = input('Trailer url: ')

            info = {
                'directors': diretores,
                'release_date': lancamento,
                'genres': genero,
                'image_url': image_url,
                'trailer_url': trailer_url,
                'actors': atores,
                'duration': duracao
            }

            bson_doc = bson.BSON.encode({'type': 'movie', 'title': nome, 'info': info})
            decoded_doc = bson.BSON.decode(bson_doc)
            db.insertOne(decoded_doc)
            input('Press Enter to continue...')

        if opcao == '2':
            db.searchAll()
            input('Press Enter to continue...')

        if opcao == '3':
            print('Entre com o ator e o genero')
            try:
                ator = input('Ator: ')
                genero = input('Gênero: ')
                db.createIndex([{"info.genres": genero, "info.actors": ator}])
            except:
                print("Falha")
            input('Press Enter to continue...')

        if opcao == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Entre com o nome do filme que deseja alterar')
            nome = input('Nome: ')
            categoria = alterar()
            if categoria != 0:
                new_value = input('Novo valor: ')
                db.update(nome, categoria, new_value)
            input('Press Enter to continue...')

        if opcao == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Entre com o nome do filme que deseja remover')
            nome = input('Nome: ')
            db.deleteOne({"title": nome})
            input('Press Enter to continue...')

    print('Bye...')


if __name__ == "__main__":
    main()
