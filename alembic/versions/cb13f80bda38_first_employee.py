"""First Employee

Revision ID: cb13f80bda38
Revises: 
Create Date: 2025-12-17 18:35:16.924823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb13f80bda38'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("employees" ,   sa.Column("id" ,sa.Integer() , primary_key=True , nullable=False),
                                    sa.Column("firstname" , sa.String(), nullable=False),
                                    sa.Column("age", sa.Integer() , nullable=False),
                                    sa.Column("created_at" , sa.TIMESTAMP(timezone=True) , server_default=sa.text("now()") , nullable=False , autoincrement=False),
                                    sa.PrimaryKeyConstraint("id"),

                                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("employees"   ,
                                    sa.Column("id" ,sa.Integer() , primary_key=True , nullable=False),
                                    sa.Column("firstname" , sa.String(), nullable=False),
                                    sa.Column("age", sa.Integer() , nullable=False),
                                    sa.Column("created_at" , sa.TIMESTAMP(timezone=True) , server_default=sa.text("now()") , nullable=False , autoincrement=False),
                                    sa.PrimaryKeyConstraint("id"),
                                    )
