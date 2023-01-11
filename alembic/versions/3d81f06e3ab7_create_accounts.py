"""create accounts

Revision ID: 3d81f06e3ab7
Revises: 
Create Date: 2023-01-10 21:00:27.863567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d81f06e3ab7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE accounts(
            account_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            user_key VARCHAR(255) NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE accounts;
        """
    )
