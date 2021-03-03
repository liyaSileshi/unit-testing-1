import pytest
from calculate_stat import calculate_stat
import math 

def test_calculate_stat():
  grade_list = [1, 2, 3, 4, 5]
  mean, sd = calculate_stat(grade_list)
  assert math.isclose(mean, 3,  abs_tol=1e-02)
  assert math.isclose(sd, 1.4142,  abs_tol=1e-02)