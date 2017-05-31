import project_euler as pe


# import pytest
# import time


# @pytest.mark.benchmark(
#     group="tests",
#     max_time=0.5,
#     min_rounds=5,
#     timer=time.time,
#     disable_gc=True,
#     warmup=False
# )

def test_problem_001():
    result = pe.problem_001.problem_001()
    assert result == 233168


def test_problem_001_bench(benchmark):
    result = benchmark(pe.problem_001.problem_001)
    assert result == 233168


def test_problem_002():
    result = pe.problem_002.problem_002()
    assert result == 4613732


def test_problem_002_bench(benchmark):
    result = benchmark(pe.problem_002.problem_002)
    assert result == 4613732


def test_problem_003():
    result = pe.problem_003.problem_003()
    assert result == 6857


def test_problem_003_bench(benchmark):
    result = benchmark(pe.problem_003.problem_003)
    assert result == 6857


def test_problem_004():
    result = pe.problem_004.problem_004()
    assert result == 906609


def test_problem_004_bench(benchmark):
    result = benchmark(pe.problem_004.problem_004)
    assert result == 906609


def test_problem_005():
    result = pe.problem_005.problem_005()
    assert result == 232792560


def test_problem_005_bench(benchmark):
    result = benchmark(pe.problem_005.problem_005)
    assert result == 232792560


def test_problem_006():
    result = pe.problem_006.problem_006()
    assert result == 25164150


def test_problem_006_bench(benchmark):
    result = benchmark(pe.problem_006.problem_006)
    assert result == 25164150


def test_problem_007():
    result = pe.problem_007.problem_007()
    assert result == 104743


def test_problem_007_bench(benchmark):
    result = benchmark(pe.problem_007.problem_007)
    assert result == 104743


def test_problem_008():
    result = pe.problem_008.problem_008()
    assert result == 23514624000


def test_problem_008_bench(benchmark):
    result = benchmark(pe.problem_008.problem_008)
    assert result == 23514624000


def test_problem_009():
    result = pe.problem_009.problem_009()
    assert result == 31875000


def test_problem_009_bench(benchmark):
    result = benchmark(pe.problem_009.problem_009)
    assert result == 31875000


def test_problem_010():
    result = pe.problem_010.problem_010()
    assert result == 142913828922


def test_problem_010_bench(benchmark):
    result = benchmark(pe.problem_010.problem_010)
    assert result == 142913828922


def test_problem_011():
    result = pe.problem_011.problem_011()
    assert result == 70600674


def test_problem_011_bench(benchmark):
    result = benchmark(pe.problem_011.problem_011)
    assert result == 70600674


def test_problem_012():
    result = pe.problem_012.problem_012()
    assert result == 76576500


def test_problem_012_bench(benchmark):
    result = benchmark(pe.problem_012.problem_012)
    assert result == 76576500


def test_problem_013():
    result = pe.problem_013.problem_013()
    assert result == 5537376230


def test_problem_013_bench(benchmark):
    result = benchmark(pe.problem_013.problem_013)
    assert result == 5537376230


def test_problem_014():
    result_a = pe.problem_014.problem_014_a()
    assert result_a == 837799
    result_a = pe.problem_014.problem_014_a()
    assert result_a == 837799


def test_problem_014_method_a_bench(benchmark):
    result = benchmark(pe.problem_014.problem_014_a)
    assert result == 837799


def test_problem_014_method_b_bench(benchmark):
    result = benchmark(pe.problem_014.problem_014_b)
    assert result == 837799


def test_problem_015():
    result = pe.problem_015.problem_015()
    assert result == 137846528820


def test_problem_015_bench(benchmark):
    result = benchmark(pe.problem_015.problem_015)
    assert result == 137846528820


def test_problem_016():
    result = pe.problem_016.problem_016()
    assert result == 1366


def test_problem_016_bench(benchmark):
    result = benchmark(pe.problem_016.problem_016)
    assert result == 1366


def test_problem_017():
    result = pe.problem_017.problem_017()
    assert result == 21124


