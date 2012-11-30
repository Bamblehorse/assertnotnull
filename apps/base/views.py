import json
from common.jsondecorator import render_to_json

@render_to_json()
def jsons(request):
    jsondata = json.load(open('/home/branwulf/Projets/jsonsmall.txt'))
    return jsondata