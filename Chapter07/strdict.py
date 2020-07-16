#!/usr/bin/env python

class StrDict(dict):
    """ ディクショナリ型を継承してクラスを作る
    """
    def __init__(self):
        pass

    def __setitem__(self, key, value):
        """ 特殊メソッドをオーバーライド
            keyが文字列型以外なら例外を発生
        """
        if not isinstance(key, str):
            # キーが文字列でない場合には例外を発生
            raise ValueError("Key must be string.")
            # スーパークラスの特殊メソッドを呼び出し，キーと値を設定
        dict.__setitem__(self, key, value)