def test_problem_017_bench(benchmark):
    result = benchmark(pe.problem_017.problem_017)
    assert result == 21124


def test_problem_018():
    result = pe.problem_018.problem_018()
    assert result == 1074


def test_problem_018_bench(benchmark):
    result = benchmark(pe.problem_018.problem_018)
    assert result == 1074


def test_problem_019():
    result_a = pe.problem_019.problem_019_a()
    assert result_a == 171
    result_b = pe.problem_019.problem_019_b()
    assert result_b == 171


def test_problem_019_a_bench(benchmark):
    result = benchmark(pe.problem_019.problem_019_a)
    assert result == 171


def test_problem_019_b_bench(benchmark):
    result = benchmark(pe.problem_019.problem_019_b)
    assert result == 171


def test_problem_020():
    result = pe.problem_020.problem_020()
    assert result == 648


def test_problem_020_bench(benchmark):
    result = benchmark(pe.problem_020.problem_020)
    assert result == 648


def test_problem_021():
    result = pe.problem_021.problem_021()
    assert result == 31626


def test_problem_021_bench(benchmark):
    result = benchmark(pe.problem_021.problem_021)
    assert result == 31626


def test_problem_022():
    result = pe.problem_022.problem_022()
    assert result == 871198282


def test_problem_022_bench(benchmark):
    result = benchmark(pe.problem_022.problem_022)
    assert result == 871198282


def test_problem_023():
    result = pe.problem_023.problem_023()
    assert result == 4179871


def test_problem_023_bench(benchmark):
    result = benchmark(pe.problem_023.problem_023)
    assert result == 4179871


def test_problem_024():
    result = pe.problem_024.problem_024()
    assert result == 2783915460


def test_problem_024_bench(benchmark):
    result = benchmark(pe.problem_024.problem_024)
    assert result == 2783915460


def test_problem_025():
    result = pe.problem_025.problem_025()
    assert result == 4782


def test_problem_025_bench(benchmark):
    result = benchmark(pe.problem_025.problem_025)
    assert result == 4782


def test_problem_026():
    result = pe.problem_026.problem_026()
    assert result == 983


def test_problem_026_bench(benchmark):
    result = benchmark(pe.problem_026.problem_026)
    assert result == 983


def test_problem_027():
    result = pe.problem_027.problem_027()
    assert result == -59231


def test_problem_027_bench(benchmark):
    result = benchmark(pe.problem_027.problem_027)
    assert result == -59231


def test_problem_028():
    result = pe.problem_028.problem_028()
    assert result == 669171001


def test_problem_028_bench(benchmark):
    result = benchmark(pe.problem_028.problem_028)
    assert result == 669171001


def test_problem_029():
    result = pe.problem_029.problem_029()
    assert result == 9183


def test_problem_029_bench(benchmark):
    result = benchmark(pe.problem_029.problem_029)
    assert result == 9183


def test_problem_030():
    result = pe.problem_030.problem_030()
    assert result == 443839


def test_problem_030_bench(benchmark):
    result = benchmark(pe.problem_030.problem_030)
    assert result == 443839


def test_problem_031():
    result = pe.problem_031.problem_031()
    assert result == 73682


def test_problem_031_bench(benchmark):
    result = benchmark(pe.problem_031.problem_031)
    assert result == 73682


def test_problem_032():
    result = pe.problem_032.problem_032()
    assert result == 45228


def test_problem_032_bench(benchmark):
    result = benchmark(pe.problem_032.problem_032)
    assert result == 45228


def test_problem_033():
    result = pe.problem_033.problem_033()
    assert result == 100


def test_problem_033_bench(benchmark):
    result = benchmark(pe.problem_033.problem_033)
    assert result == 100


def test_problem_034():
    result = pe.problem_034.problem_034()
    assert result == 40730


def test_problem_034_bench(benchmark):
    result = benchmark(pe.problem_034.problem_034)
    assert result == 40730


def test_problem_035():
    result = pe.problem_035.problem_035()
    assert result == 55


