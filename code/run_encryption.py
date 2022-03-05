from pathlib import Path
from cryptos import nine_crypt, nine_decrypt
import os

"""
Program to encrypt and decrypt most sensitive secrets to Mari and Evangelion
3/4/2022
"""

encoding = "utf-8"
# load key from environment variables or ask for input
key_hint = "KEY_TO_MARI=a _________ girl with a ___ _____"   + "\nDecryption script will likely be recovered soon"
KEY_TO_MARI = bytes(os.environ.get("KEY_TO_MARI") or input(key_hint + "\ninput key to mari:"), encoding=encoding)
print("Attempting to process with key: ", KEY_TO_MARI)

# encyption notes
cipher = "AES-192"
sentinel = "MrRobot"
encryption_notice = f"Rest of File Encrypted (mode: {cipher}):\n{key_hint}\n"
n = 9001


def process_encryption(file_, in_notice, out_notice, encrypt_func):
    with open(file_, 'r', encoding=encoding) as f:
        doc = f.read()
        print(doc)

        plain = doc.split(in_notice)[0]
        secrets = encrypt_func(doc.split(in_notice)[1], KEY_TO_MARI)
        out_doc = plain + out_notice + secrets.decode(encoding)
    return out_doc


def main():
    proj_dir = Path().cwd().parent  # TODO may need to change this
    secrets_dir = proj_dir / "plaintext"

    # encrypt files
    # for file_ in secrets_dir.glob("*.txt"):
    #     out_doc = process_encryption(file_, sentinel, encryption_notice, nine_crypt)
    #     with open(proj_dir / file_.name, 'w', encoding=encoding) as f:
    #         f.write(out_doc)

    # decrypt files
    for file_ in proj_dir.glob('[4-9]*.txt'):
        file_ = file_.parent / file_.name
        out_doc = process_encryption(file_, encryption_notice, "Decrypted: \n", nine_decrypt)
        print(out_doc)
        with open(file_.parent / (file_.name + ".decrypted"), "w", encoding=encoding) as f:
            f.write(out_doc)


if __name__ == "__main__":
    main()
