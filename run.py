import streamlit.web.cli as stcli
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "view/app_view.py"]
    sys.exit(stcli.main())