def test_problem_035_bench(benchmark):
    result = benchmark(pe.problem_035.problem_035)
    assert result == 55


def test_problem_036():
    result = pe.problem_036.problem_036()
    assert result == 872187


def test_problem_036_bench(benchmark):
    result = benchmark(pe.problem_036.problem_036)
    assert result == 872187


def test_problem_037():
    result = pe.problem_037.problem_037()
    assert result == 748317


def test_problem_037_bench(benchmark):
    result = benchmark(pe.problem_037.problem_037)
    assert result == 748317


def test_problem_038():
    result = pe.problem_038.problem_038()
    assert result == 932718654


def test_problem_038_bench(benchmark):
    result = benchmark(pe.problem_038.problem_038)
    assert result == 932718654


def test_problem_039():
    result = pe.problem_039.problem_039()
    assert result == 840


def test_problem_039_bench(benchmark):
    result = benchmark(pe.problem_039.problem_039)
    assert result == 840


def test_problem_040():
    result = pe.problem_040.problem_040()
    assert result == 210


def test_problem_040_bench(benchmark):
    result = benchmark(pe.problem_040.problem_040)
    assert result == 210


def test_problem_040_brute_force_bench(benchmark):
    result = benchmark(pe.problem_040.problem_040_brute_force)
    assert result == 210


def test_problem_041():
    result = pe.problem_041.problem_041()
    assert result == 7652413


def test_problem_041_bench(benchmark):
    result = benchmark(pe.problem_041.problem_041)
    assert result == 7652413


def test_problem_042():
    result = pe.problem_042.problem_042()
    assert result == 162


def test_problem_042_bench(benchmark):
    result = benchmark(pe.problem_042.problem_042)
    assert result == 162


def test_problem_043():
    result = pe.problem_043.problem_043()
    assert result == 16695334890


def test_problem_043_bench(benchmark):
    result = benchmark(pe.problem_043.problem_043)
    assert result == 16695334890


def test_problem_044():
    result = pe.problem_044.problem_044()
    assert result == 5482660


def test_problem_044_bench(benchmark):
    result = benchmark(pe.problem_044.problem_044)
    assert result == 5482660


def test_problem_045():
    result = pe.problem_045.problem_045()
    assert result == 1533776805


def test_problem_045_bench(benchmark):
    result = benchmark(pe.problem_045.problem_045)
    assert result == 1533776805


def test_problem_046():
    result = pe.problem_046.problem_046()
    assert result == 5777


def test_problem_046_bench(benchmark):
    result = benchmark(pe.problem_046.problem_046)
    assert result == 5777


def test_problem_047():
    result = pe.problem_047.problem_047()
    assert result == 134043


def test_problem_047_bench(benchmark):
    result = benchmark(pe.problem_047.problem_047)
    assert result == 134043


def test_problem_048():
    result = pe.problem_048.problem_048()
    assert result == 9110846700


def test_problem_048_bench(benchmark):
    result = benchmark(pe.problem_048.problem_048)
    assert result == 9110846700


def test_problem_049():
    result = pe.problem_049.problem_049()
    assert result == '296962999629'


def test_problem_049_bench(benchmark):
    result = benchmark(pe.problem_049.problem_049)
    assert result == '296962999629'


def test_problem_050():
    result = pe.problem_050.problem_050()
    assert result == 997651


def test_problem_050_bench(benchmark):
    result = benchmark(pe.problem_050.problem_050)
    assert result == 997651


def test_problem_051():
    result = pe.problem_051.problem_051()
    assert result == 121313


def test_problem_051_bench(benchmark):
    result = benchmark(pe.problem_051.problem_051)
    assert result == 121313


def test_problem_052():
    result = pe.problem_052.problem_052()
    assert result == 142857


def test_problem_052_bench(benchmark):
    result = benchmark(pe.problem_052.problem_052)
    assert result == 142857


def test_problem_053():
    result = pe.problem_053.problem_053()
    assert result == 4075


def test_problem_053_bench(benchmark):
    result = benchmark(pe.problem_053.problem_053)
    assert result == 4075


