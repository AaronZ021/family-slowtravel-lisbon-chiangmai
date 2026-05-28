#!/usr/bin/env python3
import csv
import hashlib
import json
import time
import urllib.parse
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed"
CACHE = ROOT / "data" / "cache"

AREAS = [
    ("lisbon", "Campo de Ourique", 38.7153262, -9.1679353),
    ("lisbon", "Estrela / Lapa", 38.7147150, -9.1592192),
    ("lisbon", "Parque das Nacoes", 38.7638712, -9.0953729),
    ("lisbon", "Belem / Restelo", 38.6980808, -9.2144079),
    ("chiang_mai", "Nimman / Santitham", 18.7990098, 98.9719744),
    ("chiang_mai", "Old City outer edge", 18.7822420, 98.9794442),
    ("chiang_mai", "Hang Dong", 18.6856866, 98.9192218),
    ("chiang_mai", "San Sai", 18.8491034, 99.0451285),
]

CITIES = [
    ("lisbon", 38.7223, -9.1393),
    ("chiang_mai", 18.7883, 98.9853),
]

TARGET_MONTHS = {1, 2, 3, 4, 10, 11}


def get_json(url, cache_path, sleep_after=0, retries=2):
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists():
        return json.loads(cache_path.read_text())
    req = urllib.request.Request(url, headers={"User-Agent": "family-slowtravel-local-research/1.0"})
    last_error = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read().decode("utf-8")
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt >= retries:
                raise
            time.sleep(8 * (attempt + 1))
    cache_path.write_text(data)
    if sleep_after:
        time.sleep(sleep_after)
    return json.loads(data)


def overpass_query(lat, lon, radius, mode="full"):
    if mode == "daily":
        body = f"""
      node(around:{radius},{lat},{lon})["leisure"="playground"];
      way(around:{radius},{lat},{lon})["leisure"="playground"];
      relation(around:{radius},{lat},{lon})["leisure"="playground"];
      node(around:{radius},{lat},{lon})["leisure"="park"];
      way(around:{radius},{lat},{lon})["leisure"="park"];
      relation(around:{radius},{lat},{lon})["leisure"="park"];
      node(around:{radius},{lat},{lon})["amenity"="pharmacy"];
      node(around:{radius},{lat},{lon})["shop"="supermarket"];
      node(around:{radius},{lat},{lon})["shop"="convenience"];
      node(around:{radius},{lat},{lon})["shop"="laundry"];
      node(around:{radius},{lat},{lon})["amenity"="hospital"];
      way(around:{radius},{lat},{lon})["amenity"="hospital"];
      node(around:{radius},{lat},{lon})["amenity"="clinic"];
        """
    else:
        body = f"""
      node(around:{radius},{lat},{lon})["leisure"="playground"];
      way(around:{radius},{lat},{lon})["leisure"="playground"];
      relation(around:{radius},{lat},{lon})["leisure"="playground"];
      node(around:{radius},{lat},{lon})["leisure"="park"];
      way(around:{radius},{lat},{lon})["leisure"="park"];
      relation(around:{radius},{lat},{lon})["leisure"="park"];
      node(around:{radius},{lat},{lon})["amenity"="pharmacy"];
      node(around:{radius},{lat},{lon})["shop"="supermarket"];
      node(around:{radius},{lat},{lon})["shop"="convenience"];
      node(around:{radius},{lat},{lon})["shop"="laundry"];
      node(around:{radius},{lat},{lon})["amenity"="hospital"];
      way(around:{radius},{lat},{lon})["amenity"="hospital"];
      node(around:{radius},{lat},{lon})["amenity"="clinic"];
      node(around:{radius},{lat},{lon})["amenity"="cafe"];
        """
    return f"""
    [out:json][timeout:60];
    (
      {body}
    );
    out tags center;
    """


def classify(tags):
    if tags.get("leisure") == "playground":
        return "playground"
    if tags.get("leisure") == "park":
        return "park"
    if tags.get("amenity") == "pharmacy":
        return "pharmacy"
    if tags.get("shop") in ("supermarket", "convenience"):
        return "grocery"
    if tags.get("shop") == "laundry":
        return "laundry"
    if tags.get("amenity") == "hospital":
        return "hospital"
    if tags.get("amenity") == "clinic":
        return "clinic"
    if tags.get("amenity") == "cafe":
        return "cafe"
    return "other"


