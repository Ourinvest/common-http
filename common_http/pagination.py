import math


def pagination(collection, cursor, query: dict, page=1, items_per_page=10):
    try:
        page = int(page) or 1  # if evaluates to 0, becomes 1 (min value)
    except ValueError:
        page = 1

    try:
        items_per_page = int(items_per_page) or 1  # if evaluates to 0, becomes 1 (min value)
    except ValueError:
        items_per_page = 10

    total_items = collection.count_documents(query)
    total_pages = math.ceil(total_items / items_per_page)
    total_pages = total_pages if total_pages > 0 else 1

    if page > total_pages:
        page = total_pages

    items = cursor.skip((page - 1) * items_per_page).limit(items_per_page)

    return items, total_pages, total_items


def pagination_schema(collection, cursor, query, schema, page=1, items_per_page=10):
    data, total_pages, total_items = pagination(collection, cursor, query, page, items_per_page)
    return {
        "items": schema().dump(data, many=True),
        "items_total": total_items,
        "items_per_page": int(items_per_page),
        "current_page": int(page),
        "total_pages": total_pages,
    }
