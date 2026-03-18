# Constellation Web Interface

A web-based control panel for monitoring and controlling Constellation satellite setups, built as a GSoC 2026 evaluation task for DESY.

## Features

- **Header Bar**: Displays satellite count, global state indicator, and connection status
- **Control Panel**: Command buttons (Initialize, Launch, Start, Stop, Land) with state-aware enabling/disabling, and Run ID input
- **Satellite Cards**: Individual satellite status with prominent state banner, expandable details, and context-aware action buttons
- **Log Viewer**: Real-time log display with level filtering, source filtering, search, auto-scroll, and fixed-height layout

## Satellite State Machine

The interface implements the full Constellation FSM including transitional states:

**Steady states**: NEW, INIT, ORBIT, RUN, SAFE, ERROR, DEAD

**Transitional states**: initializing, launching, landing, starting, stopping, reconfiguring, interrupting

```

NEW → [initialize] → initializing → INIT → [launch] → launching → ORBIT → [start] → starting → RUN
INIT ← [landing] ← ORBIT ← [stopping] ← RUN

```

Commands are disabled during transitional states. A spinner animation indicates the transition is in progress. Transitional states resolve automatically after a brief delay, simulating real satellite behavior.

**Additional transitions**:

- `reconfigure`: ORBIT → reconfiguring → ORBIT
- `interrupt`: ORBIT or RUN → interrupting → SAFE
- `initialize`: ERROR or SAFE → initializing → INIT (recovery path)

## Tech Stack

- **Framework**: SvelteKit (Svelte 5 with runes)
- **Styling**: Custom CSS with responsive design
- **Fonts**: DM Sans, JetBrains Mono

## Getting Started

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

## Project Structure

```
src/
├── lib/components/
│   ├── HeaderBar.svelte      # Top bar with status indicators
│   ├── ControlPanel.svelte   # Global command buttons
│   ├── SatelliteCard.svelte  # Individual satellite display with state banner
│   └── LogViewer.svelte      # Log panel with filtering
├── routes/
│   ├── +layout.svelte        # App layout
│   └── +page.svelte          # Main dashboard with FSM logic
└── app.css                   # Global styles
```

## AI Usage

Claude was used for initial project scaffolding, maintaining consistent code patterns across components, and iterating on visual designs to compare layout options. The majority of implementation, layout decisions, and component structure were done independently based on the MissionControl and Observatory references from the Constellation documentation.

## Author

Vishwajeet Singh
