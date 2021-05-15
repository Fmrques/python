from sql_alchemy import banco



class SiteModel(banco.Model):

    __tablename__ = 'sites'

    site_id = banco.Column(banco.Integer, primary_key=True)
    url = banco.Column(banco.String(80))
    

    def __init__(self, url):
        self.url = url 


    def json(self):
        return {
            'site_id': self.site_id,
            'url': self.url,
            'hoteis' :[]
            
        }


    @classmethod
    def find_hotel(cls, hotel_id): #o parâmetro cls indica que é uma função da classe
        #cls  = mesma coisa que estiver escrevendo HotelModel
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()   #SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if hotel:
            return hotel
        return None

    
    def save_hotel(self):
        banco.session.add(self) #session meio que vai acionar os dados
        banco.session.commit()
    
    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

