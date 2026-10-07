import ast
from pathlib import Path
ast.parse(Path("backend/main.py").read_text(encoding="utf-8"))
print("backend syntax: OK")
print("frontend index: OK" if Path("frontend/index.html").exists() else "frontend missing")
print("assets: OK" if Path("frontend/assets/app.js").exists() and Path("frontend/assets/styles.css").exists() else "assets missing")
