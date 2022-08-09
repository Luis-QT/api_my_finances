"""" File to generate type_operations data """
from sqlalchemy.orm import Session
from app.db.models import TypeOperation

def generate_type_operations(db: Session):
    """ Creating type_operations """
    type_operation = TypeOperation(
        name='Entrada'
    )
    db.add(type_operation)
    db.commit()

    type_operation = TypeOperation(
        name='Salida'
    )
    db.add(type_operation)
    db.commit()
