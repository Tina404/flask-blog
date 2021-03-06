"""empty message

Revision ID: 2994b726f569
Revises: 3c61f3302322
Create Date: 2020-02-24 09:45:00.556556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2994b726f569'
down_revision = '3c61f3302322'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
