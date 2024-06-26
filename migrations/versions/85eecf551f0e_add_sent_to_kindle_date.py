"""Add sent_to_kindle date

Revision ID: 85eecf551f0e
Revises: 12f4cb02e6d7
Create Date: 2024-06-02 14:04:43.877122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85eecf551f0e'
down_revision: Union[str, None] = '12f4cb02e6d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sent_to_kindle', sa.TIMESTAMP(), nullable=True))
        batch_op.create_index(batch_op.f('ix_entries_sent_to_kindle'), ['sent_to_kindle'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_entries_sent_to_kindle'))
        batch_op.drop_column('sent_to_kindle')

    # ### end Alembic commands ###
