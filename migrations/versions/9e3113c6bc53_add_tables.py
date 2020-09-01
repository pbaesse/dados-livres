"""add tables

Revision ID: 9e3113c6bc53
Revises: 3247c8cb1cdd
Create Date: 2020-08-03 16:36:01.694821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e3113c6bc53'
down_revision = '3247c8cb1cdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('similar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name=op.f('fk_similar_post_id_post')),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], name=op.f('fk_similar_software_id_software')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_similar'))
    )
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_similar_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_similar_timestamp'), ['timestamp'], unique=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_similar')
        batch_op.drop_column('similar')

    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.drop_index('ix_software_similar')
        batch_op.drop_column('similar')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.add_column(sa.Column('similar', sa.VARCHAR(length=200), nullable=True))
        batch_op.create_index('ix_software_similar', ['similar'], unique=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('similar', sa.VARCHAR(length=200), nullable=True))
        batch_op.create_index('ix_post_similar', ['similar'], unique=False)

    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_similar_timestamp'))
        batch_op.drop_index(batch_op.f('ix_similar_name'))

    op.drop_table('similar')
    # ### end Alembic commands ###
