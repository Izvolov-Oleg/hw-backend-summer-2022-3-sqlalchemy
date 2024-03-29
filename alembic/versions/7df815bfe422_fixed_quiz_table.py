"""fixed quiz table

Revision ID: 7df815bfe422
Revises: 61ddd5de7539
Create Date: 2022-08-28 20:40:57.861076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7df815bfe422'
down_revision = '61ddd5de7539'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answers', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('questions', sa.Column('theme_id', sa.Integer(), nullable=False))
    op.alter_column('questions', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_foreign_key(None, 'questions', 'themes', ['theme_id'], ['id'])
    op.alter_column('themes', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('themes', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.alter_column('questions', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('questions', 'theme_id')
    op.alter_column('answers', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
