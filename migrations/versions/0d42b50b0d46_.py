"""empty message

Revision ID: 0d42b50b0d46
Revises: fc268fffa5a1
Create Date: 2020-02-06 22:26:59.553258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d42b50b0d46'
down_revision = 'fc268fffa5a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('movie_title', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('movie_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
