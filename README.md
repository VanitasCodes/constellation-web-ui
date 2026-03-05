# Constellation Web Interface

A web-based control panel for monitoring and controlling Constellation satellite setups, built as a GSoC 2026 evaluation task for DESY.

## Features

- **Header Bar**: Displays satellite count, global state indicator, and connection status
- **Control Panel**: Command buttons (Initialize, Launch, Start, Stop, Land) with state-aware enabling/disabling, and Run ID input
- **Satellite Cards**: Individual satellite status with expandable details, state badges, and context-aware action buttons
- **Log Viewer**: Real-time log display with level filtering, source filtering, search, and auto-scroll

## Satellite State Machine

The interface implements the Constellation FSM:

```
NEW → [initialize] → INIT → [launch] → ORBIT → [start] → RUN
INIT ← [land] ← ORBIT ← [stop] ← RUN
```

**States**: NEW, INIT, ORBIT, RUN, SAFE, ERROR, DEAD

## Tech Stack

- **Framework**: SvelteKit (Svelte 5)
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
│   ├── SatelliteCard.svelte  # Individual satellite display
│   └── LogViewer.svelte      # Log panel with filtering
├── routes/
│   └── +page.svelte          # Main dashboard
└── app.css                   # Global styles
```

## Author

Vishwajeet Singh