"""empty message

Revision ID: 314bdbc6aafa
Revises: 
Create Date: 2023-01-10 21:27:59.244868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '314bdbc6aafa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meals', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=500),
               existing_nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('dietary_restrictions',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('dietary_restrictions',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    with op.batch_alter_table('meals', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###
