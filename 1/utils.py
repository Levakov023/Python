def split_tarrifs(tarrifs : list) -> dict:
    """
    Splits a list of tariff codes into their respective chapters, headings, subheadings and duty rates.

    Args:
    tarrifs (list): A list of strings representing tariff codes.

    Returns:
    dict: A dictionary with the following keys:
        - 'chapters': A list of the first two digits of each tariff code.
        - 'headings': A list of the first four digits of each tariff code.
        - 'subheadings': A list of the first six digits of each tariff code.
        - 'duty rates': A list of the first eight digits of each tariff code.
    """
    result = {
        "chapters": [i[:2] for i in tarrifs],
        "headings": [i[:4] for i in tarrifs],
        "subheadings": [i[:6] for i in tarrifs],
        "duty rates": [i[:8] for i in tarrifs],
    }
    return result

def max_word_occurrences(data: dict, chapters: list, word: str) -> int:
    """
    Returns the maximum number of occurrences of a given word in any part of a tariff dataset.

    Args:
    data (dict): A dictionary representing a tariff dataset, where each key represents a tariff code
                    and its corresponding value is a list of words found in the tariff description.
    chapters (list): A list of chapter codes (as strings) to search for the given word.
    word (str): The word to search for.

    Returns:
    An integer representing the maximum number of occurrences of the given word in any part.
    """
    result = []
    for chapter in chapters:
        amount = 0
        for key, value in data.items():
            if key.startswith(chapter):
                if word in value:
                    amount += value.count(word)
        result.append(amount)
    return max(result)

def unique_count(data : dict, chapters: list, word : str) -> int:
    """
    Returns the number of unique chapters in which a given word occurs in a dictionary of tariff descriptions.

    Arguments:
        - data: a dictionary of tariff descriptions, where each key represents a tariff code and each value is a list of words
        - chapters: a list of chapter codes (two-digit strings) to consider for the count
        - word: a string representing the word to search for in the descriptions

    Returns:
         An integer representing the number of unique chapters in which the given word appears at least once.
    """
    chaps_words = {i : 0 for i in chapters}
    for chapter in chapters:
        for key, value in data.items():
            if key.startswith(chapter):
                if word in value:
                    chaps_words[chapter] += 1
    return sum(1 for i in chaps_words.values() if i > 0)

def total_word_count(data : dict, word : str) -> int:
    """
    Returns the total number of occurrences of a given word across all descriptions in the data.

    Parameters:
    data (dict): A dictionary containing descriptions as values.
    word (str): The word to count.

    Returns:
    int: The total number of occurrences of the given word across all descriptions.
    """
    count = 0
    for i in data.values():
        for j in i:
            if word == j:
                count += 1
    return count

def solution(unique_words : list , tarrifs_data : dict, input_data : dict) -> dict:
    """
    Generates a dictionary with various statistics for each unique word in a given input data, using the tarrifs_data
    as a reference for chapter, heading, subheading and duty rates.

    Args:
        unique_words (list): A list of unique words to generate statistics for.
        tarrifs_data (dict): A dictionary containing tarrif codes as keys and lists of words as values.
            It is used as reference to identify the chapter, heading, subheading and duty rate for each word in input_data.
        input_data (dict): A dictionary containing words as keys and lists of tarrif codes as values.
            It is used to count the total occurrences of each word, as well as the maximum count for each word
            within a single chapter, heading, subheading, duty rate or tariff code, as well as the number of unique
            chapters, headings, subheadings, duty rates and tariff codes where each word appears.

    Returns:
        A dictionary with the following keys:
        - "Id": A list of integer IDs starting at 1 and going up to the number of unique words.
        - "Word": A list of unique words in the same order as the input unique_words.
        - "TotalCount": A list of integers representing the total count of each word in input_data.
        - "SingleChapterMaxCount": A list of integers representing the maximum count of each word in a single chapter.
        - "UniqueChaptersCount": A list of integers representing the number of unique chapters where each word appears.
        - "SingleHeadingMaxCount": A list of integers representing the maximum count of each word in a single heading.
        - "UniqueHeadingCount": A list of integers representing the number of unique headings where each word appears.
        - "SingleSubheadingMaxCount": A list of integers representing the maximum count of each word in a single subheading.
        - "UniqueSubheadingCount": A list of integers representing the number of unique subheadings where each word appears.
        - "SingleDutyRateMaxCount": A list of integers representing the maximum count of each word in a single duty rate.
        - "UniqueDutyRateCount": A list of integers representing the number of unique duty rates where each word appears.
        - "SingleTariffMaxCount": A list of integers representing the maximum count of each word in a single tariff code.
        - "UniqueTariffCount": A list of integers representing the number of unique tariff codes where each word appears.
        """

    data_for_csv = {
        "Id": [i for i in range(1, len(unique_words) + 1)],
        "Word": unique_words,
        "TotalCount": [total_word_count(input_data, i) for i in unique_words],
        "SingleChapterMaxCount": [max_word_occurrences(input_data, tarrifs_data["chapters"], i) for i in unique_words],
        "UniqueChaptersCount": [unique_count(input_data, tarrifs_data["chapters"], i) for i in
                                unique_words],
        "SingleHeadingMaxCount": [max_word_occurrences(input_data, tarrifs_data["headings"], i) for i in unique_words],
        "UniqueHeadingCount": [unique_count(input_data, tarrifs_data["headings"], i) for i in
                               unique_words],
        "SingleSubheadingMaxCount": [max_word_occurrences(input_data, tarrifs_data["subheadings"], i) for i in
                                     unique_words],
        "UniqueSubheadingCount": [unique_count(input_data, tarrifs_data["subheadings"], i) for i in
                                  unique_words],
        "SingleDutyRateMaxCount": [max_word_occurrences(input_data, tarrifs_data["duty rates"], i) for i in
                                   unique_words],
        "UniqueDutyRateCount": [unique_count(input_data, tarrifs_data["duty rates"], i) for i in
                                unique_words],
        "SingleTariffMaxCount": [max_word_occurrences(input_data, input_data.keys(), i) for i in unique_words],
        "UniqueTariffCount": [unique_count(input_data, input_data.keys(), i) for i in unique_words]
    }
    return data_for_csv
