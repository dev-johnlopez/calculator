from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
address = Table('address', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('property_id', Integer),
    Column('addressLine1', String(length=255), nullable=False),
    Column('addressLine2', String(length=255)),
    Column('addressLine3', String(length=255)),
    Column('city', String(length=255), nullable=False),
    Column('state', String(length=255), nullable=False),
    Column('postalCode', String(length=255), nullable=False),
    Column('longitude', Numeric(precision=18, scale=13)),
    Column('latitude', Numeric(precision=15, scale=13)),
    Column('create_user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].columns['latitude'].create()
    post_meta.tables['address'].columns['longitude'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].columns['latitude'].drop()
    post_meta.tables['address'].columns['longitude'].drop()
