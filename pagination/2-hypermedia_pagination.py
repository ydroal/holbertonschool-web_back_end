#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple, Dict


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
        """
        Returns a specific page of the dataset.

        Args:
            page (int, optional): The page number (start from 1)
            page_size (int, optional): The number of items per page

        Returns:
            List[List]: The page of the dataset.
        """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns pagination data.

        Args:
            page (int, optional): The page number (start from 1)
            page_size (int, optional): The number of items per page

        Returns:
            dict: The pagination data.
        """
        data_page = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": len(data_page),  # 指定されたページに表示されるアイテム（データ行）の数
            "page": page,  # 現在取得しているページのページ番号
            "data": data_page,  # データセットから取得されたアイテム（データ行）のリスト
            "next_page": page + 1 if page < total_pages else None,  # 次ページの番号
            "prev_page": page - 1 if page > 1 else None,  # 前のページのページ番号
            "total_pages": total_pages  # データセット全体を表示するのに必要な総ページ数
        }
