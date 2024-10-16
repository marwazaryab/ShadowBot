# :robot: ShadowBot
A bot that verifies and assigns roles to participants and tells them their team number for the 2024 Girls in STEAM Olympics.

## :cherry_blossom: Features

- **User Verification:** Users can verify themselves using their registered email addresses.
- **Role Assignment:** Automatically assigns users to a "Participant" role and specific team roles (e.g., Team 1, Team 2) upon verification.
- **Error Handling:** Provides feedback on success and failure, ensuring a smooth user experience.

## :butterfly: Requirements

- Python 3.8 or higher.
- Discord.py library (v2.0 or higher).
- A Discord bot token.

## :lady_beetle: Installation

1. Clone the repository.
2. Create a `.env` file with ur discord token saved in a variable titled "DISCORD_TOKEN".
3. Create a `registered_users.json` file containing a hashmap of registered email addresses (key) and their corresponding team numbers (value).
