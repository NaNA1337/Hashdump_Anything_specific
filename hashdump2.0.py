import hashlib
import string


def brute_force_hash(target_hash, max_length=5, hash_algorithm='md5'):
    # 生成一个字符集，可以是字母、数字等
    charset = string.ascii_letters + string.digits

    # 选择哈希算法
    hash_func = hashlib.new(hash_algorithm)

    # 生成从长度1到max_length的字符串
    for length in range(1, max_length + 1):
        # 使用字符集进行有序组合（不随机）
        for attempt in generate_combinations(charset, length):
            # 拼接字符以形成一个字符串
            attempt_str = ''.join(attempt)

            # 计算这个字符串的哈希值
            hash_func.update(attempt_str.encode())
            attempt_hash = hash_func.hexdigest()

            # 打印当前尝试的字符串及其哈希值（可选）
            print(f"Trying: {attempt_str} -> {attempt_hash}")

            # 检查哈希是否匹配
            if attempt_hash == target_hash:
                return attempt_str

            # 重置哈希对象以供下一次使用
            hash_func = hashlib.new(hash_algorithm)

    return None


def generate_combinations(charset, length):
    """
    生成指定长度的所有字符组合，不包含随机性。
    """
    if length == 1:
        for char in charset:
            yield char
    else:
        for char in charset:
            for suffix in generate_combinations(charset, length - 1):
                yield char + suffix


if __name__ == "__main__":
    # 示例目标哈希值（用MD5生成）
    target = "d41d8cd98f00b204e9800998ecf8427e"  # 目标 MD5 哈希值（空字符串的 MD5）

    # 选择哈希算法，如 'md5', 'sha1', 'sha256' 等
    hash_algorithm = 'md5'

    # 爆破哈希值，寻找匹配的字符串
    result = brute_force_hash(target, hash_algorithm=hash_algorithm)

    if result:
        print(f"匹配的字符串: {result}")
    else:
        print("没有匹配的字符串")
