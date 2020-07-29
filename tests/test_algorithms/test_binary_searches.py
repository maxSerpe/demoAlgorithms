from algorithms import daysToBouquets


def test_days_to_bouquets_base_case():
    assert daysToBouquets([1, 10, 3, 10, 2], 3, 1) == 3
    assert daysToBouquets([1, 10, 3, 10, 2], 3, 2) == -1
    assert daysToBouquets([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
    assert daysToBouquets([1000000000, 1000000000], 1, 1) == 1000000000
    assert daysToBouquets([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2) == 9
