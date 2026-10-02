import json
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://git.neonteam.dev/amizing/robinsr/raw/branch/main/res.json"
OUT = Path("./common/res/avatarConfigs.json")


def main() -> None:
    req = Request(URL, headers={"User-Agent": "curl/8.0"})
    with urlopen(req) as r:
        data = json.load(r)

    configs = data["avatarConfigs"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"avatarConfigs": configs}, indent=2), encoding="utf-8")
    print(f"wrote {OUT} ({len(configs)} entries)")


if __name__ == "__main__":
    main()
