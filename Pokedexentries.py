import Pokemon_dictionaries 
from PIL import Image

class Bulbasaur:
  def bulbasaur(img, specie, entry):
    img = Image.open("https://archives.bulbagarden.net/media/upload/a/a3/Spr_1b_001.png")
    img = img.resize((200, 200))
    img.show()
    specie = print("Seed Pokemon")
    entry = print("A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.")
    
!Bulbasaur = bulbasaur()
