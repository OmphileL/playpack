from playpack import playModule
def test_add():
    assert playModule.add(1,2)  == 3, 'incorrect'
