"""" File to generate months data """
from sqlalchemy.orm import Session
from app.db.models import Month

def generate_months(db: Session):
    """ Generate months """
    months_data = [
        {'number': 1, 'name': 'Enero'},
        {'number': 2, 'name': 'Febrero'},
        {'number': 3, 'name': 'Marzo'},
        {'number': 4, 'name': 'Abril'},
        {'number': 5, 'name': 'Mayo'},
        {'number': 6, 'name': 'Junio'},
        {'number': 7, 'name': 'Julio'},
        {'number': 8, 'name': 'Agosto'},
        {'number': 9, 'name': 'Setiembre'},
        {'number': 10, 'name': 'Octubre'},
        {'number': 11, 'name': 'Noviembre'},
        {'number': 12, 'name': 'Diciembre'}
    ]
    for month_data in months_data:
        month = Month(
            number=month_data['number'],
            name=month_data['name']
        )
        db.add(month)
        db.commit()
