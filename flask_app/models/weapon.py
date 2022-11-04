from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import team

class weapon:
    db = "Splatoon3Hub"
    def __init__(self, id, name):
        self.id = id
        self.name = name



# weapons = [
#     "Hero Shot Replica",
#     "Splattershot Jr.",
#     "Splat Charger",
#     "Splat Roller",
#     "Splattershot",
#     "Blaster",
#     "Splat Dualies",
#     "Slosher",
#     "Octobrush",
#     "Heavy Splatling",
#     "Tri-Stringer",
#     "Splat Brella",
#     "Aerospray MG",
#     "Splatana Wiper",
#     "Carbon Roller",
#     "N-ZAP '85",
#     "Rapid Blaster",
#     "Inkbrush",
#     "Classic Squiffer",
#     "Dualie Squelchers",
#     "Splatershot Pro",
#     "Sploosh-o-matic",
#     "Splatterscope",
#     "Tri-Slosher",
#     "REEF-LUX 450",
#     "Range Blaster",
#     ".52 Gal",
#     "Dynamo Roller",
#     "Mini Splatling",
#     "Luna Blaster",
#     "L-3 Nozzlenose",
#     "Dapple Dualies",
#     "Sloshing Machine",
#     "Jet Squelcher",
#     "Splatana Stamper",
#     "Tenta Brella",
#     "Splach-o-matic",
#     "Dark Tetra Dualies",
#     ".96 Gal",
#     "Undercover Brella",
#     "E-Liter 4K",
#     "Squeezer",
#     "Bloblobber",
#     "Flingza Roller",
#     "Hydra Splatling",
#     "Glooga Dualies",
#     "Clash Blaster",
#     "Bamboozler 14 Mk 1",
#     "H-3 Nozzlenose",
#     "Goo Tuber",
#     "Rapid Blaster Pro",
#     "E-Liter 4K Scope",
#     "Nautilus 47",
#     "Explosher",
#     "Ballpoint Splatling"
# ]