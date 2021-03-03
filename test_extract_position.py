from extract_position import extract_position

def test_extract_position():
  pos1 = extract_position('|error| numerical calculations could not converge.')
  assert pos1 == None
  pos2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
  assert pos2 == '21.432'