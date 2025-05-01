import httpx
from app.data.ingestion import fetch_all_assets

GROQ_API_KEY = "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"  # 🔁 Replace this with your key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

async def generate_groq_summary() -> str:
    assets = await fetch_all_assets()

    if not assets:
        return "No data available to summarize."

    lines = []
    for asset in assets:
        if "error" in asset:
            continue
        lines.append(
            f"{asset['symbol']}: Price ${asset['latest_price']}, "
            f"24h Change {asset['change_percent_24h']}%, "
            f"7d Avg ${asset['average_price_7d']}"
        )

    raw_input = "\n".join(lines)
    prompt = f"""Summarize the following financial market data in a human-readable way:\n\n{raw_input}"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a financial analyst summarizing market data."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]