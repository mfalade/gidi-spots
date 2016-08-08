"""empty message

Revision ID: 514f5ef032e9
Revises: e1f9427865fa
Create Date: 2016-08-08 16:33:14.412126

"""

# revision identifiers, used by Alembic.
revision = '514f5ef032e9'
down_revision = 'e1f9427865fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=50), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    ### end Alembic commands ###
