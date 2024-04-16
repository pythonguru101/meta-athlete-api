from run import db
from datetime import datetime, timedelta
from sqlalchemy import Enum
from sqlalchemy.orm import backref
from utils.enums import SportType, SchoolGrade, UserType


class MetaAthleteNFT(db.Model):
    __tablename__ = 'nft_athlete_card'
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nft_uuid = db.Column(db.String(100), nullable=True)
    kind = db.Column(Enum(UserType), nullable=False)
    sport = db.Column(Enum(SportType), nullable=False)
    birthdate = db.Column(db.DateTime(), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    height = db.Column(db.Float(), nullable=False)
    schoolgrade = db.Column(Enum(SchoolGrade), nullable=False)
    photo = db.Column(db.Integer, db.ForeignKey('files.p_id'), nullable = False)
    photoObj = db.relationship("File", backref=backref("nft_athlete_card", lazy="dynamic"))
    cardMinted = db.Column(db.Boolean, nullable=False, default=False)
    quantity_gold = db.Column(db.Integer, default=0)
    quantity_platinum = db.Column(db.Integer, default=0)
    quantity_diamond = db.Column(db.Integer, default=0)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def is_over_18(self):
        eighteen_years_ago = datetime.now() - timedelta(days=18*365)
        return self.birthdate <= eighteen_years_ago
    
    @staticmethod
    def to_json(data):
        date = data.birthdate
        formatted_date = ''
        if date:
            formatted_date = date.strftime("%d/%m/%Y/")
        
        return {
            'p_id': data.p_id,
            'name': data.name,
            'nft_uuid': data.nft_uuid,
            'kind': UserType.fetch_items(data.kind.value),
            'sport': SportType.fetch_items(data.sport.value),
            'birthdate': formatted_date,
            'weight': data.weight,
            'height': data.height,
            'schoolgrade': SchoolGrade.fetch_items(data.schoolgrade.value),
            'photo': data.photo,
            'cardMinted': data.cardMinted,
            'quantity_gold': data.quantity_gold,
            'quantity_platinum': data.quantity_platinum,
            'quantity_diamond': data.quantity_diamond,
        }
        
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id=p_id).first()
    
    @classmethod
    def return_all(cls):
        return list(map(lambda x: cls.to_json(x), MetaAthleteNFT.query.all())) 
