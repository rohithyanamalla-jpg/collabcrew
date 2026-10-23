from datetime import date
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List

class RegisterIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: str = Field(min_length=5, max_length=180)
    password: str = Field(min_length=8, max_length=128)
    role: str = "creator"

class LoginIn(BaseModel):
    email: str
    password: str

class ProfileIn(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    biography: Optional[str] = None
    specialization: Optional[str] = None
    experience_level: Optional[str] = None
    availability: Optional[str] = None
    rate_min: Optional[int] = None
    rate_max: Optional[int] = None
    skills: Optional[List[str]] = None
    tools: Optional[List[str]] = None
    content_types: Optional[List[str]] = None
    formats: Optional[List[str]] = None
    aspect_ratios: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    workflow: Optional[str] = None

class PortfolioIn(BaseModel):
    title: str = Field(min_length=2, max_length=180)
    description: str = ""
    content_type: str = "AI Image"
    visual_style: str = "Cinematic"
    preview_url: str = ""
    tools: List[str] = []
    skills: List[str] = []
    workflow: str = "Concept → generation → refinement → export"
    prompt_notes: str = ""
    prompt_private: bool = True
    aspect_ratio: str = "16:9"
    output_format: str = "MP4"
    commercial_use: bool = False
    license_type: str = "Review required"
    visibility: str = "Public"

class BriefIn(BaseModel):
    title: str = Field(min_length=3, max_length=180)
    description: str = Field(min_length=10)
    brand_name: str = "Independent Brand"
    industry: str = "Technology"
    objective: str = "Brand awareness"
    target_audience: str = ""
    content_type: str = "AI Video"
    visual_style: str = "Cinematic"
    platform: str = "Instagram"
    aspect_ratio: str = "9:16"
    output_format: str = "MP4"
    budget_min: Optional[int] = None
    budget_max: Optional[int] = None
    deadline: Optional[date] = None
    deliverables: int = 1
    required_skills: List[str] = []
    required_tools: List[str] = []
    commercial_use: bool = False
    license_type: str = "Non-exclusive"
    usage_rights: str = "Confirm usage rights with creator"
    ai_disclosure: str = "Disclose AI-generated content"
    revision_rounds: int = 2
    status: str = "Draft"

class ApplicationIn(BaseModel):
    proposal: str = Field(min_length=10)
    proposed_budget: Optional[int] = None

class StatusIn(BaseModel):
    status: str

class EvidenceIn(BaseModel):
    evidence_type: str
    evidence_reference: str = Field(min_length=5)
