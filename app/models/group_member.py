from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from app.db.base import Base
from sqlalchemy import UniqueConstraint


class GroupMember(Base):
    __tablename__ = "group_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    joined_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint("user_id", "group_id", name="uq_group_member"),
    )
