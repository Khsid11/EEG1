from app import app

@app.route('/api', defaults={'path': ''})
@app.route('/api/<path:path>', methods=['GET', 'POST'])
def api(path):
    return app.wsgi_app

if __name__ == "__main__":
    app.run()
