<script>
  let { satellites = [], runId = $bindable('run_001'), oncommand } = $props();

  const commands = [
    {
      name: 'initialize',
      label: 'Initialize',
      color: '#4263eb',
      fromStates: ['NEW', 'ERROR', 'SAFE'],
    },
    {
      name: 'launch',
      label: 'Launch',
      color: '#3b5bdb',
      fromStates: ['INIT'],
    },
    {
      name: 'start',
      label: 'Start',
      color: '#2b8a3e',
      fromStates: ['ORBIT'],
    },
    {
      name: 'stop',
      label: 'Stop',
      color: '#c92a2a',
      fromStates: ['RUN'],
    },
    {
      name: 'land',
      label: 'Land',
      color: '#e8590c',
      fromStates: ['ORBIT'],
    },
  ];

  function isDisabled(fromStates) {
    return !satellites.some((s) => fromStates.includes(s.state));
  }
</script>

<div class="panel">
  <div class="buttons">
    {#each commands as cmd}
      <button
        style="--btn-color: {cmd.color}"
        disabled={isDisabled(cmd.fromStates)}
        onclick={() => oncommand?.(cmd.name)}
      >
        {cmd.label}
      </button>
    {/each}
  </div>
  <div class="run-id">
    <label for="run-id-input">Run ID</label>
    <input
      id="run-id-input"
      type="text"
      bind:value={runId}
      placeholder="Run identifier..."
    />
  </div>
</div>

<style>
  .panel {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 24px;
    background: #fff;
    border-bottom: 1px solid #e0e2e6;
  }

  .buttons {
    display: flex;
    gap: 8px;
  }

  .buttons button {
    padding: 7px 20px;
    border: none;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    background: var(--btn-color);
    cursor: pointer;
    transition:
      opacity 0.12s,
      transform 0.1s;
  }

  .buttons button:hover:not(:disabled) {
    opacity: 0.88;
    transform: translateY(-1px);
  }

  .buttons button:active:not(:disabled) {
    transform: translateY(0);
  }

  .buttons button:disabled {
    background: #ced4da;
    color: #868e96;
    cursor: not-allowed;
  }

  .run-id {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .run-id label {
    font-size: 12px;
    font-weight: 600;
    color: #868e96;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .run-id input {
    padding: 7px 12px;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    font-size: 13px;
    font-family: 'JetBrains Mono', monospace;
    color: #343a40;
    width: 180px;
    outline: none;
    background: #f8f9fa;
    transition:
      border-color 0.15s,
      background 0.15s;
  }

  .run-id input:focus {
    border-color: #4263eb;
    background: #fff;
  }

  @media (max-width: 768px) {
    .panel {
      flex-direction: column;
      gap: 12px;
      padding: 12px 16px;
    }
    .buttons {
      flex-wrap: wrap;
    }
  }
</style>
