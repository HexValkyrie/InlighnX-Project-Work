import json
import yaml
import pandas as pd
import requests

# ------------------------------
# LOAD CONFIGS
# ------------------------------
with open("configs/ioc_feeds.txt", "r") as f:
    IOC_LIST = [line.strip() for line in f.readlines()]

with open("configs/mitre_mapping.json", "r") as f:
    MITRE_MAP = json.load(f)

with open("configs/sigma_rules.yml", "r") as f:
    SIGMA = yaml.safe_load(f)

# ------------------------------
# HELPER: THREAT SCORING
# ------------------------------
def calculate_score(ioc_hit, mitre_hit, behavior_hit):
    score = 0
    if ioc_hit: score += 40
    if mitre_hit: score += 30
    if behavior_hit: score += 20

    # Asset criticality (dummy fixed value)
    score += 10
    return score

# ------------------------------
# HELPER: MITRE MAPPING
# ------------------------------
def map_mitre(log):
    if " -enc " in log.get("CommandLine", ""):
        return "powershell_encoded"

    if log.get("RuleName") == "lsass_dump":
        return "lsass_dump"

    return None

# ------------------------------
# HELPER: IOC MATCH
# ------------------------------
def ioc_match(log):
    fields = ["CommandLine", "Image", "SourceImage", "TargetImage"]
    for f in fields:
        if f in log and any(ioc in str(log[f]) for ioc in IOC_LIST):
            return True
    return False

# ------------------------------
# HELPER: BEHAVIOR RULE
# ------------------------------
def sigma_match(log):
    if " -enc " in log.get("CommandLine", ""):
        return True
    return False

# ------------------------------
# PROCESS LOG
# ------------------------------
def analyze_log(log):
    mitre_key = map_mitre(log)
    mitre_hit = mitre_key is not None
    ioc_hit = ioc_match(log)
    behavior_hit = sigma_match(log)

    score = calculate_score(ioc_hit, mitre_hit, behavior_hit)

    return {
        "user": log.get("User", "N/A"),
        "hostname": log.get("Hostname", "N/A"),
        "technique": MITRE_MAP[mitre_key]["technique"] if mitre_hit else "None",
        "tactic": MITRE_MAP[mitre_key]["tactic"] if mitre_hit else "None",
        "score": score,
        "ioc_hit": ioc_hit,
        "behavior_hit": behavior_hit
    }

# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    with open("sample_logs/windows_evtx_sample.json", "r") as f:
        log = json.load(f)

    result = analyze_log(log)

    print("\n=== TVA RESULT ===")
    print(json.dumps(result, indent=4))

    # Export to CSV
    df = pd.DataFrame([result])
    df.to_csv("output/dashboard.csv", index=False)

    with open("output/results.json", "w") as f:
        json.dump(result, f, indent=4)
