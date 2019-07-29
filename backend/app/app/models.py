from sqlalchemy import MetaData

from app import db

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

db.Model.metadata = MetaData(naming_convention=convention)


class Repositories(db.Model):
    __tablename__ = 'repositories'

    repository_id = db.Column(db.String(32), primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    parent = db.Column(db.ForeignKey(u'repositories.repository_id'), index=True, nullable=True)
    fields = db.relationship(
        u'RepositoryFields',
        backref='repositories',
        cascade='all, delete-orphan'
    )
    items = db.relationship(
        u'Items',
        backref='repositories',
        cascade='all, delete-orphan'
    )

    def to_json(self):
        return {
            'repository_id': self.repository_id,
            'name': self.name,
            'parent': self.parent
        }


    @staticmethod
    def from_json(json_record):
        return Repositories(
            repository_id=json_record.get('repository_id'),
            name=json_record.get('name'),
            parent=json_record.get('parent')
        )


class RepositoryFieldTypes(db.Model):
    __tablename__ = 'repository_field_types'

    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    fields = db.relationship(
        u'RepositoryFields',
        backref='repository_field_types',
        cascade='all, delete-orphan'
    )

    def to_json(self):
        return {
            'type_id': self.type_id,
            'name': self.name
        }

    @staticmethod
    def from_json(json_record):
        return RepositoryFieldTypes(
            type_id=json_record.get('type_id'),
            name=json_record.get('name')
        )


class RepositoryFields(db.Model):
    __tablename__ = 'repository_fields'

    field_id = db.Column(db.String(32), primary_key=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    required = db.Column(db.Boolean, default=False)
    repository_id = db.Column(db.ForeignKey(u'repositories.repository_id'))
    field_type_id = db.Column(db.ForeignKey(u'repository_field_types.type_id'))
    numerical_props = db.relationship(
        u'NumericalFieldProperties',
        backref='repository_fields',
        cascade='all, delete-orphan'
    )
    numerical_data = db.relationship(
        u'NumericalData',
        backref='repository_fields',
        cascade='all, delete-orphan'
    )
    plain_text_props = db.relationship(
        u'PlainTextFieldProperties',
        backref='repository_fields',
        cascade='all, delete-orphan'
    )
    plain_text_data = db.relationship(
        u'PlainTextData',
        backref='repository_fields',
        cascade='all, delete-orphan'
    )

    def to_json(self):
        return {
            'field_id': self.field_id,
            'name': self.name,
            'required': self.required,
            'repository_id': self.repository_id,
            'field_type_id': self.field_type_id
        }

    @staticmethod
    def from_json(json_record):
        return RepositoryFields(
            field_id=json_record.get('field_id'),
            name=json_record.get('name'),
            required=json_record.get('required'),
            repository_id=json_record.get('repository_id'),
            field_type_id=json_record.get('field_type_id')
        )


class NumericalFieldProperties(db.Model):
    __tablename__ = 'numerical_field_props'

    property_id = db.Column(db.String(32), primary_key=True, nullable=False)
    field_id = db.Column(db.ForeignKey(u'repository_fields.field_id'), index=True, nullable=False)
    min_value = db.Column(db.Integer, default=0, nullable=False)
    max_value = db.Column(db.Integer, default=0, nullable=False)

    def to_json(self):
        return {
            'property_id': self.property_id,
            'field_id': self.field_id,
            'min_value': self.min_value,
            'max_value': self.max_value
        }

    @staticmethod
    def from_json(json_record):
        return NumericalFieldProperties(
            property_id=json_record.get('property_id'),
            field_id=json_record.get('field_id'),
            min_value=json_record.get('min_value'),
            max_value=json_record.get('max_value')
        )


class PlainTextFieldProperties(db.Model):
    __tablename__ = 'plain_text_field_props'

    property_id = db.Column(db.String(32), primary_key=True, nullable=False)
    field_id = db.Column(db.ForeignKey(u'repository_fields.field_id'), index=True, nullable=False)
    min_size = db.Column(db.Integer, default=0, nullable=False)
    max_size = db.Column(db.Integer, default=0, nullable=False)

    def to_json(self):
        return {
            'property_id': self.property_id,
            'field_id': self.field_id,
            'min_value': self.min_size,
            'max_value': self.max_size
        }

    @staticmethod
    def from_json(json_record):
        return PlainTextFieldProperties(
            property_id=json_record.get('property_id'),
            field_id=json_record.get('field_id'),
            min_value=json_record.get('min_size'),
            max_value=json_record.get('max_size')
        )


class Items(db.Model):
    __tablename__ = 'items'

    item_id = db.Column(db.String(32), primary_key=True, nullable=False)
    repository_id = db.Column(db.ForeignKey(u'repositories.repository_id'), index=True, nullable=False)
    numerical_data = db.relationship(
        u'NumericalData',
        backref='items',
        cascade='all, delete-orphan'
    )
    plain_text_data = db.relationship(
        u'PlainTextData',
        backref='items',
        cascade='all, delete-orphan'
    )

    def to_json(self):
        return {
            'item_id': self.item_id,
            'repository_id': self.repository_id
        }

    @staticmethod
    def from_json(json_record):
        return Items(
            item_id=json_record.get('item_id'),
            repository_id=json_record.get('repository_id')
        )


class NumericalData(db.Model):
    __tablename__ = 'numerical_data'

    data_id = db.Column(db.String(32), primary_key=True, nullable=False)
    data = db.Column(db.Integer, nullable=True)
    item_id = db.Column(db.ForeignKey(u'items.item_id'), index=True, nullable=False)
    field_id = db.Column(db.ForeignKey(u'repository_fields.field_id'), index=True, nullable=False)
    repository_id = db.Column(db.ForeignKey(u'repositories.repository_id'), index=True, nullable=False)

    def to_json(self):
        return {
            'data_id': self.data_id,
            'data': self.data,
            'item_id': self.item_id,
            'field_id': self.field_id,
            'repository_id': self.repository_id
        }

    @staticmethod
    def from_json(json_record):
        return NumericalData(
            data_id=json_record.get('data_id'),
            data=json_record.get('data'),
            item_id=json_record.get('item_id'),
            field_id=json_record.get('field_id'),
            repository_id=json_record.get('repository_id')
        )


class PlainTextData(db.Model):
    __tablename__ = 'plain_text_data'

    data_id = db.Column(db.String(32), primary_key=True, nullable=False)
    data = db.Column(db.Text(), nullable=True)
    item_id = db.Column(db.ForeignKey(u'items.item_id'), index=True, nullable=False)
    field_id = db.Column(db.ForeignKey(u'repository_fields.field_id'), index=True, nullable=False)
    repository_id = db.Column(db.ForeignKey(u'repositories.repository_id'), index=True, nullable=False)

    def to_json(self):
        return {
            'data_id': self.data_id,
            'data': self.data,
            'item_id': self.item_id,
            'field_id': self.field_id,
            'repository_id': self.repository_id
        }

    @staticmethod
    def from_json(json_record):
        return PlainTextData(
            data_id=json_record.get('data_id'),
            data=json_record.get('data'),
            item_id=json_record.get('item_id'),
            field_id=json_record.get('field_id'),
            repository_id=json_record.get('repository_id')
        )
