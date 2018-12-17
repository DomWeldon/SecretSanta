"""Store for stuff."""

EVERYONE = ("🧔", "🧕", "👱", "🤹", "🛀", "🐺", "🦊")
"""People in secret santa."""


def merry_christmas() -> None:
    """Print some nice christmas stuff"""
    print(f"{'🎄'*5}🎅🤶MERRY CHRISTMAS EVERYONE!🦃🌰{'🎄'*5}")


def secret_santa() -> None:
    """Explain what we're doing"""

    print(
        f"Arranging a Secret Santa for {len(EVERYONE)} people: {', '.join(EVERYONE)}"
    )
