from app import app
from flask import request, render_template
from urllib.parse import urlparse

@app.route("/")
@app.route("/index")
@app.route("/home")
def home_page():
    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    # Static routes with static content
    links = list()
    for rule in app.url_map.iter_rules():
        if not str(rule).startswith("/admin") and not str(rule).startswith("/user"):
            if "GET" in rule.methods and len(rule.arguments) == 0:
                url = f"{host_base}{str(rule)}"
                links.append((url,str(rule)))
                
    return render_template("home.html", links=links)