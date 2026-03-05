from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from models import Category


class ExpenseBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(default=Category.OTHER.value)
    description: Optional[str] = Field(None, max_length=500)
    date: Optional[datetime] = None


class ExpenseCreate(ExpenseBase):
    """Schema for creating an expense"""
    pass


class ExpenseUpdate(BaseModel):
    """Schema for updating an expense"""
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    description: Optional[str] = Field(None, max_length=500)
    date: Optional[datetime] = None


class ExpenseResponse(ExpenseBase):
    """Schema for expense response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ExpenseSummary(BaseModel):
    """Schema for expense summary"""
    total_expenses: float
    expense_count: int
    category_breakdown: dict[str, float]
