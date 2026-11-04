"""Post-extraction consistency check; no OCR or NuMind model is run."""
from decimal import Decimal
import json
from pathlib import Path


def supported(candidate):
    if candidate["printed_total"] is None:
        return False
    total = Decimal(candidate["total"])
    return (sum((Decimal(x) for x in candidate["lines"]), Decimal("0"))
            + Decimal(candidate["tax"]) == total
            and total == Decimal(candidate["printed_total"]))


def run():
    fixtures = json.loads((Path(__file__).parent / "fixtures.json").read_text())
    rows = []
    for item in fixtures:
        first = item["candidates"][0]["id"] if item["candidates"] else None
        valid = [x["id"] for x in item["candidates"] if supported(x)]
        checked = valid[0] if len(valid) == 1 else None
        rows.append({"case": item["case"], "expected": item["expected"],
                     "first_candidate": first, "constraint_check": checked,
                     "first_correct": first == item["expected"],
                     "checked_correct": checked == item["expected"]})
    return {"cases": len(rows),
            "first_candidate_correct": sum(x["first_correct"] for x in rows),
            "constraint_check_correct": sum(x["checked_correct"] for x in rows),
            "constraint_abstentions": sum(x["constraint_check"] is None for x in rows),
            "rows": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
