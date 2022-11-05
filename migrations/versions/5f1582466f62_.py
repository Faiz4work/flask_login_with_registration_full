"""empty message

Revision ID: 5f1582466f62
Revises: a3d711890d76
Create Date: 2022-10-11 20:15:39.238929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f1582466f62'
down_revision = 'a3d711890d76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maintenances_tyres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=False),
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
    sa.Column('maintenance_expiry_year_month_km_date', sa.DateTime(), nullable=True),
    sa.Column('type_of_service', sa.String(length=50), nullable=True),
    sa.Column('service_intervals', sa.String(length=50), nullable=True),
    sa.Column('tyre_value', sa.String(length=50), nullable=True),
    sa.Column('accident_value', sa.String(length=50), nullable=True),
    sa.Column('accident_incident', sa.String(length=50), nullable=True),
    sa.Column('other_value', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('toll_value', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maintenances_tyres')
    # ### end Alembic commands ###