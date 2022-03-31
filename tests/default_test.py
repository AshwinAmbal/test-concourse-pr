def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_name():
    name = 'Ashwin'
    assert name == 'Ashwin'
