"""empty message

Revision ID: 687691603e38
Revises: 36f07a7ccd3b
Create Date: 2022-10-07 00:12:16.782546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '687691603e38'
down_revision = '36f07a7ccd3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fleet_inspection_card_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_service_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('current_sign_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('last_service')
        batch_op.drop_column('current_sign_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fleet_inspection_card_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_sign_time', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('last_service', sa.DATETIME(), nullable=True))
        batch_op.drop_column('current_sign_date')
        batch_op.drop_column('last_service_date')

    # ### end Alembic commands ###
