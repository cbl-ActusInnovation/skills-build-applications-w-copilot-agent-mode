# OctoFit Tracker Activity Data

This directory contains initial data for the OctoFit Tracker application.

## activities.json

This file contains the list of activities/clubs available in the OctoFit Tracker system.

Each activity has the following fields:
- `name`: The name of the activity/club
- `description`: A detailed description of what the activity involves
- `schedule`: When the activity meets
- `max_attendance`: Maximum number of participants
- `activity_type`: The type of activity (e.g., "club", "sport", "fitness")

This data can be loaded into the Django application using the database population command when the application is set up.
