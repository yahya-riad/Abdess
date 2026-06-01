from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

@dataclass(frozen=True)
class FieldSpec:
    name: str
    start: int
    end: int
    converter: Callable[[str], Any] = lambda s: s.strip()

def to_str(value: str) -> str:
    return value.strip()

def to_float(value: str) -> float | None:
    value = value.strip().replace(",", ".")
    return float(value) if value else None

SCHEMA = [
    FieldSpec("isin", 0, 10, to_str),
    FieldSpec("account_code", 10, 25, to_str),
    FieldSpec("product_code", 25, 35, to_str),
    FieldSpec("currency", 35, 38, to_str),
    FieldSpec("amount", 38, 53, to_float),
]

def parse_line(line: str, schema: list[FieldSpec]) -> dict:
    record = {}
    for field in schema:
        raw = line[field.start:field.end]
        record[field.name] = field.converter(raw)
    return record

def is_data_line(line: str) -> bool:
    return bool(line.strip())

def parse_file(file_path: str, schema: list[FieldSpec]) -> list[dict]:
    records = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.rstrip("\n")

            if not is_data_line(line):
                continue

            if len(line) < max(field.end for field in schema):
                raise ValueError(
                    f"Ligne {line_number} trop courte: longueur={len(line)}"
                )

            record = parse_line(line, schema)

            if record["isin"] and len(record["isin"]) != 10:
                raise ValueError(
                    f"Ligne {line_number}: ISIN invalide '{record['isin']}'"
                )

            records.append(record)

    return records



# transaction/parser/transaction_parser.py

from datetime import datetime
from transaction.model.transaction_line_dto import TransactionLineDto


def parse_date(value: str) -> datetime | None:
    value = value.strip()
    if not value or value == "00000000":
        return None
    return datetime.strptime(value, "%Y%m%d")


def parse_float(value: str) -> float | None:
    value = value.strip().replace(",", ".")
    if not value:
        return None
    return float(value)


def parse_transaction_line(line: str) -> TransactionLineDto:
    data = {
        "TransactionType": line[0:20].strip(),
        "OrderType": line[20:40].strip(),
        "Isin": line[40:52].strip(),
        "FundCode": line[52:70].strip(),
        "TradeDate": parse_date(line[70:78]),
        "SettlementDate": parse_date(line[78:86]),
        "Quantity": parse_float(line[86:101]),
        "PriceType": line[101:111].strip() or None,
        "Underlying": line[111:141].strip() or None,
        "Recycle": line[141:151].strip() or None,
        "Amount": parse_float(line[151:166]),
    }

    return TransactionLineDto.model_validate(data)


def parse_file(file_path: str) -> list[TransactionLineDto]:
    items: list[TransactionLineDto] = []

    with open(file_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")
            if not line.strip():
                continue
            items.append(parse_transaction_line(line))

    return items

