#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (start from 1)
        page_size (int): The number of items per page


    Returns:
        Tuple: size two containing a start index and an end index
    '''

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # readerから各行を取得し、それを新しいリストdatasetに保存
                dataset = [row for row in reader]
            # 最初の行（ヘッダー行）を除くすべての行をself.__datasetに保存
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        index = index_range(page, page_size)
        start_index = index[0]
        end_index = index[1]

        if start_index >= len(data) or start_index < 0:
            return []

        res = self.dataset()[start_index:end_index]  # self.datasetの呼び出し
        return res
