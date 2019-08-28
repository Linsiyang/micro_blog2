"""user update

Revision ID: 638e6d1e5a9b
Revises: 4d29db865388
Create Date: 2019-08-28 10:10:10.481380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638e6d1e5a9b'
down_revision = '4d29db865388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
