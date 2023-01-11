"""create meals

Revision ID: 30b128602389
Revises: 29389d77cc14
Create Date: 2023-01-10 21:00:41.663163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b128602389'
down_revision = '29389d77cc14'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE meals(
            meal_id SERIAL PRIMARY KEY,
            meal_name VARCHAR(255) NOT NULL,
            recipes VARCHAR(255) NOT NULL,
            ingredients VARCHAR(255) NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE meals;
        """
    )
