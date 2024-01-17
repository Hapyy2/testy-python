import bubble
def test_bubble():
    assert sorted([5, 4, 6, 7, 2, 3, 1]) == bubble.sort([5, 4, 6, 7, 2, 3, 1])
    assert sorted([5, 4, 3, 1, 3, 2, 3]) == bubble.sort([5, 4, 3, 1, 3, 2, 3])