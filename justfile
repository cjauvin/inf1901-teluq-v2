serve:
    hugo server --disableFastRender --noHTTPCache --port 1313

# Le cours en PDF et en EPUB (build/livre/site/telechargements/)
livre:
    uv run scripts/livre/generer.py
