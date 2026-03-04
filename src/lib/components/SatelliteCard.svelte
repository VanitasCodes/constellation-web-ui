<script>
  let { satellite, oncommand } = $props();

  const stateColors = {
    NEW: { bg: '#e9ecef', text: '#495057' },
    INIT: { bg: '#dbe4ff', text: '#364fc7' },
    ORBIT: { bg: '#fff3bf', text: '#e67700' },
    RUN: { bg: '#d3f9d8', text: '#2b8a3e' },
    SAFE: { bg: '#ffe8cc', text: '#d9480f' },
    ERROR: { bg: '#ffe3e3', text: '#c92a2a' },
  };

  const nextActions = {
    NEW: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
    INIT: { cmd: 'launch', label: 'Launch', color: '#3b5bdb' },
    ORBIT: { cmd: 'start', label: 'Start', color: '#2b8a3e' },
    RUN: { cmd: 'stop', label: 'Stop', color: '#c92a2a' },
    SAFE: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
    ERROR: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
  };

  let colors = $derived(stateColors[satellite.state] ?? stateColors.NEW);
  let action = $derived(nextActions[satellite.state]);
</script>

<div class="card">
  <div class="top">
    <span class="name">{satellite.name}</span>
    <span class="badge" style="background: {colors.bg}; color: {colors.text}">
      {satellite.state}
    </span>
  </div>
  <p class="message">{satellite.lastMessage}</p>
  {#if action}
    <button
      class="action"
      style="background: {action.color}"
      onclick={() => oncommand?.(satellite.name, action.cmd)}
    >
      {action.label}
    </button>
  {/if}
</div>

<style>
  .card {
    background: #fff;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 16px 18px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    transition: box-shadow 0.15s ease;
  }

  .card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }

  .top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }

  .name {
    font-size: 14px;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    color: #1a1b1e;
  }

  .badge {
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: 'JetBrains Mono', monospace;
  }

  .message {
    font-size: 13px;
    color: #868e96;
    margin-bottom: 14px;
  }

  .action {
    width: 100%;
    padding: 8px;
    border: none;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    transition: opacity 0.12s;
  }

  .action:hover {
    opacity: 0.88;
  }
</style>
