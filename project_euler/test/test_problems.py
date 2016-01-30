import project_euler as pe
#import pytest
#import time


# @pytest.mark.benchmark(
#     group="tests",
#     max_time=0.5,
#     min_rounds=5,
#     timer=time.time,
#     disable_gc=True,
#     warmup=False
# )

def test_problem_001(benchmark):
    result = benchmark(pe.problem_001.problem_001)
    assert result == 233168


def test_problem_002(benchmark):
    result = benchmark(pe.problem_002.problem_002)
    assert result == 4613732


def test_problem_003(benchmark):
    result = benchmark(pe.problem_003.problem_003)
    assert result == 6857


def test_problem_004(benchmark):
    result = benchmark(pe.problem_004.problem_004)
    assert result == 906609

def test_problem_005(benchmark):
    result = benchmark(pe.problem_005.problem_005)
    assert result == 232792560


def test_problem_006(benchmark):
    result = benchmark(pe.problem_006.problem_006)
    assert result == 25164150


def test_problem_007(benchmark):
    result = benchmark(pe.problem_007.problem_007)
    assert result == 104743


def test_problem_008(benchmark):
    result = benchmark(pe.problem_008.problem_008)
    assert result == 23514624000


def test_problem_009(benchmark):
    result = benchmark(pe.problem_009.problem_009)
    assert result == 31875000
