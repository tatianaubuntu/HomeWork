def test_smartphone(smartphone_fixture):
    assert smartphone_fixture.color == 'black'
    assert smartphone_fixture.quantity == 15
