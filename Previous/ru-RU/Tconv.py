#!/usr/bin/env python3
import re
import csv
from pathlib import Path

# Опционально: если установлен chardet, будет использован для детекции
try:
    import chardet
except Exception:
    chardet = None

# Параметры — при необходимости измените
INPUT = "MDS_3_39.rc"      # исходный файл со скриптом
CSV_OUT = "strings.csv"  # экспорт для перевода
OUTPUT = "output.txt"    # результат с подставленными переводами

# Регулярное выражение для строк в двойных кавычках (учитывает экранирование \" и \\)
STRING_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')

def detect_encoding(path: Path):
    data = path.read_bytes()
    # если chardet доступен — попробуем его
    if chardet:
        det = chardet.detect(data)
        enc = det.get("encoding")
        if enc:
            return enc
    # иначе пробуем набор распространённых кодировок
    candidates = ('utf-8', 'utf-16', 'utf-16le', 'utf-16be', 'utf-32', 'cp1251', 'cp1252', 'latin1')
    for enc in candidates:
        try:
            data.decode(enc)
            return enc
        except Exception:
            continue
    # если ничего не подошло — вернуть utf-8 и читать с заменой ошибок
    return 'utf-8'

def read_text_with_detect(path: Path):
    enc = detect_encoding(path)
    try:
        return path.read_text(encoding=enc), enc
    except Exception:
        # как запасной вариант — читать байты и декодировать с заменой ошибок
        data = path.read_bytes()
        return data.decode(enc, errors='replace'), enc

def unescape(s):
    # распаковать escape-последовательности (например \n, \t, \uXXXX)
    try:
        return bytes(s, "utf-8").decode("unicode_escape")
    except Exception:
        return s

def escape_for_source(s):
    # экранировать для помещения обратно в кавычки в исходном формате
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
    return s

def extract_strings(text):
    lst = []
    for m in STRING_RE.finditer(text):
        raw = m.group(1)
        orig = unescape(raw)
        lst.append(orig)
    return lst

def export_csv(strings, path: Path):
    seen = set()
    rows = []
    for s in strings:
        if s not in seen:
            seen.add(s)
            rows.append((s, ""))  # orig, translation
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["orig", "translation"])
        writer.writerows(rows)

def import_csv(path: Path):
    translations = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            orig = row.get("orig", "")
            tr = row.get("translation", "")
            if orig is None:
                orig = ""
            if tr is None:
                tr = ""
            translations[orig] = tr
    return translations

def replace_in_text(text, translations):
    def repl(m):
        raw = m.group(1)
        orig = unescape(raw)
        tr = translations.get(orig, "")
        if tr:
            esc = escape_for_source(tr)
            return f'"{esc}"'
        return m.group(0)
    return STRING_RE.sub(repl, text)

def main():
    p_in = Path(INPUT)
    if not p_in.exists():
        print("Исходный файл не найден:", INPUT)
        return

    text, detected = read_text_with_detect(p_in)
    print("Прочитано в кодировке:", detected)

    strings = extract_strings(text)

    p_csv = Path(CSV_OUT)
    if not p_csv.exists():
        export_csv(strings, p_csv)
        print("Создан файл для перевода:", CSV_OUT)
        print("Откройте его в редакторе и заполните колонку 'translation', затем запустите скрипт снова.")
        return

    translations = import_csv(p_csv)
    new_text = replace_in_text(text, translations)
    Path(OUTPUT).write_text(new_text, encoding="utf-8")
    print("Создан файл с подставленными переводами:", OUTPUT)

if __name__ == "__main__":
    main()
