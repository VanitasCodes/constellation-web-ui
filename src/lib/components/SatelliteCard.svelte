<script>
  import { slide } from 'svelte/transition';

  let { satellite, oncommand } = $props();
  let expanded = $state(false);

  const stateColors = {
    NEW: { bg: '#e9ecef', text: '#495057' },
    INIT: { bg: '#dbe4ff', text: '#364fc7' },
    ORBIT: { bg: '#fff3bf', text: '#e67700' },
    RUN: { bg: '#d3f9d8', text: '#2b8a3e' },
    SAFE: { bg: '#ffe8cc', text: '#d9480f' },
    ERROR: { bg: '#ffe3e3', text: '#c92a2a' },
  };

  const singleActions = {
    NEW: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
    INIT: { cmd: 'launch', label: 'Launch', color: '#3b5bdb' },
    RUN: { cmd: 'stop', label: 'Stop', color: '#c92a2a' },
    SAFE: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
    ERROR: { cmd: 'initialize', label: 'Initialize', color: '#4263eb' },
  };

  const orbitActions = [
    { cmd: 'start', label: 'Start', color: '#2b8a3e' },
    { cmd: 'land', label: 'Land', color: '#e8590c' },
  ];

  let colors = $derived(stateColors[satellite.state] ?? stateColors.NEW);
  let single = $derived(singleActions[satellite.state]);
  let isOrbit = $derived(satellite.state === 'ORBIT');
</script>

<div class="card">
  <div class="top">
    <button class="name" onclick={() => (expanded = !expanded)}>
      <svg class="chevron" class:rotated={expanded} viewBox="0 0 12 12">
        <path
          d="M4 2 L8 6 L4 10"
          fill="none"
          stroke="currentColor"
          stroke-width="1.5"
          stroke-linecap="round"
        />
      </svg>
      {satellite.name}
    </button>
    <span class="badge" style="background: {colors.bg}; color: {colors.text}">
      {satellite.state}
    </span>
  </div>
  <p class="message">{satellite.lastMessage}</p>

  {#if expanded}
    <div class="details" transition:slide={{ duration: 150 }}>
      <div class="row">
        <span class="key">Host</span>
        <span class="val">{satellite.host}</span>
      </div>
      <div class="row">
        <span class="key">Port</span>
        <span class="val">{satellite.port}</span>
      </div>
      <div class="row">
        <span class="key">State</span>
        <span class="val">{satellite.state}</span>
      </div>
    </div>
  {/if}

  {#if isOrbit}
    <div class="split-actions">
      {#each orbitActions as act}
        <button
          class="action"
          style="background: {act.color}"
          onclick={() => oncommand?.(satellite.name, act.cmd)}
        >
          {act.label}
        </button>
      {/each}
    </div>
  {:else if single}
    <button
      class="action full"
      style="background: {single.color}"
      onclick={() => oncommand?.(satellite.name, single.cmd)}
    >
      {single.label}
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
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 14px;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    color: #1a1b1e;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    transition: color 0.12s;
  }

  .name:hover {
    color: #4263eb;
  }

  .chevron {
    width: 12px;
    height: 12px;
    color: #adb5bd;
    transition: transform 0.15s ease;
    flex-shrink: 0;
  }

  .chevron.rotated {
    transform: rotate(90deg);
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
    padding-left: 18px;
  }

  .details {
    margin-bottom: 14px;
    padding: 10px 0;
    border-top: 1px solid #f1f3f5;
    border-bottom: 1px solid #f1f3f5;
  }

  .row {
    display: flex;
    gap: 12px;
    font-size: 12px;
    padding: 2px 0;
  }

  .key {
    color: #868e96;
    font-weight: 600;
    min-width: 50px;
  }

  .val {
    color: #343a40;
    font-family: 'JetBrains Mono', monospace;
  }

  .action {
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

  .action.full {
    width: 100%;
  }

  .split-actions {
    display: flex;
    gap: 8px;
  }

  .split-actions .action {
    flex: 1;
  }
</style>
