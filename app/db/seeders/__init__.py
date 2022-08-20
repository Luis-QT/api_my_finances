""" Init seeders """
from app.db.seeders.months import generate_months
from app.db.seeders.type_operations import generate_type_operations
from app.db.seeders.users import generate_users

def run_seeds(db):
    """ Run seed """
    generate_users(db)
    generate_type_operations(db)
    generate_months(db)

    # if eval(os.environ['SEED_TEST']) is True:
    #     generate_other_seeders(db)
