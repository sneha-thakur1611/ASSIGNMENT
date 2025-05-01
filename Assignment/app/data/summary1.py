from app.data.ingestion import fetch_all_assets

async def generate_mock_summary() -> str:
    assets = await fetch_all_assets()

    if not assets:
        return "No data available to generate summary."

    lines = []
    for asset in assets:
        if "error" in asset:
            continue
        lines.append(
            f"{asset['symbol']} is currently at ${asset['latest_price']} "
            f"with a 24h change of {asset['change_percent_24h']}% "
            f"and a 7-day average of ${asset['average_price_7d']}."
        )

    summary = " ".join(lines)
    return summary