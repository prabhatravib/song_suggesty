import sqlite3
from config import ANALYTICS_DB_PATH


def init_db():
    """
    Initialize the analytics SQLite database and create the playlist_events table if it doesn't exist.
    """
    conn = sqlite3.connect(ANALYTICS_DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS playlist_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            input_type TEXT,
            playlist_url TEXT,
            recommended_video_id TEXT
        )
    ''')
    conn.commit()
    conn.close()


def track_playlist(input_type: str, playlist_url: str, recommended_video_id: str) -> None:
    """
    Record a playlist event to the analytics database.

    :param input_type: Source of playlist ('spotify' or 'youtube').
    :param playlist_url: The full playlist URL provided by the user.
    :param recommended_video_id: The ID of the recommended video.
    """
    # Ensure the DB and table exist
    init_db()

    conn = sqlite3.connect(ANALYTICS_DB_PATH)
    c = conn.cursor()
    c.execute(
        '''
        INSERT INTO playlist_events (input_type, playlist_url, recommended_video_id)
        VALUES (?, ?, ?)
        ''',
        (input_type, playlist_url, recommended_video_id)
    )
    conn.commit()
    conn.close()
