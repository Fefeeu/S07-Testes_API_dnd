db = db.getSiblingDB('logs_de_teste');

const colecoes_ja_existentes = db.getCollectionNames();

if(!colecoes_ja_existentes.includes('historico')){
    db.createCollection('historico');
} else {
    print("Collection 'historico' já existe, operação de criação pulada");
}

db.historico.insertOne({
    mensagem: "Banco Inicializado com Sucesso",
    data: new Date()
});