"""empty message

Revision ID: 802609a71f7d
Revises: bfdbfe488b17
Create Date: 2022-10-05 04:28:22.141716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '802609a71f7d'
down_revision = 'bfdbfe488b17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maintenances_tyres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('driver', sa.String(length=50), nullable=True),
    sa.Column('reg_num', sa.String(length=50), nullable=True),
    sa.Column('yr_mth', sa.String(length=50), nullable=True),
    sa.Column('make', sa.String(length=50), nullable=True),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.Column('fuel_value', sa.String(length=50), nullable=True),
    sa.Column('km_travelled', sa.String(length=50), nullable=True),
    sa.Column('oil_value', sa.String(length=50), nullable=True),
    sa.Column('km', sa.String(length=50), nullable=True),
    sa.Column('repair_and_maint', sa.String(length=50), nullable=True),
    sa.Column('maintenance_plan', sa.String(length=50), nullable=True),
    sa.Column('maintenance_expiry_year_month_km', sa.String(length=50), nullable=True),
    sa.Column('type_of_service', sa.String(length=50), nullable=True),
    sa.Column('service_intervals', sa.String(length=50), nullable=True),
    sa.Column('tyre_value', sa.String(length=50), nullable=True),
    sa.Column('accident_value', sa.String(length=50), nullable=True),
    sa.Column('accident_incident', sa.String(length=50), nullable=True),
    sa.Column('other_value', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('toll_value', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maintenances_tyres')
    # ### end Alembic commands ###
