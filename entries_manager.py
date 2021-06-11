from entry import Entry
from database import Database
from marsh import EntrieSchema


class EntriesManager:

    @staticmethod
    def lounch_db():
        session = Database.database_launch()
        return session

    @staticmethod
    def request_data(request_form):
        return {"title": request_form['title'],
                "description": request_form['description'],
                "content": request_form['content']}

    @staticmethod
    def create_entry(**entry_data):
        new_entry = Entry(**entry_data)
        EntriesManager.save_entry(new_entry)
        return new_entry

    @staticmethod
    def save_entry(entry):
        session = Create.session_singletone
        merged_entry = session.merge(entry)
        session.commit()
        return merged_entry

    @staticmethod
    def remove_file(entry):
        session = Create.session_singletone
        session.delete(entry)
        session.commit()
    
    @staticmethod
    def find_by(id=None, title=None):
        session = Create.session_singletone
        if title is None:
            query = session.query(Entry).filter(Entry.id == id)
        else:
            query = session.query(Entry).filter(Entry.title == title)
        return query.first()

    @staticmethod
    def json_find_by(id=None, title=None):
        query = EntriesManager.find_by(id, title)
        schema = EntrieSchema()
        return schema.dump(query)

    @staticmethod
    def find_all():
        session = Create.session_singletone
        entries = session.query(Entry).all()
        schema = EntrieSchema()
        return [schema.dump(entry) for entry in entries]

    @staticmethod
    def change_entry(editing_entry, new_entry_data):
        editing_entry.title = new_entry_data['title']
        editing_entry.description = new_entry_data['description']
        editing_entry.content = new_entry_data['content']

        EntriesManager.save_entry(editing_entry)



class Create(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Create, cls).__new__(cls)
        return cls.instance
    session_singletone = EntriesManager.lounch_db()














