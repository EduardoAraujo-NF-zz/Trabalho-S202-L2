import pymongo
import sys


class Database:
    def __init__(self, collection_name):
        self.clusterConnection = pymongo.MongoClient(
            "mongodb+srv://root:root@l2cluster.1oxvw.mongodb.net/test?authSource=admin&replicaSet=atlas-14aoi5-shard"
            "-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true "
        )
        self.db = self.clusterConnection['TrabFlix']
        self.collection = self.db[collection_name]

    def executeQuery(self, filters: dict, project: dict):
        response = self.collection.find(filters, project)
        documentos = []
        for docs in response:
            documentos.append(docs)
        return documentos

    def insertOne(self, doc: dict):
        try:
            result = self.collection.insert_one(doc)
            print('Inserido com sucesso :D')
            return result.acknowledged
        except:
            print(f"Erro: {sys.exc_info()}")

    def executeDbCommand(self, command):
        self.db.command(command)

    def createIndex(self, indices: list):
        result = self.collection.create_index(indices)
        print(f'Resultado da criação de indice:\n {result}')

    def dropIndex(self, indices: list, need_print: bool):
        for indice in indices:
            result = self.collection.drop_index(indice[0])
            if need_print:
                print(f'Resultado da exclusão de indice: {result}')

    def deleteOne(self, doc: dict):
        try:
            result = self.collection.delete_one(doc)
            print('Removido com sucesso :D')
            return result.acknowledged
        except:
            print(f"Erro: {sys.exc_info()}")

    def searchAll(self):
        response = self.collection.find({}, {"_id": 0})
        movie = []
        for movieVar in response:
            movie.append(movieVar)

        for movieRef in movie:
            print("Nome: ", movieRef["title"])
            print("Gêneros: ", ", ".join(movieRef["info"]["genres"]))
            print("Atores: ", ", ".join(movieRef["info"]["actors"]))
            print("Diretores: ", ", ".join(movieRef["info"]["directors"]))
            print("Duração: ", movieRef["info"]["duration"])
            print("Data de Lançamento: ", movieRef["info"]["release_date"])
            print("Imagem: ", movieRef["info"]["image_url"])
            print("Trailer: ", movieRef["info"]["trailer_url"])
            print("\n")

    def update(self, movie, categoria, newvalue):
        if categoria != "title":
            self.collection.update_one({"title": movie}, {"$set": {'info.' + categoria: newvalue}})
        else:
            self.collection.update_one({"title": movie}, {"$set": {categoria: newvalue}})
