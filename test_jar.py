from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10

def test_deposity_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def test_limit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(3)
        jar.withdraw(4)

def test_wrong_value():
  
    with pytest.raises(ValueError):
        jar = Jar(-1)
    
    with pytest.raises(ValueError):
        jar = Jar('cat')
