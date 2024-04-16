from run import db
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
from utils.enums import CardType

class AvailableCardsModel(db.Model):
    __tablename__ = 'avail_tier_cards'
    p_id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer, nullable=False)
    tier =  db.Column(Enum(CardType), nullable=False)
    id_nft = db.Column(db.Integer, db.ForeignKey('nft_athlete_card.p_id'), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()

    def db_to_commit(self):
        db.session.commit()

    def update_data(self, old_data, new_data):
        old_data.card_number = new_data['card_number']
        old_data.tier = new_data['tier']
        old_data.id_nft = new_data['id_nft']
        return old_data

    @staticmethod
    def to_json(data):
        return {
            'p_id': data.p_id,
            'card_number': data.card_number, 
            'tier': CardType.fetch_items(data.tier.value),
            'id_nft': data.id_nft,    
        }
        
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id=p_id).first()
    
    @classmethod
    def return_all(cls):
        return list(map(lambda x: cls.to_json(x), AvailableCardsModel.query.all()))




