mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless=true\n\
port=$port\n\
enablecors=false\n\
\n\
"> ~/.streamlit/config.toml
