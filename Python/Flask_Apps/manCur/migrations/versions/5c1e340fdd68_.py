"""empty message

Revision ID: 5c1e340fdd68
Revises: f011edccc2ef
Create Date: 2018-02-28 13:15:52.273811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c1e340fdd68'
down_revision = 'f011edccc2ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('variant_size', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('variants', 'variant_size')
    # ### end Alembic commands ###