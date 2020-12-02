import hmac
from random import SystemRandom

# Define global variables
_sys_rng = SystemRandom()
SALT_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
DEFAULT_PBKDF2_ITERATIONS = 150000


def gen_salt(length):
    """Generate a random string of SALT_CHARS with specified ``length``."""
    if length <= 0:
        raise ValueError("Salt length must be positive")
    return "".join(_sys_rng.choice(SALT_CHARS) for _ in range(length))


def generate_hash(salt, password, method):
    salt = salt.encode("utf-8")
    password = password.encode("utf-8")
    mac = hmac.HMAC(salt, password, method)
    return mac.hexdigest()


def generate_password_hash(password, method="sha256", salt_length=8):
    """Hash a password with given hash method and salt length.

    The format for the hashed string looks like this::
        method$salt$hash

    :param password: the password to hash.
    :param method: the hash method to use (one that hashlib supports). Can
                   optionally be in the format ``pbkdf2:<method>[:iterations]``
                   to enable PBKDF2.
    :param salt_length: the length of the salt in letters.
    :return: the hashed string
    """
    salt = gen_salt(salt_length)
    hash_value = generate_hash(salt, password, method)
    return f'{method}${salt}${hash_value}'


def check_password_hash(password_hash, password):
    """Check a password against a given salted and hashed value.

    :param password_hash: a hashed string
    :param password: given password string
    :return: True if the password matched, False otherwise.
    """
    if password_hash.count("$") < 2:
        return False
    method, salt, user_hash_value = password_hash.split("$", 2)
    gen_hash_value = generate_hash(salt, password, method)
    return user_hash_value == gen_hash_value


if __name__ == '__main__':
    user_password = generate_password_hash('test')
    print(user_password.split('$',2))
    print(check_password_hash(user_password, 'test'))
