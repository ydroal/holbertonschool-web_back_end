#!/usr/bin/env python3
'''
Module to returns the log message obfuscated:
'''
from typing import List
import re
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        # logging.Formatterクラスの初期化メソッドに、ログメッセージのフォーマット"FORMAT"を指定
        # デフォルトのログメッセージフォーマットをFORMATに設定
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Returns the log message in obfuscated form.

        Args:
            record (logging.LogRecord): The log record before obfuscation.

        Returns:
            str: log message obfuscated
        '''
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        # 指定されたフォーマットに基づいてレコードを整形
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    returns the log message obfuscated

    Args:
        fields (list): List of strings representing all fields to obfuscate
        redaction (string): String to be replaced
        message (string): String representing the log line
        separator (string): Character separating fields in log line

    Returns:
         log message obfuscated
    '''
    for field in fields:
        regex = f'{field}=([^ {separator}]*)'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logging.Logger object with the specified settings.

    Returns:
        logging.Logger object
    '''
    # loggerオブジェクトの作成
    logger = logging.getLogger('user_data')

    # user_dataからの最低出力レベルをDEBUGに設定
    logger.setLevel(logging.INFO)

    # Streamハンドラクラスをインスタンス化
    st_handler = logging.StreamHandler()

    # RedactingFormatterをハンドラに設定
    formatter = RedactingFormatter(PII_FIELDS)
    # st_handlerによる出力フォーマットを先で定義した'formatter'に設定
    st_handler.setFormatter(formatter)

    # インスタンス化したハンドラをuser_dataに渡す
    logger.addHandler(st_handler)

    # メッセージの伝播を停止
    logger.propagate = False

    return logger
