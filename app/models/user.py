from run import db
from sqlalchemy import Enum


class UserModel(db.Model):
    __tablename__ = 'user'

    p_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    wallet_id = db.Column(db.String(64), nullable=False, unique=True) 
    did = db.Column(db.String(100), nullable=True) 
    vc = db.Column(db.String(100), nullable=True) 
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()

    def db_to_commit(self):
        db.session.commit()

    def update_data(self, old_data, new_data):
        old_data.username = new_data['username']
        old_data.password = new_data['password']
        old_data.wallet_id = new_data['wallet_id']
        old_data.did = new_data['did']
        old_data.vc = new_data['vc']
    
        return old_data

    @staticmethod
    def to_json(data):
        return {
            'p_id': data.p_id,
            'username': data.username,
            'password': data.password,
            'wallet_id': data.wallet_id,  
            'did': data.did,  
            'vc': data.vc,   
        }
        
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id=p_id).first()
    
    @classmethod
    def return_all(cls):
        return list(map(lambda x: cls.to_json(x), UserModel.query.all()))