def test_problem_054():
    result = pe.problem_054.problem_054()
    assert result == 376


def test_problem_054_bench(benchmark):
    result = benchmark(pe.problem_054.problem_054)
    assert result == 376


def test_problem_055():
    result = pe.problem_055.problem_055()
    assert result == 249


def test_problem_055_bench(benchmark):
    result = benchmark(pe.problem_055.problem_055)
    assert result == 249


def test_problem_056():
    result = pe.problem_056.problem_056()
    assert result == 972


def test_problem_056_bench(benchmark):
    result = benchmark(pe.problem_056.problem_056)
    assert result == 972


def test_problem_057():
    result = pe.problem_057.problem_057()
    assert result == 153


def test_problem_057_bench(benchmark):
    result = benchmark(pe.problem_057.problem_057)
    assert result == 153


def test_problem_058():
    result = pe.problem_058.problem_058()
    assert result == 26241


def test_problem_058_bench(benchmark):
    result = benchmark(pe.problem_058.problem_058)
    assert result == 26241


def test_problem_059():
    result = pe.problem_059.problem_059()
    assert result == 107359


def test_problem_059_bench(benchmark):
    result = benchmark(pe.problem_059.problem_059)
    assert result == 107359


def test_problem_060():
    result = pe.problem_060.problem_060()
    assert result == 26033


def test_problem_060_bench(benchmark):
    result = benchmark(pe.problem_060.problem_060)
    assert result == 26033


def test_problem_061():
    result = pe.problem_061.problem_061()
    assert result == 28684


def test_problem_061_bench(benchmark):
    result = benchmark(pe.problem_061.problem_061)
    assert result == 28684


def test_problem_062():
    result = pe.problem_062.problem_062()
    assert result == 127035954683


def test_problem_062_bench(benchmark):
    result = benchmark(pe.problem_062.problem_062)
    assert result == 127035954683


def test_problem_063():
    result = pe.problem_063.problem_063()
    assert result == 49


def test_problem_063_bench(benchmark):
    result = benchmark(pe.problem_063.problem_063)
    assert result == 49


def test_problem_064():
    result = pe.problem_064.problem_064()
    assert result == 1322


def test_problem_064_bench(benchmark):
    result = benchmark(pe.problem_064.problem_064)
    assert result == 1322


def test_problem_065():
    result = pe.problem_065.problem_065()
    assert result == 272


def test_problem_065_bench(benchmark):
    result = benchmark(pe.problem_065.problem_065)
    assert result == 272


def test_problem_067():
    result = pe.problem_067.problem_067()
    assert result == 7273


def test_problem_067_bench(benchmark):
    result = benchmark(pe.problem_067.problem_067)
    assert result == 7273


def test_problem_068():
    result = pe.problem_068.problem_068()
    assert result == 6531031914842725


def test_problem_068_bench(benchmark):
    result = benchmark(pe.problem_068.problem_068)
    assert result == 6531031914842725


def test_problem_069():
    result = pe.problem_069.problem_069()
    assert result == 510510


def test_problem_069_bench(benchmark):
    result = benchmark(pe.problem_069.problem_069)
    assert result == 510510


def test_problem_070():
    result = pe.problem_070.problem_070()
    assert result == 8319823


def test_problem_070_bench(benchmark):
    result = benchmark(pe.problem_070.problem_070)
    assert result == 8319823


def test_problem_071():
    result = pe.problem_071.problem_071()
    assert result == 428570


def test_problem_071_bench(benchmark):
    result = benchmark(pe.problem_071.problem_071)
    assert result == 428570


def test_problem_072():
    result = pe.problem_072.problem_072()
    assert result == 303963552391


def test_problem_072_bench(benchmark):
    result = benchmark(pe.problem_072.problem_072)
    assert result == 303963552391


def test_problem_073():
    result = pe.problem_073.problem_073()
    assert result == 7295372


def test_problem_073_bench(benchmark):
    result = benchmark(pe.problem_073.problem_073)
    assert result == 7295372
