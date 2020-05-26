import sys
import requests
import hashlib

# TO DO:
# add nice command line interface -> https://www.sicara.ai/blog/2018-12-18-perfect-command-line-interfaces-python

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again.")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwnd_api_check(password):
    """ check if password exists in api response """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    if args:
        for password in args:
            count = pwnd_api_check(password)
            if count:
                print(f"{password} was found {count} time(s). Don't use this password!")
            else:
                print(f"{password} was not found. You may still use it.")
    else:
        print("No password given.")


if __name__ == "__main__":
    main(sys.argv[1:])
