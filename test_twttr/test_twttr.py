from twttr import shorten

tests = ["haha", "tttt", "TUTUTU", "aAbB", "EIOeio", "123"]
results = ["hh", "tttt", "TTT", "bB", "","123"]
def test_shorten():
    for i,test in enumerate(tests):
        assert shorten(test)==results[i]
