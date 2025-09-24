import subprocess

mapping = {
      "ਦਿਖਾਓ": "print", "dikhao": "print",
      "ਲੇਜਾ": "input", "leja": "input",
      "ਜੇ": "if", "je": "if",
      "ਨਹੀਂਜੇ": "elif", "nahije": "elif",
      "ਨਹੀਂਤਾਂ": "else", "nahintan": "else",
      "ਲਈ": "for", "lai": "for",
      "ਜਦਤੱਕ": "while", "jadtak": "while",
      "ਪਰਿਭਾਸ਼ਾਕਰੋ": "def", "paribhashakaro": "def",
      "ਵਰਗ": "class", "varg": "class",
      "ਵਾਪਸਦਿਓ": "return", "wapisdeo": "return",
      "ਤੋੜਦਿਓ": "break", "tordeo": "break",
      "ਜਾਰੀਰੱਖੋ": "continue", "jarirakho": "continue",
      "ਆਯਾਤਕਰੋ": "import", "aayatkaro": "import",
      "ਤੋਂ": "from", "to": "from",
      "ਦੇਤੌਰਤੇ": "as", "detaurte": "as",
      "ਨਾਲ": "with", "naal": "with",
      "ਕੋਸ਼ਿਸ਼ਕਰੋ": "try", "koshishkaro": "try",
      "ਤੋਂਇਲਾਵਾ": "except", "toillawa": "except",
      "ਅਖੀਰਕਰੇ": "finally", "akhirkare": "finally",
      "ਸੱਚ": "True", "sach": "True",
      "ਝੂਠ": "False", "jhuth": "False",
      "ਕੁਝਨਹੀਂ": "None", "kuchnahi": "None",
      "ਜਾਂ": "or", "jam": "or",
}

def translate(code: str) -> str:
    for pb_word, py_word in mapping.items():
        code = code.replace(pb_word, py_word)
    return code

with open("test.pb", "r", encoding="utf-8") as f:
    pb_code = f.read()

python_code = translate(pb_code)
with open("temp.py", "w", encoding="utf-8") as f:
    f.write(python_code)

subprocess.run(["python3", "temp.py"])
