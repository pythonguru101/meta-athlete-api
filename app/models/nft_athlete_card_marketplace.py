from run import db
from datetime import datetime
from sqlalchemy.orm import backref


class NFTMarketplaceModel(db.Model):
    __tablename__ = 'nft_athlete_card_marketplace'
    p_id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.String, db.ForeignKey('user.wallet_id'), nullable = False)
    wallet = db.relationship("UserModel", backref=backref("nft_athlete_card_marketplace", lazy="dynamic"))
    tier = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(100) , nullable=False)
    athlete_card_id = db.Column(db.Integer, db.ForeignKey('nft_athlete_card.p_id'), nullable = False)
    athlete = db.relationship("MetaAthleteNFT", backref=backref("nft_athlete_card_marketplace", lazy="dynamic"))
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def to_json(data):
        print(data)
        return {
            'p_id': data.p_id,
            'wallet_id': data.wallet_id,
            'tier': data.tier,
            'price':data.price,
            'athlete_card_id':data.athlete_card_id,            
        }

    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id=p_id).first()

    @classmethod
    def return_all(cls):
        return list(map(lambda x: cls.to_json(x), NFTMarketplaceModel.query.all())) 
