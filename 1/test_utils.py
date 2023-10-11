import pytest
from utils import *


def test_total_word_count():
    data = {'0100405060': ['the', 'red', 'magnet', 'elephant', 'market'],
            '0100405040': ['elephant', 'magnet', 'the', 'market'],
            '0410500030': ['the', 'red', 'violin', 'wolf'],
            '3900339302': ['the', 'yellow', 'magnet', 'potato', 'the', 'bob', 'elephant']}

    assert total_word_count(data, "the") == 5
    assert total_word_count(data, "red") == 2
    assert total_word_count(data, "magnet") == 3


def test_unique_count():
    data = {'0101010101': ['the', 'quick', 'brown', 'fox'],
            '0202020202': ['jumped', 'over', 'the', 'lazy', 'dog'],
            '0303030202': ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']}

    # Test Case 1
    chapters = ['01', '02', '03']
    word = 'the'
    assert unique_count(data, chapters, word) == 3

    # Test Case 2
    chapters = ['01', '02', '03']
    word = 'jumped'
    assert unique_count(data, chapters, word) == 2

    # Test Case 3
    chapters = ['01', '02', '03']
    word = 'cat'
    assert unique_count(data, chapters, word) == 0


def test_split_tarrifs():
    tarrifs = ['0100405060', '0100405040', '0410500030', '3900339302']
    expected_result = {
        'chapters': ['01', '01', '04', '39'],
        'headings': ['0100', '0100', '0410', '3900'],
        'subheadings': ['010040', '010040', '041050', '390033'],
        'duty rates': ['01004050', '01004050', '04105000', '39003393']
    }
    tarrifs2 = ['0203040566', '0197405040', '9876543211', '1928374653']
    expected_result2 = {
        'chapters': ['02', '01', '98', '19'],
        'headings': ['0203', '0197', '9876', '1928'],
        'subheadings': ['020304', '019740', '987654', '192837'],
        'duty rates': ['02030405', '01974050', '98765432', '19283746']
    }
    # test case 1
    assert split_tarrifs(tarrifs) == expected_result

    # test case 2
    assert split_tarrifs(tarrifs2) == expected_result2


def test_total_chapter_values():
    data = {
        "01004050": ["red", "apple", "market", "dog", "green"],
        "01005050": ["banana", "carrot", "flower", "dog", "elephant"],
        "02004050": ["red", "banana", "market", "elephant", "green"],
        "03004050": ["carrot", "dog", "elephant", "green"],
        "04004050": ["red", "apple", "dog", "elephant", "green"],
        "05004050": ["apple", "carrot", "dog", "elephant", "green"],
        "05004150": ["apple", "carrot", "dog", "elephant", "green"],
    }
    chapters = ["0100", "0200", "0300"]
    word = "dog"
    assert max_word_occurrences(data, chapters, word) == 2

@pytest.fixture
def unique_words():
    return ['elephant', 'market', 'potato', 'red', 'the', 'violin', 'yellow']


@pytest.fixture
def tarrifs_data():
    return {
        'chapters': ['01', '01', '04', '39'],
        'headings': ['0100', '0100', '0410', '3900'],
        'subheadings': ['010040', '010040', '041050', '390033'],
        'duty rates': ['01004050', '01004050', '04105000', '39003393']
    }


@pytest.fixture
def input_data():
    return {
        '0100405060': ['the', 'red', 'elephant', 'market'],
        '0100405040': ['elephant', 'the', 'market'],
        '0410500030': ['the', 'red', 'violin'],
        '3900339302': ['the', 'yellow', 'potato', 'the', 'elephant']
    }


def test_solution(unique_words, tarrifs_data, input_data):
    result = solution(unique_words, tarrifs_data, input_data)
    assert result['Word'] == unique_words
    assert result['TotalCount'] == [3, 2, 1, 2, 5, 1, 1]
    assert result['SingleChapterMaxCount'] == [2, 2, 1, 1, 2, 1, 1]
    assert result['UniqueChaptersCount'] == [2, 1, 1, 2, 3, 1, 1]
    assert result['SingleHeadingMaxCount'] == [2, 2, 1, 1, 2, 1, 1]
    assert result['UniqueHeadingCount'] == [2, 1, 1, 2, 3, 1, 1]
    assert result['SingleSubheadingMaxCount'] == [2, 2, 1, 1, 2, 1, 1]
    assert result['UniqueSubheadingCount'] == [2, 1, 1, 2, 3, 1, 1]
    assert result['SingleDutyRateMaxCount'] == [2, 2, 1, 1, 2, 1, 1]
    assert result['UniqueDutyRateCount'] == [2, 1, 1, 2, 3, 1, 1]
    assert result['SingleTariffMaxCount'] == [1, 1, 1, 1, 2, 1, 1]
    assert result['UniqueTariffCount'] == [3, 2, 1, 2, 4, 1, 1]


@pytest.fixture
def test_data():
    unique_words2 = ['apple', 'banana', 'carrot', 'dog', 'elephant', 'flower', 'green']
    tariff_data2 = {
        'chapters': ['01', '02', '03', '04', '05'],
        'headings': ['0100', '0200', '0300', '0400', '0500'],
        'subheadings': ['010040', '020040', '030040', '040040', '050040'],
        'duty rates': ['01004050', '02004050', '03004050', '04004050', '05004050']
    }
    input_data2 = {
        '0100405010': ['dog', 'elephant', 'green', 'banana', 'apple', 'flower', 'carrot', 'banana', 'carrot',
                       'elephant', 'banana', 'apple'],
        '0200405020': ['dog', 'carrot', 'green', 'elephant', 'flower', 'banana', 'apple', 'elephant', 'carrot',
                       'green'],
        '0300405020': ['green', 'elephant', 'carrot', 'banana', 'dog', 'apple', 'flower', 'banana', 'carrot',
                       'elephant'],
        '0400405020': ['dog', 'elephant', 'green', 'banana', 'carrot', 'flower', 'dog', 'apple', 'elephant',
                       'carrot'],
        '0500405010': ['flower', 'dog', 'banana', 'carrot', 'elephant', 'green', 'apple', 'banana', 'carrot',
                       'dog'],
    }
    return unique_words2, tariff_data2, input_data2


def test_solution2(test_data):
    unique_words2, tariff_data2, input_data2 = test_data
    result = solution(unique_words2, tariff_data2, input_data2)
    assert result['Word'] == unique_words2
    assert result['TotalCount'] == [6, 9, 10, 7, 9, 5, 6]
    assert result['SingleChapterMaxCount'] == [2, 3, 2, 2, 2, 1, 2]
    assert result['UniqueChaptersCount'] == [5, 5, 5, 5, 5, 5, 5]
    assert result['SingleHeadingMaxCount'] == [2, 3, 2, 2, 2, 1, 2]
    assert result['UniqueHeadingCount'] == [5, 5, 5, 5, 5, 5, 5]
    assert result['SingleSubheadingMaxCount'] == [2, 3, 2, 2, 2, 1, 2]
    assert result['UniqueSubheadingCount'] == [5, 5, 5, 5, 5, 5, 5]
    assert result['SingleDutyRateMaxCount'] == [2, 3, 2, 2, 2, 1, 2]
    assert result['UniqueDutyRateCount'] == [5, 5, 5, 5, 5, 5, 5]
    assert result['SingleTariffMaxCount'] == [2, 3, 2, 2, 2, 1, 2]
    assert result['UniqueTariffCount'] == [5, 5, 5, 5, 5, 5, 5]
