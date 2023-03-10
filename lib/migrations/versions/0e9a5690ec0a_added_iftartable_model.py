"""Added IftarTable model

Revision ID: 0e9a5690ec0a
Revises: 11ab5ee210c0
Create Date: 2023-03-08 12:55:27.552395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e9a5690ec0a'
down_revision = '11ab5ee210c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('iftar_tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('iftar_time', sa.Time(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iftar_tables')
    # ### end Alembic commands ###
