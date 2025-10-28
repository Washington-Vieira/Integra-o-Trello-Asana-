import streamlit as st
from controller import sync_controller

st.title("Integração Trello → Asana (MVC Dinâmico)")

boards = sync_controller.get_boards()
workspaces = sync_controller.get_workspaces()

board_options = {board['name']: board['id'] for board in boards}
workspace_options = {ws['name']: ws['gid'] for ws in workspaces}

st.sidebar.header("Configurações")

selected_board_name = st.sidebar.selectbox("Selecione o Quadro Trello", list(board_options.keys()))
selected_workspace_name = st.sidebar.selectbox("Selecione o Workspace Asana", list(workspace_options.keys()))

board_id = board_options[selected_board_name]
workspace_id = workspace_options[selected_workspace_name]

if st.sidebar.button("Iniciar Sincronização"):
    try:
        with st.spinner("Sincronizando..."):
            results = sync_controller.sync_trello_to_asana(board_id, workspace_id)
            st.success("Sincronização concluída!")
            for res in results:
                st.write(res)
    except Exception as e:
        st.error(f"Erro: {e}")
