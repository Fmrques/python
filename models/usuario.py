from sql_alchemy import banco



class UserModel(banco.Model):

    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
      

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'senha': self.senha
             }


    @classmethod
    def find_user(cls, user_id): #o parâmetro cls indica que é uma função da classe
        #cls  = mesma coisa que estiver escrevendo HotelModel
        user = cls.query.filter_by(user_id=user_id).first()   #SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login): 
        login = cls.query.filter_by(login=login).first()   #SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if login:
            return login
        return None

    
    def save_user(self):
        banco.session.add(self) #session meio que vai acionar os dados
        banco.session.commit()
    
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()


