"""adicionado nullable na nota.

Revision ID: 1d0be2546a9d
Revises: 74f645f2664b
Create Date: 2024-09-15 13:54:42.321024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d0be2546a9d'
down_revision = '74f645f2664b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alugueis', schema=None) as batch_op:
        batch_op.alter_column('nota',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alugueis', schema=None) as batch_op:
        batch_op.alter_column('nota',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
