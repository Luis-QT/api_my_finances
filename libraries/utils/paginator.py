""" Paginator """

def paginate(query, params):
    """ Paginate query """
    count = query.count()
    items = query.limit(params.limit).offset(params.limit * (params.page - 1)).all()

    return count, items
