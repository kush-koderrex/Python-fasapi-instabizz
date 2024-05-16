"""add content column to posts table

Revision ID: a15b1de9f134
Revises: 8bac1caf8539
Create Date: 2024-05-14 12:20:33.571306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a15b1de9f134'
down_revision: Union[str, None] = '8bac1caf8539'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
