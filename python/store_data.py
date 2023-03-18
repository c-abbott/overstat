import sqlite3
from owl_api import OWLAPI
from dotenv import load_dotenv

load_dotenv()

# Initialize the OWLAPI class
api = OWLAPI()

# Connect to the database (this will create a new file called "overstat.db" if it doesn't exist)
conn = sqlite3.connect("overstat.db")
cursor = conn.cursor()

# Create the necessary tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY,
    competition_id TEXT,
    conclusion TEXT,
    end_timestamp INTEGER,
    local_time_zone TEXT,
    local_scheduled_date TEXT,
    season_id TEXT,
    start_timestamp INTEGER,
    actual_start_timestamp INTEGER,
    actual_end_timestamp INTEGER,
    state TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS match_teams (
    match_id INTEGER,
    team_id INTEGER,
    score INTEGER,
    winner BOOLEAN,
    FOREIGN KEY(match_id) REFERENCES matches(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS match_players (
    match_id INTEGER,
    player_id INTEGER,
    FOREIGN KEY(match_id) REFERENCES matches(id)
)
""")

# Commit the changes and close the connection to the database
conn.commit()

# Fetch the data from the API
data = api.fetch_owl_data()

# Insert the data into the database
for match_id, match_data in data.items():
    cursor.execute("""
    INSERT INTO matches (id, competition_id, conclusion, end_timestamp, local_time_zone, local_scheduled_date, season_id, start_timestamp, actual_start_timestamp, actual_end_timestamp, state)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    # TODO: completionId is not in the API response, need to fix this
    """, (match_id, match_data['competitionId'], match_data['conclusion'], match_data['endTimestamp'], match_data['localTimeZone'], match_data['localScheduledDate'], match_data['seasonId'], match_data['startTimestamp'], match_data['actualStartTimestamp'], match_data['actualEndTimestamp'], match_data['state']))

    for team_id, team_data in match_data['teams'].items():
        cursor.execute("""
        INSERT INTO match_teams (match_id, team_id, score, winner)
        VALUES (?, ?, ?, ?)
        """, (match_id, team_id, team_data['score'], team_id == match_data['winner']))

    for player_id in match_data['players']:
        cursor.execute("""
        INSERT INTO match_players (match_id, player_id)
        VALUES (?, ?)
        """, (match_id, player_id))

# Commit the changes and close the connection to the database
conn.commit()
conn.close()
