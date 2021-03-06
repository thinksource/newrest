"""empty message

Revision ID: fec776194617
Revises: 9cc48970528d
Create Date: 2018-10-09 08:08:52.394925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fec776194617'
down_revision = '9cc48970528d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Order',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('customer', sa.String(length=80), nullable=False),
    sa.Column('totalpayment', sa.DECIMAL(precision=14, scale=2), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Order_item',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('product_id', postgresql.UUID(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('item_price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('order_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['Order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['Product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Order_item')
    op.drop_table('Order')
    # ### end Alembic commands ###
