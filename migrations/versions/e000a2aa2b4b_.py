"""empty message

Revision ID: e000a2aa2b4b
Revises: 0804bd9f1d87
Create Date: 2021-10-27 15:10:11.700746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e000a2aa2b4b'
down_revision = '0804bd9f1d87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('public_id', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'users', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'public_id')
    # ### end Alembic commands ###
