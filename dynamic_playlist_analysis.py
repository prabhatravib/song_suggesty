import os
import json
import openai
from config import OPENAI_API_KEY

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY


def analyze_videos(videos: list[dict]) -> dict:
    """
    Analyze a list of YouTube videos and recommend a similar song (video) not already in the playlist.
    Expects videos as list of dicts with keys: video_id, title, url.
    Returns a dict with:
      - recommended_video: {video_id, title, url}
      - reason: string explanation
    """
    # Prepare the playlist overview
    titles = [v["title"] for v in videos]
    playlist_str = "\n".join(f"- {t}" for t in titles)

    # Construct system + user prompt
    system_prompt = (
        "You are a helpful music recommendation assistant. "
        "Given a set of YouTube video titles representing a user's existing playlist, "
        "suggest one single video not in that playlist that matches the user's taste. "
        "Provide your answer in JSON with keys 'recommended_video' (with subkeys 'video_id', 'title', 'url') and 'reason'."
    )
    user_prompt = (
        f"Here are the current playlist video titles:\n{playlist_str}\n"
        "Recommend one YouTube video (song) not in this list that best fits the mood and style. "
        "Output only valid JSON."
    )

    # Call the OpenAI ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=300,
    )

    content = response.choices[0].message.content.strip()

    # Parse JSON response
    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON response from recommendation API: {content}")

    # Validate keys
    rec = result.get("recommended_video")
    if not rec or not all(k in rec for k in ("video_id", "title", "url")):
        raise RuntimeError(f"Recommended video JSON missing required keys: {result}")

    return {
        "recommended_video": rec,
        "reason": result.get("reason", "")
    }
