#!/bin/sh

# Railway sometimes sets STREAMLIT_SERVER_PORT to the literal string "$PORT".
# Fix it by replacing with the actual $PORT environment variable value.
if [ "${STREAMLIT_SERVER_PORT}" = "\$PORT" ]; then
  export STREAMLIT_SERVER_PORT="$PORT"
fi

# Start Streamlit
streamlit run app.py --server.address 0.0.0.0 --server.enableCORS false
