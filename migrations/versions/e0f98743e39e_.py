"""empty message

Revision ID: e0f98743e39e
Revises: 
Create Date: 2020-02-21 17:00:56.327439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0f98743e39e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('meeting_date', sa.String(length=50), nullable=False),
    sa.Column('meeting_hour', sa.String(length=50), nullable=False),
    sa.Column('project_name', sa.String(length=50), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('place', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('target', sa.String(length=50), nullable=True),
    sa.Column('done', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('rol', sa.String(length=50), nullable=True),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('priority', sa.String(length=50), nullable=True),
    sa.Column('notes', sa.String(length=50), nullable=True),
    sa.Column('care', sa.String(length=50), nullable=True),
    sa.Column('tracking', sa.String(length=50), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topics')
    op.drop_table('guests')
    op.drop_table('meetings')
    op.drop_table('users')
    # ### end Alembic commands ###