def collect_poi():
    rows = []
    samples = []
    for city, area, lat, lon in AREAS:
        for radius in (1000, 5000):
            mode = "daily" if radius >= 5000 else "full"
            q = overpass_query(lat, lon, radius, mode=mode)
            digest = hashlib.sha1(q.encode()).hexdigest()[:12]
            url = "https://overpass-api.de/api/interpreter?data=" + urllib.parse.quote(q)
            cache_path = CACHE / "overpass" / f"{city}_{area.replace(' ', '_').replace('/', '_')}_{radius}_{digest}.json"
            try:
                data = get_json(url, cache_path, sleep_after=2)
                status = "ok"
            except Exception as exc:
                data = {"elements": []}
                status = f"failed: {type(exc).__name__}"
            counts = defaultdict(int)
            names = defaultdict(list)
            seen = set()
            for el in data.get("elements", []):
                tags = el.get("tags", {})
                cat = classify(tags)
                key = (el.get("type"), el.get("id"), cat)
                if cat == "other" or key in seen:
                    continue
                seen.add(key)
                counts[cat] += 1
                nm = tags.get("name") or tags.get("name:en") or tags.get("brand")
                if nm and len(names[cat]) < 8:
                    names[cat].append(nm)
            rows.append({
                "city": city,
                "area": area,
                "radius_m": radius,
                "playgrounds": counts["playground"],
                "parks": counts["park"],
                "grocery": counts["grocery"],
                "pharmacies": counts["pharmacy"],
                "laundry": counts["laundry"],
                "hospitals": counts["hospital"],
                "clinics": counts["clinic"],
                "cafes": counts["cafe"],
                "sample_playgrounds": "; ".join(names["playground"]),
                "sample_parks": "; ".join(names["park"]),
                "sample_grocery": "; ".join(names["grocery"]),
                "query_status": status,
            })
            samples.append({
                "city": city,
                "area": area,
                "radius_m": radius,
                "cache_file": str(cache_path.relative_to(ROOT)),
                "overpass_endpoint": "https://overpass-api.de/api/interpreter",
            })
    out = OUT / "poi_summary.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    with (OUT / "poi_cache_manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(samples[0].keys()))
        writer.writeheader()
        writer.writerows(samples)


def collect_open_meteo(kind):
    rows = []
    for city, lat, lon in CITIES:
        if kind == "weather":
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": "2023-01-01",
                "end_date": "2025-12-31",
                "daily": "temperature_2m_max,precipitation_sum",
                "timezone": "auto",
            }
            base = "https://archive-api.open-meteo.com/v1/archive"
        else:
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": "2023-01-01",
                "end_date": "2025-12-31",
                "hourly": "pm2_5",
                "timezone": "auto",
            }
            base = "https://air-quality-api.open-meteo.com/v1/air-quality"
        url = base + "?" + urllib.parse.urlencode(params)
        cache_path = CACHE / ("climate" if kind == "weather" else "air_quality") / f"open_meteo_{kind}_{city}_2023_2025.json"
        data = get_json(url, cache_path, sleep_after=1)
        if kind == "weather":
            by_month = defaultdict(lambda: {"temp_values": [], "rain_days": 0, "days": 0, "rain_mm": 0.0})
            daily = data["daily"]
            for d, tmax, rain in zip(daily["time"], daily["temperature_2m_max"], daily["precipitation_sum"]):
                y, m, _ = map(int, d.split("-"))
                if m not in TARGET_MONTHS:
                    continue
                key = f"{m:02d}"
                by_month[key]["days"] += 1
                if tmax is not None:
                    by_month[key]["temp_values"].append(float(tmax))
                if rain is not None:
                    by_month[key]["rain_mm"] += float(rain)
                    if float(rain) >= 1.0:
                        by_month[key]["rain_days"] += 1
            for month, vals in sorted(by_month.items()):
                avg_t = sum(vals["temp_values"]) / len(vals["temp_values"]) if vals["temp_values"] else None
                rows.append({
                    "city": city,
                    "month": month,
                    "avg_daily_high_c": round(avg_t, 1) if avg_t is not None else "",
                    "rain_days_ge_1mm_per_30d": round(vals["rain_days"] / vals["days"] * 30, 1),
                    "avg_rain_mm_per_30d": round(vals["rain_mm"] / vals["days"] * 30, 1),
                })
        else:
            by_month = defaultdict(lambda: {"vals": [], "hours": 0, "over_25": 0, "over_35": 0})
            hourly = data["hourly"]
            for ts, pm in zip(hourly["time"], hourly["pm2_5"]):
                m = int(ts[5:7])
                if m not in TARGET_MONTHS or pm is None:
                    continue
                key = f"{m:02d}"
                val = float(pm)
                by_month[key]["vals"].append(val)
                by_month[key]["hours"] += 1
                if val > 25:
                    by_month[key]["over_25"] += 1
                if val > 35:
                    by_month[key]["over_35"] += 1
            for month, vals in sorted(by_month.items()):
                avg_pm = sum(vals["vals"]) / len(vals["vals"]) if vals["vals"] else None
                rows.append({
                    "city": city,
                    "month": month,
                    "avg_pm25_ugm3": round(avg_pm, 1) if avg_pm is not None else "",
                    "pct_hours_pm25_gt_25": round(vals["over_25"] / vals["hours"] * 100, 1) if vals["hours"] else "",
                    "pct_hours_pm25_gt_35": round(vals["over_35"] / vals["hours"] * 100, 1) if vals["hours"] else "",
                })
    out = OUT / ("climate_month_summary.csv" if kind == "weather" else "air_quality_month_summary.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    collect_poi()
    collect_open_meteo("weather")
    collect_open_meteo("air")
    print("wrote processed POI, climate, and air-quality summaries")


if __name__ == "__main__":
    main()
