
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/", response_model=schemas.ExpenseResponse, status_code=201)
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


@router.get("/", response_model=list[schemas.ExpenseResponse])
def list_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db)


@router.get("/{expense_id}", response_model=schemas.ExpenseResponse)
def expense_detail(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = crud.get_expense(db, expense_id)

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.put("/{expense_id}", response_model=schemas.ExpenseResponse)
def edit_expense(
    expense_id: int,
    expense_data: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    expense = crud.update_expense(db, expense_id, expense_data)

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


@router.delete("/{expense_id}")
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = crud.delete_expense(db, expense_id)

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense deleted successfully"}
