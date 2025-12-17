"""Adding Roles&Position

Revision ID: 297da5472f23
Revises: cb13f80bda38
Create Date: 2025-12-18 00:40:05.922373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '297da5472f23'
down_revision: Union[str, Sequence[str], None] = 'cb13f80bda38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("roles" ,   sa.Column("id" , sa.Integer() , nullable=False , index= True),
                                sa.Column("position" , sa.String() , nullable=False),
                                sa.Column("started_at" , sa.TIMESTAMP(timezone=True) , server_default=sa.text("now()")),
                                sa.Column("earning" , sa.Integer() , nullable=False),
                                sa.Column("owner_id" , sa.Integer() , nullable=False),
                                sa.ForeignKeyConstraint(['owner_id'] , ['employees.id'] , ondelete="CASCADE"),
                                sa.PrimaryKeyConstraint('id')
                                    
                                )



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('roles')
