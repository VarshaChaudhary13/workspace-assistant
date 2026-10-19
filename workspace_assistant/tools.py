from .google_auth import gmail, drive, calendar


def search_gmail(query: str, max_results: int = 5) -> dict:
    """Search the user's Gmail using Gmail search syntax."""
    res = gmail.users().messages().list(
        userId="me", q=query, maxResults=max_results
    ).execute()
    results = []
    for message in res.get("messages", []):
        msg = gmail.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "Date"],
        ).execute()
        headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
        results.append(
            {
                "subject": headers.get("Subject"),
                "from": headers.get("From"),
                "date": headers.get("Date"),
                "snippet": msg.get("snippet"),
            }
        )
    return {"messages": results}


def search_drive(query: str, max_results: int = 5) -> dict:
    """Search Google Drive file names and content."""
    res = drive.files().list(
        q=f"fullText contains '{query}'",
        pageSize=max_results,
        fields="files(id, name, mimeType, modifiedTime)",
    ).execute()
    return {"files": res.get("files", [])}


def list_events(time_min: str, time_max: str) -> dict:
    """List calendar events between two RFC3339 timestamps."""
    res = calendar.events().list(
        calendarId="primary",
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy="startTime",
    ).execute()
    return {
        "events": [
            {
                "summary": event.get("summary"),
                "start": event["start"].get(
                    "dateTime", event["start"].get("date")
                ),
            }
            for event in res.get("items", [])
        ]
    }
