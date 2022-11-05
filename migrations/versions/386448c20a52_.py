"""empty message

Revision ID: 386448c20a52
Revises: cb76f9185f3a
Create Date: 2022-10-26 01:07:52.834501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386448c20a52'
down_revision = 'cb76f9185f3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fleet_inspection_card_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('driver_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_fleet_inspection_card_form_driver_id_user'), 'user', ['driver_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fleet_inspection_card_form', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_fleet_inspection_card_form_driver_id_user'), type_='foreignkey')
        batch_op.drop_column('driver_id')

    # ### end Alembic commands ###