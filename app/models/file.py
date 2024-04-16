from run import db


class File(db.Model):
    __tablename__ = 'files'
    p_id = db.Column(db.Integer, primary_key = True)
    file_url = db.Column(db.String(500), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()

    def db_to_commit(self):
        db.session.commit()

    def update_data(self, old_data,new_data):
        old_data.file_url =  new_data['file_url']

        return old_data
    
    @staticmethod
    def to_json(data):
        return {
            'p_id': data.p_id,
            'file_url': data.file_url,
        }

    @classmethod
    def return_all(cls):
        return list(map(lambda x: cls.to_json(x), File.query.all()))
