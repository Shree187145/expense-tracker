
from sqlalchemy.orm import Session
from app import models
from app.schemas import ExpenseCreate, ExpenseUpdate


# Create expense
def create_expense(db: Session, expense: ExpenseCreate):
    new_expense = models.Expense(**expense.model_dump())

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


# Read all expenses
def get_all_expenses(db: Session):
    return db.query(models.Expense).all()


# Read one expense
def get_expense(db: Session, expense_id: int):
    return db.query(models.Expense).filter(
        models.Expense.id == expense_id
    ).first()


# Update expense
def update_expense(
    db: Session,
    expense_id: int,
    expense_data: ExpenseUpdate
):
    expense = get_expense(db, expense_id)

    if expense is None:
        return None

    for key, value in expense_data.model_dump(exclude_unset=True).items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)

    return expense


# Delete expense
def delete_expense(db: Session, expense_id: int):
    expense = get_expense(db, expense_id)

    if expense is None:
        return None

    db.delete(expense)
    db.commit()

    return expense
