import hashlib
import re


def get_md5(str):
    """
    md5加密算法
    :param str:
    :return:
    """
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()


def parse_url(str):
    """
    判断给定的音频地址是否是正确的url
    :param str:
    :return:
    """
    match = re.findall("www.gov.cn", str)
    if not match:
        new_url = "http://www.gov.cn"+str
    else:
        new_url = str
    return new_url