from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")


#LISTA DE USUÁRIOS APENAS PARA TESTE
class Users(Resource):
    def get(self):
        dados = atributos.parse_args()
        if dados['login'] == 'fafa' and dados['senha'] == '521523':
            return {'Usuários': [user.json() for user in UserModel.query.all()]}
        return {'message': 'Permission not granted'}



# Funções do CRUD
class User(Resource):
    #/usuarios/{user_id}

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message':'User not found.'}, 404 #not found
 
  
    @jwt_required()   
    def delete(self, hotel_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message':'Error deleting user.'}, 500 #Internal Server Error
            return {'message': 'User Deleted'}
        return {'message': 'User not found.'}, 404
     
   
class UserRegister(Resource):
    #/cadastro
    def post(self):
        
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'message':'Login already exists'}
        
        user = UserModel(**dados)
        user.save_user()
        return {'Message':'User created successfully!'}, 201 #Created

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()


        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200
        return {'message': 'Username or password is incorrect.'}, 401 #Unauthorized
    
class UserLogout(Resource):
        
        @jwt_required()
        def post(self):
            jwt_id = get_jwt()['jti'] #JWT Token Identifier
            BLACKLIST.add(jwt_id)
            return {'Message': 'Logged out successfully!'}, 200