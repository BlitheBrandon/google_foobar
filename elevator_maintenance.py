def answer(lst):
    lst.sort(key=lambda s: map(int, s.split('.')))
    return lst
