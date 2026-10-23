from datetime import datetime, date
from sqlalchemy import String, Text, Integer, Float, Boolean, Date, DateTime, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(180), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(300))
    role: Mapped[str] = mapped_column(String(20), default="creator")
    avatar_url: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    otp_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    otp_expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    creator_profile: Mapped["CreatorProfile"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")

class CreatorProfile(Base):
    __tablename__ = "creator_profiles"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    biography: Mapped[str] = mapped_column(Text, default="")
    specialization: Mapped[str] = mapped_column(String(100), default="AI Video")
    experience_level: Mapped[str] = mapped_column(String(40), default="Intermediate")
    availability: Mapped[str] = mapped_column(String(40), default="Available")
    rate_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    rate_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    skills: Mapped[list] = mapped_column(JSON, default=list)
    tools: Mapped[list] = mapped_column(JSON, default=list)
    content_types: Mapped[list] = mapped_column(JSON, default=list)
    formats: Mapped[list] = mapped_column(JSON, default=list)
    aspect_ratios: Mapped[list] = mapped_column(JSON, default=list)
    languages: Mapped[list] = mapped_column(JSON, default=list)
    workflow: Mapped[str] = mapped_column(Text, default="")
    verification_status: Mapped[str] = mapped_column(String(40), default="Self-reported")
    projects: Mapped[list["PortfolioProject"]] = relationship(back_populates="creator", cascade="all, delete-orphan")
    user: Mapped[User] = relationship(back_populates="creator_profile")

class PortfolioProject(Base):
    __tablename__ = "portfolio_projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("creator_profiles.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(180))
    description: Mapped[str] = mapped_column(Text, default="")
    content_type: Mapped[str] = mapped_column(String(60), default="AI Image", index=True)
    visual_style: Mapped[str] = mapped_column(String(80), default="Cinematic")
    preview_url: Mapped[str] = mapped_column(String(600), default="")
    tools: Mapped[list] = mapped_column(JSON, default=list)
    skills: Mapped[list] = mapped_column(JSON, default=list)
    workflow: Mapped[str] = mapped_column(Text, default="Concept → generation → refinement → export")
    prompt_notes: Mapped[str] = mapped_column(Text, default="", nullable=True)
    prompt_private: Mapped[bool] = mapped_column(Boolean, default=True)
    aspect_ratio: Mapped[str] = mapped_column(String(20), default="16:9")
    output_format: Mapped[str] = mapped_column(String(30), default="MP4")
    commercial_use: Mapped[bool] = mapped_column(Boolean, default=False)
    license_type: Mapped[str] = mapped_column(String(80), default="Review required")
    visibility: Mapped[str] = mapped_column(String(20), default="Public", index=True)
    is_demo: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    creator: Mapped[CreatorProfile] = relationship(back_populates="projects")

class CreativeBrief(Base):
    __tablename__ = "creative_briefs"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    brand_name: Mapped[str] = mapped_column(String(140), default="Independent Brand")
    title: Mapped[str] = mapped_column(String(180), index=True)
    description: Mapped[str] = mapped_column(Text)
    industry: Mapped[str] = mapped_column(String(80), default="Technology")
    objective: Mapped[str] = mapped_column(String(160), default="Brand awareness")
    target_audience: Mapped[str] = mapped_column(String(200), default="")
    content_type: Mapped[str] = mapped_column(String(60), default="AI Video", index=True)
    visual_style: Mapped[str] = mapped_column(String(80), default="Cinematic")
    platform: Mapped[str] = mapped_column(String(80), default="Instagram")
    aspect_ratio: Mapped[str] = mapped_column(String(20), default="9:16")
    output_format: Mapped[str] = mapped_column(String(40), default="MP4")
    budget_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    budget_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    deadline: Mapped[date | None] = mapped_column(Date, nullable=True)
    deliverables: Mapped[int] = mapped_column(Integer, default=1)
    required_skills: Mapped[list] = mapped_column(JSON, default=list)
    required_tools: Mapped[list] = mapped_column(JSON, default=list)
    commercial_use: Mapped[bool] = mapped_column(Boolean, default=False)
    license_type: Mapped[str] = mapped_column(String(80), default="Non-exclusive")
    usage_rights: Mapped[str] = mapped_column(Text, default="Confirm usage rights with creator")
    ai_disclosure: Mapped[str] = mapped_column(String(80), default="Disclose AI-generated content")
    revision_rounds: Mapped[int] = mapped_column(Integer, default=2)
    status: Mapped[str] = mapped_column(String(30), default="Published", index=True)
    is_demo: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Application(Base):
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(primary_key=True)
    brief_id: Mapped[int] = mapped_column(ForeignKey("creative_briefs.id", ondelete="CASCADE"), index=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("creator_profiles.id", ondelete="CASCADE"), index=True)
    proposal: Mapped[str] = mapped_column(Text, default="")
    proposed_budget: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="Applied")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Collaboration(Base):
    __tablename__ = "collaborations"
    id: Mapped[int] = mapped_column(primary_key=True)
    brief_id: Mapped[int] = mapped_column(ForeignKey("creative_briefs.id", ondelete="CASCADE"), index=True)
    brand_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    creator_id: Mapped[int] = mapped_column(ForeignKey("creator_profiles.id"))
    status: Mapped[str] = mapped_column(String(30), default="In Discussion")
    activity_log: Mapped[list] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class VerificationEvidence(Base):
    __tablename__ = "verification_evidence"
    id: Mapped[int] = mapped_column(primary_key=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey("creator_profiles.id", ondelete="CASCADE"), index=True)
    evidence_type: Mapped[str] = mapped_column(String(60))
    evidence_reference: Mapped[str] = mapped_column(Text)
    review_status: Mapped[str] = mapped_column(String(30), default="Pending")
    reviewed_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
