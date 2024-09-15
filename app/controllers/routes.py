from app import app, db ,request, jsonify
from app.models.aluguel import  Aluguel
from app.models.filme import Filme
from app.models.usuario import Usuario
from datetime import datetime



@app.route('/')
@app.route('/api')
def index():
    return "Hello, World!"


@app.route('/api/filmes', methods = ['GET'])
def listar_filmes():
    #Obter o parametro na url de genero
    genero = request.args.get('genero')
    
    if genero: 
        filmes = Filme.query.filter(Filme.genero.like(genero)).all()
    
    else: 
       filmes = Filme.query.all()
       
    if not filmes:
        return jsonify({"Mensagem": "Nenhum filme encontrado"}), 404
    
    
    
    filmes_list = [
        {
          'id' : filme.id,
          'nome' : filme.nome,
          'genero' : filme.genero,
          'ano' : filme.ano,
          'sinopse' : filme.sinopse,
          'diretor' : filme.diretor
        }
     for filme in filmes] 
    return jsonify(filmes_list)



@app.route('/api/filmes/<int:id_filme>', methods = ['GET'])
def get_filme(id_filme):
    #Obter o parametro na url de genero
   
    filme = Filme.query.get(id_filme)
    
    if not filme:
      return jsonify({"Mensagem": "Nenhum filme encontrado"}), 404      
    
    filme_json =[
        {
          'id' : filme.id,
          'nome' : filme.nome,
          'genero' : filme.genero,
          'ano' : filme.ano,
          'sinopse' : filme.sinopse,
          'diretor' : filme.diretor
        }
        ]
     
    return jsonify(filme_json)
    
@app.route('/api/filmes/alugar', methods = ['POST'])
def alugar_filme():
          
    user_id = request.form['user_id']
    filme_id = request.form['filme_id']
    
    if user_id == '' or filme_id == '':
        return jsonify({'Message': 'Faltando parâmetros user_id ou filme_id'}), 400
   
    usuario = Usuario.query.get(user_id)
    filme = Filme.query.get(filme_id)
    
    
    
    
    if not usuario:
        return jsonify({"Message": "Usuario não existe "}), 400
    
    if not filme:
        return jsonify({"Message": "Filme não existe "}), 400
    
    
    novo_aluguel = Aluguel(usuario_id = user_id, filme_id = filme_id, data_aluguel = datetime.now())
    
    db.session.add(novo_aluguel)
    db.session.commit()
    
    return jsonify({'Message': 'Filme alugado com sucesso!'}),201
   
        
@app.route('/api/filmes/<int:id_filme>/usuario/<int:id_usuario>', methods= ['PUT'])
def adicionar_nota(id_filme,id_usuario):
    
    nota = request.json['nota']
       
    if nota is None:
      return jsonify({'Message': 'Faltando parâmetros bota'}), 400
     
    filme_id = Filme.query.get(id_filme)
    usuario_id = Usuario.query.get(id_usuario)
    
    if not usuario_id:
        return jsonify({"Message": "Usuario não existe "}), 400
    
    if not filme_id:
        return jsonify({"Message": "Filme não existe "}), 400
               
   
    aluguel = Aluguel.query.filter_by(filme_id = id_filme,usuario_id =id_usuario).first()
    
    if not aluguel:
        return jsonify({"Message": "Esse usuário não alugou este filme"}), 400
      
    aluguel.nota = nota
    
    db.session.commit()
    
    return jsonify({'Message': 'Nota atualizada com sucesso'}), 200 
    
          
@app.route('/api/filmes/<int:id_usuario>/alugueis', methods = ['GET'])
def ver_alugados(id_usuario):
   
    
    usuario = Usuario.query.get(id_usuario)
    
    if not usuario:
        return jsonify({'message': 'Usuario nao encontrado'}),404
    
    alugueis = Aluguel.query.filter_by(usuario_id = id_usuario ).all()
    
    
    
    filmes_do_usuario = [{
        'data_aluguel' : aluguel.data_aluguel,
        'nota' : aluguel.nota,
        'nome_do_filme' : aluguel.filme.nome
                
    }for aluguel in alugueis]
    
    
    
    return jsonify(filmes_do_usuario)
    
    
    
    
    
    
    
     
 
        

        



    