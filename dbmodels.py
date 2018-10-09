from uuid import UUID
from config import db
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta
import json
class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """
    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        # Prevent changing ID of object
        kwargs.pop('id', None)
        # db.session.query(self).update(kwargs)
        # if commit:
        #     db.session.commit()
        # return self
        for attr, value in kwargs.items():
            # Flask-RESTful makes everything None by default :/
            if value is not None:
                setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

# serialize output
class OutputMixin(object):
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT

        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                
                value = getattr(self, attr)

                if value is None:
                    res[relation.key] = None

                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__) for i in value]
        return res

    def to_json(self, rel=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return x.isoformat()
            if isinstance(x, UUID):
                return str(x)
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        return json.dumps(self.to_dict(rel), default=extended_encoder)

class MyModel(CRUDMixin, OutputMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""
    __abstract__ = True

    def __init__(self,   **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, UUID):
                setattr(self, key, str(value))
            else:
                setattr(self, key, value)