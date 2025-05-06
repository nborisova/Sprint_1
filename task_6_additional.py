types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicate(tickets):
    tickets_list = []
    tickets_dict = {}

    for key, value in tickets.items():
        tickets_dict[key] = []
        for i in value:
            if i not in tickets_list:
                tickets_list.append(i)
                tickets_dict[key].append(i)
            else:
                continue

    return tickets_dict
      
def get_tickets_by_type(types, tickets):
    tickets_by_type = {}

    unique_tickets = remove_duplicate(tickets)

    for key in unique_tickets.keys():
        new_key = types.get(key)
        tickets_by_type[new_key] = unique_tickets[key]

    return tickets_by_type

print(get_tickets_by_type(types, tickets))