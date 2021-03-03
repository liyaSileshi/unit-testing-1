import math

def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average():
  """Tests get average function."""
  li = [10, 90, 50]
  assert get_average(li) == 50

def test_get_average_normal_use_case():
    assert math.isclose(get_average([1,2,3,4]), 2.5)