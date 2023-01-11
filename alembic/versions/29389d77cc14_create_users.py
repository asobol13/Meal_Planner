"""create users

Revision ID: 29389d77cc14
Revises: 3d81f06e3ab7
Create Date: 2023-01-10 21:00:36.182193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29389d77cc14'
down_revision = '3d81f06e3ab7'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            dietary_restrictions BOOLEAN NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE users;
        """
    )
