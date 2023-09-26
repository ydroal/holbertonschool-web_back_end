#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    # 削除されたアイテムに関わらず、次にリクエストされるページは指定されたindexから始まるように
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get data from dataset starting from an index"""
        indexed_data = self.indexed_dataset()
        assert 0 <= index < len(indexed_data)

        data_page = []
        next_idx = index
        while len(data_page) < page_size and next_idx < len(indexed_data):
            if next_idx in indexed_data:
                data_page.append(indexed_data[next_idx])
            next_idx += 1

        return {
            'index': index,
            'data': data_page,
            'page_size': page_size,
            'next_index': next_idx
        }
