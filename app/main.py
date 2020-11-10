""" Modul pentru server. (TODO)"""
from sanic import Sanic
from sanic.response import json
from domain.localizer import Localizer

app = Sanic()

@app.route("/upload", metohds=["POST"])
async def test(request):
    return json({"hello" : "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
