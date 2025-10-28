from model import trello_model, asana_model

def get_boards():
    return trello_model.get_user_boards()

def get_workspaces():
    return asana_model.get_workspaces()

def sync_trello_to_asana(board_id, workspace_id):
    trello_boards = get_boards()
    board_name = next((b['name'] for b in trello_boards if b['id'] == board_id), "Projeto Importado do Trello")

    project_id = asana_model.create_project(board_name, workspace_id)

    lists = trello_model.get_board_lists(board_id)
    results = []
    for lst in lists:
        section_id = asana_model.create_section(project_id, lst['name'])

        cards = trello_model.get_list_cards(lst['id'])
        for card in cards:
            asana_model.create_task(card['name'], card.get('desc', ''), project_id, section_id)
            results.append(f"Tarefa criada: {card['name']} na seção {lst['name']}")

    return results
